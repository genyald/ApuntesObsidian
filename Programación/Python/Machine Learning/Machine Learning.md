#MachineLearning #IA
## Historia

1. **1943**: *Warren McCulloch* y *Walter Pitts* publican "A Logical Calculus of the Ideas Immanent in Nervous Activity", sentando las bases de las redes neuronales artificiales. Su modelo se basaba en las neuronas biológicas y su funcionamiento lógico, precursor de las ideas actuales sobre las RNA.

2. **1958**: *Frank Rosenblatt* desarrolla el **perceptrón**, uno de los primeros modelos computacionales de una red neuronal. El perceptrón podía aprender tareas básicas, pero tenía limitaciones importantes, como la incapacidad de resolver problemas no lineales.

3. **1969**: *Marvin Minsky* y *Seymour Papert* publican "Perceptrons", un libro que demuestra las limitaciones de los perceptrones para resolver problemas complejos como el **XOR**. Este trabajo llevó a una reducción del interés en las RNA por varios años, conocido como el "primer invierno de la IA".

4.  **Años 80**: Resurge el interés por las redes neuronales gracias a la introducción de la técnica de **retropropagación del error** (*backpropagation*) por *Geoffrey Hinton*, *David Rumelhart* y *Ronald J. Williams*. Este método resolvió problemas con múltiples capas de neuronas, mejorando la capacidad de aprendizaje de las redes.

5. **1990**: Las RNA pierden parte de su popularidad en favor de nuevas técnicas de Machine Learning como el **Support Vector Machine** (SVM). Estas técnicas eran más fáciles de entrenar y funcionaban mejor en problemas específicos.

6. **2006**: *Geoffrey Hinton* y su equipo desarrollan la técnica de **preentrenamiento de redes profundas** utilizando máquinas de Boltzmann restringidas, abriendo el camino para el entrenamiento de redes neuronales profundas, conocidas hoy como **Deep Learning**.

7. **2012**: Las redes neuronales resurgen con fuerza cuando *Geoffrey Hinton*, *Alex Krizhevsky* y *Ilya Sutskever* ganan el reto **ImageNet** utilizando una **Red Neuronal Convolucional** (CNN). Esta victoria marcó un punto de inflexión en el campo del *Deep Learning*.

8. **2014**: *Ian Goodfellow* y su equipo introducen las **Generative Adversarial Networks** (GANs), una arquitectura de RNA en la que dos redes compiten entre sí. Las GANs revolucionan la generación de imágenes y otros datos sintéticos.

9. **2017**: El equipo de *Google Brain* presenta los **Transformers**, una arquitectura de RNA especializada en secuencias de datos, como el lenguaje natural. Los transformers impulsaron el desarrollo de modelos como BERT y GPT, fundamentales para tareas de procesamiento de lenguaje natural (NLP).

10. **2020**: El modelo **GPT-3**, basado en transformers, demuestra la capacidad de las RNA para generar texto coherente y creativo, marcando avances significativos en la inteligencia artificial generativa.

## Notas adicionales

- Las **Redes Neuronales Convolucionales (CNN)** son especialmente eficaces para el reconocimiento de imágenes. Su arquitectura permite a las máquinas interpretar patrones visuales de forma similar al cerebro humano.

- Los **Transformers** son esenciales para modelos de lenguaje como **GPT** y **BERT**, que han transformado la forma en que las máquinas procesan y generan lenguaje natural.

- Las **GANs** permiten crear imágenes, música y otros datos sintéticos, abriendo nuevos horizontes en campos como el arte digital y la simulación de datos.





### Limitaciones de la Neurona M-P

- Solo puede recibir valores binarios, la mayoría de problemas del mundo real prescinde de otro tipo de valores.
- Requiere una selección del `threshold` de manera manual.
- No se le puede asignar un peso mayor a cada una de las entradas, todas valen lo mismo.
- No son capaces de resolver problemas que sean linealmente separables, como la compuerta XOR.

# Aprendizaje Supervisado y no Supervisado

Existen dos principales pendientes que resultan de la combinacion del aprendizaje supervisado y el no supervisado:

- Semi-supervisado
- Reforzado

La mayoría de aplicaciones de técnicas de machine learning en el mundo real se van solamente para supervisado y no supervisado.

## Aprendizaje Supervisado

El **aprendizaje supervisado** es un tipo de **Machine Learning** en el que se entrena un modelo utilizando un conjunto de datos **etiquetados**. Cada entrada en el conjunto de datos tiene un **par de entrada y salida**, lo que permite al modelo o función hipótesis aprender a mapear correctamente las entradas a las salidas.

## Clasificación vs Regresión
Dentro del aprendizaje supervisado, los modelos se dividen en dos grandes categorías:

- **Modelos de Clasificación:** Se utilizan cuando las salidas son **etiquetas categóricas**. El objetivo es asignar las entradas a una categoría discreta.
- **Modelos de Regresión:** Se utilizan cuando las salidas son **valores continuos**. El objetivo es predecir un valor numérico a partir de las entradas.

### Modelos de Clasificación

La **clasificación** es un tipo de problema en el que el modelo debe asignar cada entrada a una de varias **clases**. Es decir, el modelo predice categorías discretas como "spam/no spam" o "perro/gato".

#### Ejemplos comunes de modelos de clasificación:
- **Máquinas de soporte vectorial (SVM)**
- **K-Nearest Neighbors (KNN)**
- **Árboles de decisión**
- **Redes neuronales**

#### Ejemplo de Clasificación: Spam o No Spam
Un ejemplo típico de **clasificación** es la detección de correos electrónicos spam:

- **Entradas (features):** Palabras clave, enlaces, longitud del correo, etc.
- **Salidas (etiqueta):** "Spam" o "No spam".
- **Objetivo:** El modelo aprende a clasificar correos electrónicos en una de estas dos categorías.

```bash
# Ejemplo de clasificación usando sklearn (logistic regression para clasificación binaria)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Supongamos que X contiene las características del correo y y es la etiqueta (spam o no)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de clasificación (regresión logística)
model = LogisticRegression()
model.fit(X_train, y_train)

# Evaluación del modelo
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
```

---

### Modelos de Regresión

La **regresión** es un tipo de problema en el que el modelo debe predecir un valor **continuo**. Por ejemplo, predecir el precio de una casa en función de características como el tamaño, la ubicación, etc.

#### Ejemplos comunes de modelos de regresión:
- **Regresión lineal**
- **Regresión polinómica**
- **Árboles de decisión (para regresión)**
- **Redes neuronales (para valores continuos)**

#### Ejemplo de Regresión: Precio de una Casa
Un ejemplo típico de **regresión** es predecir el precio de una casa:

- **Entradas (features):** Tamaño de la casa, número de habitaciones, ubicación.
- **Salidas (valor continuo):** Precio de la casa.
- **Objetivo:** El modelo aprende a predecir el precio en función de las características de la casa.

```bash
# Ejemplo de regresión usando sklearn (regresión lineal)
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Supongamos que X contiene las características de la casa y y es el precio
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predicción y evaluación del modelo
y_pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, y_pred))
```

---

## Aprendizaje No Supervisado

### ¿Qué es el Aprendizaje No Supervisado?
En el **aprendizaje no supervisado**, no se cuenta con datos etiquetados. El objetivo del modelo es **descubrir patrones ocultos** en los datos, como agrupamientos (clusters) o asociaciones entre variables.

### Ejemplos comunes de técnicas de aprendizaje no supervisado:
- **Clustering (agrupamiento):** Como el algoritmo K-means.
- **Reducción de dimensionalidad:** Como el PCA (Análisis de Componentes Principales).

### Ejemplo de Clustering: Segmentación de Clientes
Un ejemplo típico es la **segmentación de clientes**, donde se agrupan en función de su comportamiento:

- **Entradas (features):** Información sobre hábitos de compra, ingresos, edad, etc.
- **Objetivo:** Encontrar grupos (clusters) de clientes con comportamientos similares.

#### Algoritmo K-Means
Uno de los algoritmos más populares en el aprendizaje no supervisado es **K-means**, que agrupa los datos en **K clusters**.

```bash
# Ejemplo de clustering usando sklearn
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Supongamos que X contiene las características de los clientes
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

# Visualización del resultado
plt.scatter(X[:, 0], X[:, 1], c=kmeans.labels_, cmap='viridis')
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='red')  # Los centroides
plt.show()
```

---

## Diferencias entre Aprendizaje Supervisado y No Supervisado

| Característica               | Aprendizaje Supervisado  | Aprendizaje No Supervisado |
|------------------------------|--------------------------|----------------------------|
| Datos                        | Etiquetados               | No etiquetados              |
| Objetivo                     | Predecir salidas conocidas | Descubrir patrones ocultos  |
| Tipo de Salida               | Categórica (clasificación) o continua (regresión) | Grupos o asociaciones      |
| Ejemplos de Algoritmos        | SVM, Regresión lineal     | K-means, PCA                |

---

## Conclusiones
- El **aprendizaje supervisado** es útil cuando se cuenta con datos etiquetados y se desea predecir salidas para nuevas entradas, ya sea mediante **clasificación** o **regresión**.
- El **aprendizaje no supervisado** se aplica cuando no se tienen etiquetas y se busca descubrir patrones o relaciones ocultas.

---

### Fuentes
- [Warren McCulloch y Walter Pitts - Redes Neuronales Artificiales (1943)](https://www.cs.cmu.edu/~jlepping/Class/10715/reading/McCulloch.and.Pitts.pdf)
- [ImageNet Challenge y Geoffrey Hinton (2012)](https://www.cs.toronto.edu/~fritz/absps/imagenet.pdf)
- "Perceptrons" - Minsky y Papert (1969)
- [Backpropagation - Hinton et al. (1986)](https://www.nature.com/articles/nature24270)
- [GANs - Ian Goodfellow (2014)](https://arxiv.org/abs/1406.2661)