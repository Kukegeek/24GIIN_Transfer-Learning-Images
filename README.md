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

Usando esta opción solo se evaluará el modelo que indiques en `MODEL_FOLDERS`.

## Evaluar uno o varios modelos propios

Si tienes uno o varios modelos propios (no quieres usar los modelos incluidos en `MODEL_FOLDERS`), sigue estas instrucciones:

- Preparación de tus modelos
  - Para cada modelo crea una carpeta en `training/models/` por ejemplo `training/models/mi_model1/`, `training/models/mi_model2/`.
  - En cada carpeta coloca `keras_model.h5` y `labels.txt` (los labels deben listarse en el mismo orden que las salidas del modelo).

- Evaluar un solo modelo
  - Usa cualquiera de las opciones A/B/C descritas arriba (A: editar `MODEL_FOLDERS`, B: invocación directa, C: usar flags CLI si los habilitas).

- Evaluar varios modelos propios (sin editar `evaluate_models.py` cada vez)
  - Opción 1 — Crear un pequeño script `run_models.py` (recomendado):

```python
from evaluate_models import evaluate_model

models = [
    'training/models/mi_model1/keras_model.h5',
    'training/models/mi_model2/keras_model.h5'
]

for path in models:
    name = path.split('/')[-2].split('\\')[-1]
    evaluate_model(path, name)

```

  - Guarda como `run_models.py` en la raíz del proyecto y ejecútalo:
```bash
python run_models.py
```

  - Opción 2 — Ejecutar desde la línea de comandos (ejemplo rápido):
```bash
python - <<'PY'
from evaluate_models import evaluate_model
for p in ['training/models/mi_model1/keras_model.h5','training/models/mi_model2/keras_model.h5']:
    evaluate_model(p, p.split('/')[-2])
PY
```

  - Opción 3 — Editar `MODEL_FOLDERS` temporalmente: reemplaza `MODEL_FOLDERS` por la lista de carpetas que quieras evaluar.

Notas:
- Si usas `run_models.py` o la invocación directa, no necesitas tocar `evaluate_models.py`.
- Asegúrate de que `labels.txt` coincide con el orden de salida del modelo (index 0 = primera etiqueta en `labels.txt`).

