import os
import sys
import numpy as np

# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
os.environ["TF_USE_LEGACY_KERAS"] = "1"

import tf_keras as keras
from tf_keras.models import load_model
from tf_keras.preprocessing import image
from tf_keras.layers import DepthwiseConv2D

# Fix for "Unrecognized keyword arguments passed to DepthwiseConv2D: {'groups': 1}"
class CustomDepthwiseConv2D(DepthwiseConv2D):
    def __init__(self, **kwargs):
        if 'groups' in kwargs:
            del kwargs['groups']
        super().__init__(**kwargs)


# Suppress TensorFlow warnings
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Configuration
TEST_DIR = 'test'
TRAINING_DIR = 'training'
MODEL_FOLDERS = [
    '10_samples_1-10.keras',
    '10_samples_11-20.keras',
    '10_samples_21-30.keras',
    '20_samples_06-25.keras',
    '30_samples_01-30.keras'
]

CLASS_MAP = {
    'soap': 0,
    'main': 1,
    'salad': 2,
    'dessert': 3,
    'nofood': 4
}

NUMBER_MAP = {
    '01': 'soap',
    '02': 'main',
    '03': 'salad',
    '04': 'dessert',
    '05': 'nofood'
}

# Reverse map for display
INT_TO_CLASS = {v: k for k, v in CLASS_MAP.items()}

def get_true_label(filename):
    # Filename format: class_test... OR 01_... OR 1_...
    # Split by underscore to get the prefix
    parts = filename.split('_')
    prefix = parts[0]

    # Check if prefix is a number in our map (e.g. 01, 02)
    if prefix in NUMBER_MAP:
        class_name = NUMBER_MAP[prefix]
        return CLASS_MAP[class_name]

    # Check if prefix is directly the class name
    if prefix in CLASS_MAP:
        return CLASS_MAP[prefix]
        
    return None

def preprocess_image(img_path):
    # Load image with target size 224x224
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    # Expand dimensions to match model input (1, 224, 224, 3)
    img_array = np.expand_dims(img_array, axis=0)
    # Normalize the image (Teachable Machine standard: (x / 127.5) - 1)
    normalized_image_array = (img_array.astype(np.float32) / 127.5) - 1
    return normalized_image_array

def evaluate_model(model_path, model_name):
    print(f"\n{'='*60}")
    print(f"Evaluando modelo: {model_name}")
    print(f"{'='*60}")
    
    try:
        # Compile=False is important for TM models
        model = load_model(model_path, custom_objects={'DepthwiseConv2D': CustomDepthwiseConv2D}, compile=False)
    except Exception as e:
        print(f"Error cargando el modelo {model_path}: {e}")
        return

    total_images = 0
    total_correct = 0
    
    # Metrics per class
    class_metrics = {k: {'total': 0, 'correct': 0, 'false_positives': 0, 'false_negatives': 0} for k in CLASS_MAP.keys()}
    
    # Get list of test files
    test_files = [f for f in os.listdir(TEST_DIR) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    
    if not test_files:
        print("No se encontraron imágenes en la carpeta test.")
        return

    print(f"Procesando {len(test_files)} imágenes de prueba...\n")

    for filename in test_files:
        true_label_idx = get_true_label(filename)
        
        if true_label_idx is None:
            print(f"Advertencia: No se pudo determinar la clase para el archivo {filename}. Saltando.")
            continue
            
        img_path = os.path.join(TEST_DIR, filename)
        
        try:
            processed_img = preprocess_image(img_path)
            prediction = model.predict(processed_img, verbose=0)
            predicted_label_idx = np.argmax(prediction)
            
            true_class_name = INT_TO_CLASS[true_label_idx]
            predicted_class_name = INT_TO_CLASS[predicted_label_idx]
            
            # Update metrics
            total_images += 1
            class_metrics[true_class_name]['total'] += 1
            
            if predicted_label_idx == true_label_idx:
                total_correct += 1
                class_metrics[true_class_name]['correct'] += 1
                # print(f"[OK] {filename}: Predicho: {predicted_class_name}")
            else:
                class_metrics[true_class_name]['false_negatives'] += 1
                class_metrics[predicted_class_name]['false_positives'] += 1
                print(f"[FALLO] {filename}: Real: {true_class_name} -> Predicho: {predicted_class_name}")
                
        except Exception as e:
            print(f"Error procesando imagen {filename}: {e}")

    # Calculate and print summary
    accuracy = (total_correct / total_images) * 100 if total_images > 0 else 0
    
    print(f"\n--- Resultados para {model_name} ---")
    print(f"Precisión Global (Accuracy): {accuracy:.2f}% ({total_correct}/{total_images})")
    
    print("\nDetalle por Categoría:")
    print(f"{'Categoría':<15} | {'Total':<6} | {'Aciertos':<8} | {'Fallos (FN)':<12} | {'Precisión':<10}")
    print("-" * 65)
    
    for class_name, metrics in class_metrics.items():
        total = metrics['total']
        correct = metrics['correct']
        fn = metrics['false_negatives']
        acc = (correct / total * 100) if total > 0 else 0
        print(f"{class_name:<15} | {total:<6} | {correct:<8} | {fn:<12} | {acc:.2f}%")

def main():
    for folder in MODEL_FOLDERS:
        model_path = os.path.join(TRAINING_DIR, folder, 'keras_model.h5')
        if os.path.exists(model_path):
            evaluate_model(model_path, folder)
        else:
            print(f"Modelo no encontrado en: {model_path}")

if __name__ == "__main__":
    main()
