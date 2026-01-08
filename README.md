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
  - Los modelos están organizados en carpetas `model01`, `model02`, `model03`, `model04`, `model05`.
  - Cada carpeta contiene `keras_model.h5` y `labels.txt`.
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

## Ejecución de la Evaluación

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
5.  `evaluate_models.py` leerá las carpetas listadas en la variable `MODEL_FOLDERS` dentro de `training/models/` (por ejemplo `model01`, `model02`, ...) y generará métricas por modelo.

## Requisitos
- Python 3.x
- tensorflow / tf-keras
- pillow
- numpy

## Notas
- Asegúrate de que cada carpeta de modelo en `training/models/` contenga `keras_model.h5`.
- Las imágenes de entrenamiento originales se guardan en `training/images/` para referencia y reproducibilidad.

## Evalúa uno o varios modelos propios

Si quieres evaluar modelos propios, hazlo desde una única sección: puedes evaluar uno o varios modelos siguiendo estos pasos.

- Opción 1 — Reemplazar el contenido de las carpetas existentes (recomendado):
  - Sustituye los archivos dentro de `training/models/model01`, `model02`, `model03`, `model04`, `model05` por los de tus modelos. Cada carpeta debe contener:
    - `keras_model.h5`
    - `labels.txt` (lista de etiquetas, una por línea, en el orden de salida del modelo)

- Opción 2 — Añadir una carpeta nueva y apuntar solo a ella:
  - Crea `training/models/mi_model/` y coloca `keras_model.h5` y `labels.txt` dentro.

Después, indica qué carpetas evaluar editando la lista `MODEL_FOLDERS` en `evaluate_models.py`. Ejemplos:

```python
# Evaluar solo el modelo en model01
MODEL_FOLDERS = ['model01']

# Evaluar varios modelos (model02 y model05)
MODEL_FOLDERS = ['model02', 'model05']

# Evaluar una carpeta nueva llamada mi_model
MODEL_FOLDERS = ['mi_model']
```

Finalmente ejecuta:

```bash
python evaluate_models.py
```

Con esto puedes evaluar uno o varios modelos desde la misma sección sin duplicar instrucciones.

---

English

## Evaluate one or several custom models

If you want to use your own models, you can simply replace the contents of the existing folders `model01`, `model02`, `model03`, `model04`, `model05` inside `training/models/` with your model files. Each folder should contain:

- `keras_model.h5`
- `labels.txt` (one label per line, matching the model output order)

Then specify which folders to evaluate by editing the `MODEL_FOLDERS` list in `evaluate_models.py`. Examples:

```python
# Evaluate only the model in model01
MODEL_FOLDERS = ['model01']

# Evaluate multiple models (model02 and model05)
MODEL_FOLDERS = ['model02', 'model05']
```

Finally run:

```bash
python evaluate_models.py
```

This way you do not need to create new folders: just replace the files inside `model01..model05` with your model and update `MODEL_FOLDERS`.

Notas:
- Si usas `run_models.py` o la invocación directa, no necesitas tocar `evaluate_models.py`.
- Asegúrate de que `labels.txt` coincide con el orden de salida del modelo (index 0 = primera etiqueta en `labels.txt`).

