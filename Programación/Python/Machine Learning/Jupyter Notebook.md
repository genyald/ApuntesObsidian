#Jupyter #Python

Jupyter Notebook es una aplicación web que permite crear y compartir documentos que contienen código, ecuaciones, visualizaciones y texto narrativo. Es una herramienta muy popular en el ámbito de la ciencia de datos, aprendizaje automático y análisis de datos, ya que permite realizar análisis de datos interactivos y visualizaciones en tiempo real. Jupyter soporta múltiples lenguajes de programación, siendo Python el más comúnmente utilizado.

## Características Principales

- **Celdas Interactivas**: Puedes combinar celdas de código y celdas de texto (Markdown) para crear documentos dinámicos.
- **Visualización de Datos**: Soporta bibliotecas populares como Matplotlib y Seaborn para la visualización de datos.
- **Documentación**: Permite incluir documentación detallada junto con el código, lo que facilita la comprensión y la colaboración.

## Atajos de Teclado

Los atajos de teclado pueden acelerar significativamente tu flujo de trabajo en Jupyter Notebook. Aquí hay algunos de los más útiles:

## Atajos de Teclado en Jupyter Notebook

### Modo Comando (presiona `Esc` para activar)

- **`Enter`**: Cambia a modo de edición.
- **`Y`**: Cambia la celda a código.
- **`M`**: Cambia la celda a Markdown.
- `R`: Cambiar la celda a Raw.
- **`B`**: Inserta una nueva celda debajo.
- **`A`**: Inserta una nueva celda arriba.
- **`D, D`**: Elimina la celda seleccionada.
- **`Z`**: Deshace la última acción.
- **`S`**: Guarda el notebook.
- **`H`**: Muestra la lista de atajos de teclado.
- **`F`**: Busca en el notebook.
- **`L`**: Activa/desactiva la numeración de líneas.
- **`O`**: Activa/desactiva la salida de la celda seleccionada.
- **`Shift + M`**: Combina la celda seleccionada con la celda anterior.
- **`Ctrl + Shift + -`**: Divide la celda en dos en la posición del cursor.

### Modo Edición (presiona `Enter` en una celda de código)

- **`Ctrl + Enter`**: Ejecuta la celda y permanece en la celda actual.
- **`Shift + Enter`**: Ejecuta la celda y selecciona la celda siguiente.
- **`Alt + Enter`**: Ejecuta la celda y crea una nueva celda debajo.
- **`Tab`**: Completa automáticamente el código o muestra sugerencias.
- **`Ctrl + Z`**: Deshace la última acción en la celda.
- **`Ctrl + Y`**: Rehace la última acción deshecha.
- **`Ctrl + A`**: Selecciona todo el contenido de la celda.
- **`Ctrl + /`**: Comenta o descomenta la línea seleccionada.
- **`Ctrl + Shift + P`**: Abre la paleta de comandos.


Aquí tienes un subtítulo más completo que incluye los comandos para instalar, activar y ejecutar Jupyter Notebook en WSL a través de `localhost`:

## Acceso a Jupyter en WSL a Través de `localhost`

Cuando se utiliza WSL (Windows Subsystem for Linux) para ejecutar aplicaciones como Jupyter Notebook, el acceso se simplifica gracias a la dirección `localhost`. A pesar de que WSL tiene su propia dirección IP interna, las solicitudes realizadas a `http://localhost` desde el navegador del sistema operativo host son redirigidas mediante NAT (Network Address Translation) por Windows. Esto permite que los servicios que escuchan en WSL sean accesibles a través de `localhost`, eliminando la necesidad de conocer la dirección IP interna del entorno WSL.
