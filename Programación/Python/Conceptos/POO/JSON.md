#JSON #Python 

JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero y fácil de leer/escribir tanto para humanos como para máquinas. Aunque está basado en la sintaxis de objetos de JavaScript, es independiente del lenguaje de programación y se usa ampliamente para la transmisión de datos entre servidores y aplicaciones web.

#### Características de JSON
- **Formato de Texto:** JSON es un formato basado en texto, lo que significa que los datos se almacenan como texto legible. Esto facilita su lectura y depuración.
  
- **Independencia del Lenguaje:** JSON puede ser usado por múltiples lenguajes de programación como Python, JavaScript, Java, C++, entre otros.

- **Ligero:** JSON es menos verboso que XML, lo que lo hace más ligero y eficiente para transmitir datos.

- **Estructura de Datos Simple:** JSON es capaz de representar estructuras de datos como objetos, listas, strings, números, booleanos, y null.

- **Interoperabilidad:** JSON es ampliamente soportado y utilizado en APIs web, lo que permite una fácil integración entre sistemas diferentes.

## Estructura de JSON

- **Objetos:**
  Un objeto en JSON se representa con llaves `{}`. Contiene pares clave-valor, donde la clave es un string y el valor puede ser un número, string, booleano, null, otro objeto o un array.

  **Ejemplo:**
  ```json
  {
      "nombre": "Juan",
      "edad": 25,
      "casado": false
  }
  ```

- **Arrays:**
  Un array en JSON se representa con corchetes `[]` y puede contener múltiples valores, los cuales pueden ser de cualquier tipo compatible con JSON.

  **Ejemplo:**
  ```json
  {
      "colores": ["rojo", "verde", "azul"]
  }
  ```

- **Valores:**
  Los valores en JSON pueden ser de los siguientes tipos:
  - **String:** Cualquier secuencia de caracteres entre comillas dobles `"`.
  - **Número:** Enteros o flotantes.
  - **Booleanos:** `true` o `false`.
  - **Null:** Un valor nulo.
  - **Objeto:** Un par clave-valor.
  - **Array:** Una lista ordenada de valores.

  **Ejemplo de valores:**
  ```json
  {
      "nombre": "Maria",
      "edad": 30,
      "altura": 1.65,
      "esEstudiante": false,
      "direccion": null
  }
  ```

## Cómo Usar JSON

- **Parseo de JSON:**
  Convertir un string en formato JSON a un objeto que pueda ser manipulado en un lenguaje de programación.
  
  **Ejemplo en Python:**
  ```python
  import json

  json_data = '{"nombre": "Juan", "edad": 25}'
  data = json.loads(json_data)
  print(data["nombre"])  # Salida: Juan
  ```

- **Serialización a JSON:**
  Convertir un objeto de un lenguaje de programación a un string en formato JSON.

  **Ejemplo en Python:**
  ```python
  import json

  data = {
      "nombre": "Maria",
      "edad": 30
  }
  json_data = json.dumps(data)
  print(json_data)  # Salida: {"nombre": "Maria", "edad": 30}
  ```

## Ventajas y Desventajas de JSON

- **Ventajas:**
  - Sencillo y fácil de entender.
  - Ligero y eficiente.
  - Amplio soporte en APIs y aplicaciones web.
  - Excelente para la interoperabilidad entre diferentes lenguajes de programación.

- **Desventajas:**
  - No soporta comentarios, lo que puede dificultar la documentación en archivos JSON.
  - No maneja tipos de datos complejos, como fechas o funciones.
  
## JSON vs. Otros Formatos

- **JSON vs. XML:**
  - JSON es más ligero y fácil de leer que XML.
  - XML soporta más características avanzadas, como esquemas y espacios de nombres.

- **JSON vs. YAML:**
  - JSON es más estructurado y menos propenso a errores de sintaxis.
  - YAML es más legible para los humanos y soporta comentarios.

## Ejemplo de uso de JSON Online

Para este ejemplo haremos uso del link: [personas.json](http://globalmentoring.com.mx/api/personas.json). El metodo para consultar la informacion de un link es con el ejercicio [[Leer Contenido Online]].

```python
from urllib.request import Request, urlopen
import json

url = 'http://globalmentoring.com.mx/api/personas.json'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}

request = Request(url, headers=headers)

with urlopen(request) as raw_text:
	# Procesamos el cuerpo de la respuesta, decodificamos:
	cuerpo_respuesta = raw_text.read().decode('utf8')
	# Convertimos a json
	json_respuesta = json.loads(cuerpo_respuesta)
	print(json_respuesta)
```

A partir de aqui, ahora podemos hacer uso de los objetos declarados en el json, los cuales se convierten en diccionarios con listas (con mas diccionarios con listas)  (en python), esto tiene una enorme ventaja:

```python
# Accediendo a la lista pesonas
for persona in json_respuesta['personas']:
	print('Persona:', persona['nombre'], 'Edad:', persona['edad'] )
```

Ahora, si quisieramos acceder a las variables de un orden superior como `'total'` o `'mensaje'`:

```python
print('Total de respuestas:', json_respuesta['total'])
print(json_respuesta['mensaje'])
```