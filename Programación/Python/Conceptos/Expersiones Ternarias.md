#Python #Ternarios

Las expresiones ternarias en Python permiten evaluar una condición y devolver un valor basado en esa condición en una sola línea de código. Son una forma compacta de escribir una declaración `if-else`.

>La sintaxis básica de una expresión ternaria es:

```python
hacer if condición else por_contrario
```
## Ejemplos Básicos

```python
x = 10
mensaje = "x es mayor que 5" if x > 5 else "x no es mayor que 5"
print(mensaje)
```

En este ejemplo, si `x` es mayor que 5, la variable `mensaje` contendrá "x es mayor que 5". De lo contrario, contendrá "x no es mayor que 5".

- Comprobar Paridad
```python
numero = 4
resultado = "par" if numero % 2 == 0 else "impar"
print(f"El número {numero} es {resultado}.")
```


En este ejemplo, `resultado` será "par" si `numero` es divisible por 2, de lo contrario será "impar".
## Ejemplos con Variables Tipo Secuencia

- Verificar Contenido en una Cadena
```python
cadena = "Hola"
mensaje = "Contiene H" if "H" in cadena else "No contiene H"
print(mensaje)
```

- Comprobar Elemento en una Lista
```python
lista = [1, 2, 3, 4, 5]
existe = "Está en la lista" if 3 in lista else "No está en la lista"
print(existe)
```

## Uso de Expresiones Ternarias con Funciones

Puedes usar expresiones ternarias dentro de funciones para hacer tu código más compacto.

- Función para Clasificar Edad
```python
def clasificar_edad(edad):
    return "Niño" if edad < 12 else "Adolescente" if edad < 18 else "Adulto"

edad = 16
print(f"La persona es un {clasificar_edad(edad)}.")
```

### Anidamiento de Expresiones Ternarias

Puedes anidar expresiones ternarias, pero esto puede hacer que tu código sea más difícil de leer.
- Clasificación de Edad con Expresiones Ternarias Anidadas
```python
edad = 20
clasificacion = "Niño" if edad < 12 else "Adolescente" if edad < 18 else "Adulto" if edad < 60 else "Adulto mayor"
print(f"La clasificación de edad es: {clasificacion}.")
```

### Ejemplos en Contextos Reales

- Asignación Basada en Entrada de Usuario
```python
usuario = input("Introduce tu nombre de usuario: ")
estado = "Acceso concedido" if usuario == "admin" else "Acceso denegado"
print(estado)
```
- Selección de Descuento
```python
precio = 120
descuento = 0.20 if precio > 100 else 0.10
precio_final = precio - (precio * descuento)
print(f"El precio final con descuento es: {precio_final}.")
```