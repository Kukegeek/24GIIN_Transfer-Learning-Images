# Clasificación de Imágenes de Comida (Transfer Learning)

Este proyecto utiliza modelos de Deep Learning (entrenados con Teachable Machine) para clasificar diferentes tipos de comida u objetos relacionados.

## Estructura del Proyecto

*   **training_images/**: Contiene las imágenes originales utilizadas para el entrenamiento, organizadas en carpetas por categoría:
    *   `01_soap`: Jabón (o productos similares)
    *   `02_main`: Plato principal
    *   `03_salad`: Ensalada
    *   `04_dessert`: Postre
    *   `05_nofood`: No comida
*   **training/**: Contiene los modelos entrenados exportados desde Teachable Machine (archivos `.keras` o `.h5` y `labels.txt`). Se han generado varios modelos con diferentes cantidades de muestras para comparar su rendimiento.
*   **test/**: Contiene imágenes para evaluar los modelos.
*   **evaluate_models.py**: Script principal para evaluar el rendimiento de los modelos frente a las imágenes de prueba.
*   **check_tf.py**: Script de utilidad para verificar la instalación de TensorFlow/Keras.

## Cómo reproducir el entrenamiento

Los modelos se han generado utilizando la herramienta online [Teachable Machine](https://teachablemachine.withgoogle.com/) de Google.

1.  Accede a la web de Teachable Machine y crea un "Image Project".
2.  Crea las clases (Class 1, Class 2, etc.) y nómbralas: `soap`, `main`, `salad`, `dessert`, `nofood`.
3.  Sube las imágenes correspondientes desde la carpeta `training_images`.
    *   Para la clase `soap`, usa las imágenes de `training_images/01_soap`.
    *   Para la clase `main`, usa las imágenes de `training_images/02_main`.
    *   Y así sucesivamente.
4.  Entrena el modelo ("Train Model").
5.  Exporta el modelo ("Export Model") seleccionando **TensorFlow** -> **Keras**.
6.  Descarga el archivo zip, descomprímelo y coloca el archivo `keras_model.h5` en una nueva carpeta dentro de `training/` (por ejemplo `training/mi_nuevo_modelo/`).

## Ejecución de la Evaluación

Para evaluar los modelos existentes contra las imágenes de test:

1.  Asegúrate de tener instaladas las dependencias (TensorFlow, Pillow, NumPy).
2.  Coloca tus imágenes de prueba en la carpeta `test/`.
3.  **Importante**: Las imágenes de prueba deben tener un nombre que identifique su clase real para poder verificar si la predicción es correcta. El script soporta dos formatos:
    *   **Prefijo por nombre**: `salad_mi_imagen.jpg`, `main_foto01.png`...
    *   **Prefijo numérico**: 
        *   `01` -> soap
        *   `02` -> main
        *   `03` -> salad
        *   `04` -> dessert
        *   `05` -> nofood
        *   Ejemplo: `03_mi_ensalada.jpg` será tratada como `salad`.
4.  Ejecuta el script:
    ```bash
    python evaluate_models.py
    ```
5.  El script recorrerá todos los modelos definidos en la lista `MODEL_FOLDERS` y mostrará la precisión global y por categoría para cada uno.

## Requisitos
*   Python 3.x
*   tensorflow / tf-keras
*   pillow
*   numpy
