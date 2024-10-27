`Matplotlib` es una librería esencial en Python para la creación de gráficos 2D y 3D, desde los más simples hasta los más complejos. Permite visualizar datos de manera clara y efectiva.

## Instalación

Para instalar Matplotlib, usa:

```bash
pip install matplotlib
```

## Importando la librería

```python
import matplotlib.pyplot as plt
```

## Gráfico de líneas

El gráfico de líneas es uno de los más comunes para visualizar la relación entre dos variables:

```python
x = [1, 2, 3, 4]
y = [1, 4, 9, 16]

plt.plot(x, y)
plt.title('Gráfico de línea')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()
```

## Histograma

Un histograma muestra la distribución de un conjunto de datos. Es útil para analizar la frecuencia de los valores:

```python
import numpy as np

data = np.random.randn(1000)  # Generar datos aleatorios
plt.hist(data, bins=30, color='blue', alpha=0.7)
plt.title('Histograma')
plt.xlabel('Valores')
plt.ylabel('Frecuencia')
plt.show()
```

>[!info] El parámetro `bins` controla el número de barras del histograma.

## Gráfico de barras

Los gráficos de barras se usan para comparar diferentes categorías:

```python
categorias = ['A', 'B', 'C', 'D']
valores = [3, 7, 5, 2]

plt.bar(categorias, valores, color='purple')
plt.title('Gráfico de barras')
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.show()
```

Puedes hacer gráficos de barras horizontales con `plt.barh()`.

## Gráfico de dispersión (Scatter plot)

El gráfico de dispersión muestra la relación entre dos variables continuas:

```python
x = np.random.rand(50)
y = np.random.rand(50)

plt.scatter(x, y, color='green')
plt.title('Gráfico de dispersión')
plt.xlabel('Eje X')
plt.ylabel('Eje Y')
plt.show()
```

>[!example]- Personalización de gráficos
> En gráficos de dispersión, puedes usar el parámetro `s` para cambiar el tamaño de los puntos y `c` para cambiar el color de cada punto.

## Gráfico de pastel

Para representar la proporción de diferentes categorías:

```python
etiquetas = ['Manzanas', 'Bananas', 'Cerezas', 'Uvas']
tamaños = [25, 35, 20, 20]

plt.pie(tamaños, labels=etiquetas, autopct='%1.1f%%', startangle=140)
plt.title('Gráfico de pastel')
plt.show()
```

>[!warning] Gráficos de Pastel
> Úsalos solo cuando haya pocas categorías. Muchos elementos pueden hacerlos difíciles de interpretar.

## Gráfico de caja (Boxplot)

Un gráfico de caja ayuda a visualizar la distribución de los datos y los valores atípicos:

```python
data = np.random.randn(100)

plt.boxplot(data)
plt.title('Gráfico de caja')
plt.show()
```

>[!important] Los boxplots son útiles para comparar la distribución de varios grupos de datos de un vistazo.

## Personalización avanzada

Matplotlib ofrece muchas opciones de personalización, como ajustar los límites de los ejes, cambiar el tamaño de la figura o añadir leyendas:

- Ajustar los ejes

	```python
	plt.xlim(0, 10)
	plt.ylim(0, 20)
	```

- Cambiar el tamaño de la figura

	```python
	plt.figure(figsize=(8, 6))
	```

- Añadir una leyenda

	```python
	plt.plot(x, y, label='Línea 1')
	plt.plot(x, [2, 5, 7, 10], label='Línea 2')
	plt.legend(loc='upper left')
	```

## Guardando gráficos

Para guardar un gráfico:

```python
plt.savefig('grafico.png', dpi=300, bbox_inches='tight')
```

>[!info]- `dpi`
> Usa `dpi` para controlar la resolución y `bbox_inches='tight'` para ajustar los márgenes del gráfico.


>[!tip] **Explora más**  
> La documentación oficial de Matplotlib es muy útil para descubrir funcionalidades más avanzadas y nuevos tipos de gráficos: https://matplotlib.org/stable/contents.html