Este prompt esta planedo para que copilot o otro modelo haga las notas como me gustan de estructura:

# **Prompt:**

Convierte el siguiente contenido en un apunte bien estructurado para GitHub. Utiliza `##` para el título principal y `###` para los subtítulos, y así sucesivamente. Incluye explicaciones detalladas después de cada bloque de código. Usa callouts (`>[!info]`, `>[!warning]`, `>[!summary]`, `>[!quote]`, `>[!example]`, `>[!tip]` y `>[!success]`) solo para información muy importante o advertencias. Si hay muchos callouts, agrégalos como plegables usando `-`, por ejemplo: `>[!tip] -`. Asegúrate de que el formato sea claro, coherente y fácil de seguir.

Ejemplo de formato:

# Título Principal

`#Etiqueta1 #Etiqueta2`

Descripción breve del tema, su importancia y aplicación.

## Instalación

Instrucciones para instalar la herramienta o librería.

```bash
# Código para instalación
```

## Importación

```python
# Código para importar la librería
```

---

## Sección de Gráficos o Funciones Comunes

### Nombre del Gráfico o Función

Descripción breve sobre el gráfico o función.

```python
# Código de ejemplo
```

- `comando` - Explicación de la sentencia del comando usado en el código.
- `más comandos` - Otros comandos que puedan ser relevantes.

> [!info] `Descripción adicional o nota importante sobre el gráfico o función.`

### Nombre de Otro Gráfico o Función

Descripción breve sobre otro gráfico o función.

```python
# Código de ejemplo
```

- `comando` - Explicación de la sentencia del comando usado en el código.
- `más comandos` - Otros comandos que puedan ser relevantes.

> [!example] `Descripción sobre personalización o ejemplos prácticos.`

### Nombre de Otro Gráfico o Función

Descripción breve sobre otro gráfico o función.

```python
# Código de ejemplo
```

- `comando` - Explicación de la sentencia del comando usado en el código.
- `más comandos` - Otros comandos que puedan ser relevantes.

> [!warning] `Descripción sobre advertencias o limitaciones.`

---

## Personalización

Descripción general sobre opciones de personalización.

- **Ajuste de Ejes**: Modifica los límites visibles de los ejes.

  ```python
  plt.xlim(min, max)  # Establece límites en el eje X
  plt.ylim(min, max)  # Establece límites en el eje Y
  ```

- **Tamaño de la Figura**: Cambia el tamaño del gráfico.

  ```python
  plt.figure(figsize=(ancho, alto))  # Especifica dimensiones de la figura
  ```

- **Leyendas**: Añade una leyenda para identificar series de datos.

  ```python
  plt.plot(x, y, label='Descripción de la serie')
  plt.legend(loc='ubicación')  # Especifica la ubicación de la leyenda
  ```

### Guardado de Resultados

Instrucciones para guardar el gráfico o resultado.

```python
plt.savefig('nombre_del_archivo.png', dpi=300, bbox_inches='tight')  # Guarda el gráfico
```

> [!info] `Usa 'dpi' para controlar la resolución y 'bbox_inches' para ajustar los márgenes del gráfico.`

---

## Recursos Adicionales

Descripción de recursos, como documentación, tutoriales, etc.

---

## Información Adicional

Descripción de información adicional relevante.

---

## Otro Título que Aborda Otra Sección

Descripción breve de esta nueva sección.