# Clasificación de Imágenes de Comida (Transfer Learning)

Este proyecto utiliza modelos de Deep Learning (entrenados con Teachable Machine) para clasificar diferentes tipos de comida u objetos relacionados.

## Estructura del Proyecto (actualizada)

- `training/images/`: Imágenes originales organizadas por categoría (estas son las imágenes que se usaron para entrenar los modelos).
  - `training/images/01_soup`
  - `training/images/02_main`
  - `training/images/03_salad`
  - `training/images/04_dessert`
  - `training/images/05_nofood`
- `training/models/`: Contiene las carpetas con los modelos exportados desde Teachable Machine. Cada subcarpeta incluye `keras_model.h5` y `labels.txt`.
  - Ejemplo: `training/models/10_samples_1-10.keras/keras_model.h5`
- `test/`: Imágenes para evaluación (nombres usados para inferir la etiqueta verdadera).
- `evaluate_models.py`: Script para evaluar modelos frente a las imágenes en `test/`.
- `check_tf.py`: Script de utilidad para verificar la instalación de TensorFlow/Keras.

## Cómo reproducir el entrenamiento (Teachable Machine)

1.  Accede a https://teachablemachine.withgoogle.com/ y crea un "Image Project".
2.  Crea las clases y nómbralas: `soup`, `main`, `salad`, `dessert`, `nofood`.
3.  Sube las imágenes desde `training/images/<carpeta_de_clase>` a la clase correspondiente.
    - Por ejemplo, para `soup` sube las imágenes de `training/images/01_soup`.
4.  Entrena el modelo en Teachable Machine.
5.  Exporta el modelo (TensorFlow -> Keras) y coloca el contenido descomprimido en una carpeta dentro de `training/models/`.
    - Ejemplo: `training/models/mi_modelo/keras_model.h5` y `training/models/mi_modelo/labels.txt`.

## Ejecución de la Evaluación (actualizado)

1.  Instala dependencias si es necesario:
```bash
pip install tensorflow pillow numpy
```
2.  Coloca las imágenes de prueba en `test/`.
3.  Nombres de archivo aceptados (para que el script determine la etiqueta verdadera):
   - Prefijo por nombre: `salad_01.jpg`, `main_02.png`, etc.
  - Prefijo numérico: `01_...` -> `soup`, `02_...` -> `main`, `03_...` -> `salad`, `04_...` -> `dessert`, `05_...` -> `nofood`.
     - Ejemplo: `03_mi_ensalada.jpg` será interpretado como `salad`.
4.  Ejecuta la evaluación:
```bash
python evaluate_models.py
```
5.  `evaluate_models.py` leerá las carpetas listadas en la variable `MODEL_FOLDERS` dentro de `training/models/` y generará métricas por modelo.

## Requisitos
- Python 3.x
- tensorflow / tf-keras
- pillow
- numpy

## Notas
- Asegúrate de que cada carpeta de modelo en `training/models/` contenga `keras_model.h5`.
- Las imágenes de entrenamiento originales se guardan en `training/images/` para referencia y reproducibilidad.

## Evaluar un solo modelo (tu modelo)

Si quieres evaluar únicamente tu modelo (en lugar de los modelos incluidos), tienes estas opciones:

1) Opción A — Rápido, sin cambios de código

  - Crea una carpeta para tu modelo en `training/models/`, por ejemplo `training/models/mi_model/`.
  - Coloca `keras_model.h5` y `labels.txt` dentro de esa carpeta.
  - Edita la lista `MODEL_FOLDERS` en `evaluate_models.py` y reemplaza su contenido por:

```python
MODEL_FOLDERS = ['mi_model']
```

  - Ejecuta:

```bash
python evaluate_models.py
```

2) Opción B — Invocación directa (sin editar el script)

  - Ejecuta la función `evaluate_model` directamente desde la línea de comandos:

```bash
python -c "from evaluate_models import evaluate_model; evaluate_model('training/models/mi_model/keras_model.h5','mi_model')"
```

3) Opción C — Recomendado: habilitar CLI (sin editar el archivo cada vez)

  - Añade soporte por argumentos en `evaluate_models.py` para pasar `--model-folder` o `--model-path`.
  - Ejemplos de uso:

```bash
# Evaluar por carpeta dentro de training/models
python evaluate_models.py --model-folder mi_model

# Evaluar por ruta directa al archivo h5
python evaluate_models.py --model-path training/models/mi_model/keras_model.h5
```

  - Comportamiento:
    - `--model-folder` buscará `training/models/<folder>/keras_model.h5`.
    - `--model-path` usará la ruta exacta que pases y mostrará como nombre del modelo la carpeta padre.

Si quieres, implemento la Opción C en `evaluate_models.py` y subo el cambio para que puedas usar los flags `--model-folder` y `--model-path`.
