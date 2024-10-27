#Python #Numeros 

En python estan presentes los sistemas numericos:
- Decimal
- Binario
- Hexadecimal
- Octal

Para declarar los tipos de sistemas numericos usamos las siguientes sentencias:

## Decimal

Cuando no agregamos ningun prefijo estamos declarando en automatico que la literal que estamos manejando es del tipo decimal.


> [!quote] Consultar
> ![[Variables#^literalyvariable]]


```python
a = 10
print(a)
```
## Binario

Para declarar un numero de tipo binario debemos usar el prefijo `0b`:

```python
a = 0b1010
print(a)
```

Como se puede observar, cuando mandamos a imprimir ese numero, por defecto a la salida se interpreta en decimal (`1010`).

## Hexadecimal

Para manejar valores en un sistema hexadecimal, hacemos uso de `0x` seguido de el valor en este sistema numerico:

```python
a = 0xA
print(a)
```

## Octal

Para manejar literales que pertenecen al sistema octal, usamos el prefijo `0o` y posteriormente el valor en sistema octal.

```python
a = 0o12
print(a)
```

# Conversión Numérica

En python es muy fácil ejecutar este tipo de conversiones, de manera que podemos hacer uso del constructor de la clase `int('numero', base)`. Debemos manejarlo como `str` porque no pude ejecutar la conversión con una base explicita como sería `23`.

Para convertir un tipo entero, incluyendo la base:

```python
a = int('23', 10)
print(a)
```

Ahora, para imprimir el `23` de base binaria (`0001 0111`) a decimal :

```python
a = int('10111', 2)
print(a)
```

Para imprimir el `23` en base octal (`27`) en decimal:
```python
a = int('27', 8)
print(a)
```

Para el `23` de hexadecimal (`17`) a decimal:

```python
a = int('17', 16)
print(a)
```

>La gran ventaja de este método de clase es que podemos hacer uso de cualquier base numérica, no solo las mas comunes:
>```python
>a = int('23', 13)
>print(a)
>```

## Formateo de Sistemas Numericos

Python permite la conversión y representación de números en diferentes bases numéricas (binaria, octal, hexadecimal) utilizando funciones y formatos específicos:
###  **Binario**:
- Formato: `{:b}`
- Función: `bin()`
- Ejemplo: `bin(42)` devuelve `'0b101010'`
### **Octal**:
- Formato: `{:o}`
- Función: `oct()`
- Ejemplo: `oct(42)` devuelve `'0o52'`
### **Hexadecimal**:
- Formato: `{:x}` para minúsculas, `{:X}` para mayúsculas
- Función: `hex()`
- Ejemplo: `hex(42)` devuelve `'0x2a'`

**Ejemplo de uso en impresión:**

```python
numero = 42
print("Binario: {:b}".format(numero))  # Resultado: 101010
print("Octal: {:o}".format(numero))    # Resultado: 52
print("Hexadecimal: {:x}".format(numero))  # Resultado: 2a

```

**Con F strings:**

```python
numero = 42
print(f"Binario: {numero:b}")  # Resultado: 101010
print(f"Octal: {numero:o}")    # Resultado: 52
print(f"Hexadecimal: {numero:x}")  # Resultado: 2a
print(f"Hexadecimal (mayúsculas): {numero:X}")  # Resultado: 2A
```


> [!success] NOTA:
> - Combinar con alineacion: `f'{numero:0^10x}'`: Centra con ceros a los lados hasta un ancho de 10 caracteres.
> - Las funciones `bin()`, `oct()`, y `hex()` incluyen prefijos (`0b`, `0o`, `0x`) en sus resultados.
>- Las cadenas de formato no incluyen prefijos, lo que es útil para la salida más limpia.
