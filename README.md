<table>
  <tr>
    <th style="vertical-align:top; width:50%">Español</th>
    <th style="vertical-align:top; width:50%">English</th>
  </tr>

  <tr>
    <td>
      <h1>Clasificación de Imágenes de Comida (Transfer Learning)</h1>
      <p>Este proyecto utiliza modelos de Deep Learning (entrenados con Teachable Machine) para clasificar diferentes tipos de comida u objetos relacionados.</p>

      <h2>Estructura del Proyecto (actualizada)</h2>
      <ul>
        <li><code>training/images/</code>: Imágenes originales organizadas por categoría (usadas para entrenar).</li>
        <ul>
          <li><code>training/images/01_soup</code></li>
          <li><code>training/images/02_main</code></li>
          <li><code>training/images/03_salad</code></li>
          <li><code>training/images/04_dessert</code></li>
          <li><code>training/images/05_nofood</code></li>
        </ul>
        <li><code>training/models/</code>: Carpetas con modelos exportados (cada una con <code>keras_model.h5</code> y <code>labels.txt</code>).</li>
        <li><code>test/</code>: Imágenes para evaluación.</li>
        <li><code>evaluate_models.py</code>: Script de evaluación.</li>
        <li><code>check_tf.py</code>: Utilidad para verificar TensorFlow/Keras.</li>
      </ul>

      <h2>Cómo reproducir el entrenamiento (Teachable Machine)</h2>
      <ol>
        <li>Accede a <a href="https://teachablemachine.withgoogle.com/">Teachable Machine</a> y crea un Image Project.</li>
        <li>Crea las clases: <code>soup</code>, <code>main</code>, <code>salad</code>, <code>dessert</code>, <code>nofood</code>.</li>
        <li>Sube imágenes desde <code>training/images/&lt;carpeta_de_clase&gt;</code> a la clase correspondiente.</li>
        <li>Entrena y exporta (TensorFlow → Keras), coloca el contenido en <code>training/models/&lt;tu_model&gt;/</code>.</li>
      </ol>

      <h2>Ejecución de la Evaluación</h2>
      <ol>
        <li>Instala dependencias si es necesario:
          <pre><code>pip install tensorflow pillow numpy</code></pre>
        </li>
        <li>Coloca las imágenes de prueba en <code>test/</code>.</li>
        <li>Formatos de nombre aceptados para inferir la etiqueta verdadera:
          <ul>
            <li>Prefijo por nombre: <code>salad_01.jpg</code>, <code>main_02.png</code>, etc.</li>
            <li>Prefijo numérico: <code>01_...</code> → <code>soup</code>, <code>02_...</code> → <code>main</code>, etc.</li>
          </ul>
        </li>
        <li>Ejecuta:
          <pre><code>python evaluate_models.py</code></pre>
        </li>
      </ol>

      <h2>Requisitos</h2>
      <ul>
        <li>Python 3.x</li>
        <li><code>tensorflow</code> / <code>tf-keras</code></li>
        <li><code>pillow</code></li>
        <li><code>numpy</code></li>
      </ul>

      <h2>Evalúa uno o varios modelos propios</h2>
      <p>Dos enfoques:</p>
      <ol>
        <li><strong>Reemplazar carpetas existentes (recomendado)</strong>: sustituye los archivos dentro de <code>training/models/model01..model05</code> por los de tus modelos (cada carpeta debe contener <code>keras_model.h5</code> y <code>labels.txt</code>).</li>
        <li><strong>Añadir una carpeta nueva</strong>: crea <code>training/models/mi_model/</code> y coloca dentro <code>keras_model.h5</code> y <code>labels.txt</code>.</li>
      </ol>

      <p>Editar la lista <code>MODEL_FOLDERS</code> en <code>evaluate_models.py</code> para indicar qué carpetas evaluar:</p>
      <pre><code># Evaluar solo model01
MODEL_FOLDERS = ['model01']

# Evaluar model02 y model05
MODEL_FOLDERS = ['model02', 'model05']

# Evaluar carpeta nueva mi_model
MODEL_FOLDERS = ['mi_model']
      </code></pre>

      <p>Finalmente:</p>
      <pre><code>python evaluate_models.py</code></pre>

      <h2>Notas</h2>
      <ul>
        <li>Asegúrate de que <code>labels.txt</code> coincida con el orden de salida del modelo (index 0 = primera etiqueta).</li>
      </ul>
    </td>

    <td>
      <h1>Food Image Classification (Transfer Learning)</h1>
      <p>This project uses Deep Learning models (exported from Teachable Machine) to classify food and related objects.</p>

      <h2>Project Structure (updated)</h2>
      <ul>
        <li><code>training/images/</code>: Original images organized by category (used for training).</li>
        <ul>
          <li><code>training/images/01_soup</code></li>
          <li><code>training/images/02_main</code></li>
          <li><code>training/images/03_salad</code></li>
          <li><code>training/images/04_dessert</code></li>
          <li><code>training/images/05_nofood</code></li>
        </ul>
        <li><code>training/models/</code>: Folders with models exported from Teachable Machine (each with <code>keras_model.h5</code> and <code>labels.txt</code>).</li>
        <li><code>test/</code>: Images for evaluation.</li>
        <li><code>evaluate_models.py</code>: Evaluation script.</li>
        <li><code>check_tf.py</code>: Utility to verify TensorFlow/Keras.</li>
      </ul>

      <h2>How to Reproduce Training (Teachable Machine)</h2>
      <ol>
        <li>Go to <a href="https://teachablemachine.withgoogle.com/">Teachable Machine</a> and create an Image Project.</li>
        <li>Create classes: <code>soup</code>, <code>main</code>, <code>salad</code>, <code>dessert</code>, <code>nofood</code>.</li>
        <li>Upload images from <code>training/images/&lt;class_folder&gt;</code> to the corresponding class.</li>
        <li>Train and export (TensorFlow → Keras), place the extracted content in <code>training/models/&lt;your_model&gt;/</code>.</li>
      </ol>

      <h2>Running Evaluation</h2>
      <ol>
        <li>Install dependencies if needed:
          <pre><code>pip install tensorflow pillow numpy</code></pre>
        </li>
        <li>Put your test images into <code>test/</code>.</li>
        <li>Accepted filename formats to infer ground-truth label:
          <ul>
            <li>Name prefix by class: <code>salad_01.jpg</code>, <code>main_02.png</code>, etc.</li>
            <li>Numeric prefix: <code>01_...</code> → <code>soup</code>, <code>02_...</code> → <code>main</code>, etc.</li>
          </ul>
        </li>
        <li>Run:
          <pre><code>python evaluate_models.py</code></pre>
        </li>
      </ol>

      <h2>Requirements</h2>
      <ul>
        <li>Python 3.x</li>
        <li><code>tensorflow</code> / <code>tf-keras</code></li>
        <li><code>pillow</code></li>
        <li><code>numpy</code></li>
      </ul>

      <h2>Evaluate one or several custom models</h2>
      <p>Two approaches:</p>
      <ol>
        <li><strong>Replace existing folders (recommended)</strong>: replace files inside <code>training/models/model01..model05</code> with your model files (each folder must contain <code>keras_model.h5</code> and <code>labels.txt</code>).</li>
        <li><strong>Add a new folder</strong>: create <code>training/models/my_model/</code> and place <code>keras_model.h5</code> and <code>labels.txt</code> there.</li>
      </ol>

      <p>Then edit the <code>MODEL_FOLDERS</code> list in <code>evaluate_models.py</code> to indicate which folders to evaluate:</p>
      <pre><code># Evaluate only model01
MODEL_FOLDERS = ['model01']

# Evaluate model02 and model05
MODEL_FOLDERS = ['model02', 'model05']

# Evaluate newly added folder my_model
MODEL_FOLDERS = ['my_model']
      </code></pre>

      <p>Finally run:</p>
      <pre><code>python evaluate_models.py</code></pre>

      <h2>Additional notes</h2>
      <ul>
        <li>If you use a helper script like <code>run_models.py</code> or invoke evaluation directly, you may not need to edit <code>evaluate_models.py</code>.</li>
        <li>Ensure <code>labels.txt</code> matches the model output order (index 0 = first label).</li>
      </ul>
    </td>
  </tr>

</table>

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
---

English

# Food Image Classification (Transfer Learning)

This project uses Deep Learning models (exported from Teachable Machine) to classify food and related objects.

## Project Structure (updated)

- `training/images/`: Original images organized by category (these were used to train the models).
  - `training/images/01_soup`
  - `training/images/02_main`
  - `training/images/03_salad`
  - `training/images/04_dessert`
  - `training/images/05_nofood`
- `training/models/`: Contains folders with models exported from Teachable Machine. Each subfolder includes `keras_model.h5` and `labels.txt`.
  - Models are organized in folders `model01`, `model02`, `model03`, `model04`, `model05`.
  - Each folder contains `keras_model.h5` and `labels.txt`.
- `test/`: Images used for evaluation (file names are used to infer the ground-truth label).
- `evaluate_models.py`: Script to evaluate models against the images in `test/`.
- `check_tf.py`: Utility script to verify TensorFlow/Keras installation.

## How to Reproduce Training (Teachable Machine)

1. Go to https://teachablemachine.withgoogle.com/ and create an Image Project.
2. Create classes and name them: `soup`, `main`, `salad`, `dessert`, `nofood`.
3. Upload images from `training/images/<class_folder>` to the corresponding class.
   - For example, upload images from `training/images/01_soup` to the `soup` class.
4. Train the model in Teachable Machine.
5. Export the model (TensorFlow -> Keras) and place the extracted content into a folder inside `training/models/`.
   - Example: `training/models/my_model/keras_model.h5` and `training/models/my_model/labels.txt`.

## Running Evaluation

1. Install dependencies if needed:
```bash
pip install tensorflow pillow numpy
```
2. Put your test images into `test/`.
3. Accepted filename formats (used by the script to determine the true label):
   - Name prefix by class: `salad_01.jpg`, `main_02.png`, etc.
   - Numeric prefix: `01_...` -> `soup`, `02_...` -> `main`, `03_...` -> `salad`, `04_...` -> `dessert`, `05_...` -> `nofood`.
     - Example: `03_my_salad.jpg` will be interpreted as `salad`.
4. Run evaluation:
```bash
python evaluate_models.py
```
5. `evaluate_models.py` will read the folders listed in the `MODEL_FOLDERS` variable inside `training/models/` (for example `model01`, `model02`, ...) and will print metrics per model.

## Requirements
- Python 3.x
- tensorflow / tf-keras
- pillow
- numpy

## Notes
- Make sure each model folder in `training/models/` contains a `keras_model.h5` file.
- The original training images are kept in `training/images/` for reference and reproducibility.

## Evaluate one or several custom models

You can evaluate one or multiple custom models from a single unified section. Two simple approaches are supported:

- Option 1 — Replace the contents of existing folders (recommended):
  - Replace the files inside `training/models/model01`, `model02`, `model03`, `model04`, `model05` with your model files. Each folder must contain:
    - `keras_model.h5`
    - `labels.txt` (one label per line, in the order of the model output)

- Option 2 — Add a new folder and point to it:
  - Create `training/models/my_model/` and place `keras_model.h5` and `labels.txt` inside.

Then specify which folders to evaluate by editing the `MODEL_FOLDERS` list in `evaluate_models.py`. Examples:

```python
# Evaluate only the model in model01
MODEL_FOLDERS = ['model01']

# Evaluate multiple models (model02 and model05)
MODEL_FOLDERS = ['model02', 'model05']

# Evaluate a newly added folder called my_model
MODEL_FOLDERS = ['my_model']
```

Finally run:

```bash
python evaluate_models.py
```

This allows you to evaluate one or several models from the same instructions without duplication.

## Additional notes
- If you use a helper script like `run_models.py` or invoke evaluation directly, you may not need to edit `evaluate_models.py`.
- Ensure `labels.txt` matches the model output order (index 0 = first label in `labels.txt`).


