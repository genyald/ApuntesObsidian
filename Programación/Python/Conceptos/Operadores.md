#Python #Operators

>Los operadores en Python son símbolos que se utilizan para realizar operaciones en operandos (valores o variables). Python soporta varios tipos de operadores, que se pueden clasificar en las siguientes categorías:

1. Operadores aritméticos
2. Operadores de comparación
3. Operadores lógicos
4. Operadores de asignación
5. Operadores bit a bit
6. Operadores de membresía
7. Operadores de identidad

## Operadores Aritméticos

Los operadores aritméticos se utilizan para realizar operaciones matemáticas comunes.

| Operador | Nombre             | Ejemplo      |
|----------|--------------------|--------------|
| `+`      | Suma               | `a + b`      |
| `-`      | Resta              | `a - b`      |
| `*`      | Multiplicación     | `a * b`      |
| `/`      | División           | `a / b`      |
| `%`      | Módulo (Resto)     | `a % b`      |
| `**`     | Exponenciación     | `a ** b`     |
| `//`     | División entera    | `a // b`     |

### Ejemplos

```python
a = 10
b = 3

print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333333333333335
print(a % b)   # 1
print(a ** b)  # 1000
print(a // b)  # 3
```
## Operadores de Comparación

Los operadores de comparación se utilizan para comparar dos valores y devuelven un valor booleano (`True` o `False`).

|Operador|Nombre|Ejemplo|
|---|---|---|
|`==`|Igual a|`a == b`|
|`!=`|Distinto de|`a != b`|
|`>`|Mayor que|`a > b`|
|`<`|Menor que|`a < b`|
|`>=`|Mayor o igual que|`a >= b`|
|`<=`|Menor o igual que|`a <= b`|
### Ejemplos
```python
a = 10
b = 3

print(a == b)  # False
print(a != b)  # True
print(a > b)   # True
print(a < b)   # False
print(a >= b)  # True
print(a <= b)  # False
```

## Operadores Lógicos

Los operadores lógicos se utilizan para combinar expresiones booleanas.

|Operador|Nombre|Ejemplo|
|---|---|---|
|`and`|Y lógico|`a and b`|
|`or`|O lógico|`a or b`|
|`not`|Negación|`not a`|
### Ejemplos
```python
a = True
b = False

print(a and b)  # False
print(a or b)   # True
print(not a)    # False
```

## Operadores de Asignación

Los operadores de asignación se utilizan para asignar valores a las variables.

|Operador|Nombre|Ejemplo|
|---|---|---|
|`=`|Asignación|`a = b`|
|`+=`|Suma y asignación|`a += b`|
|`-=`|Resta y asignación|`a -= b`|
|`*=`|Multiplicación y asignación|`a *= b`|
|`/=`|División y asignación|`a /= b`|
|`%=`|Módulo y asignación|`a %= b`|
|`**=`|Exponenciación y asignación|`a **= b`|
|`//=`|División entera y asignación|`a //= b`|
### Ejemplos
```python
a = 10
b = 3

a += b  # a = a + b
print(a)  # 13

a -= b  # a = a - b
print(a)  # 10

a *= b  # a = a * b
print(a)  # 30

a /= b  # a = a / b
print(a)  # 10.0

a %= b  # a = a % b
print(a)  # 1.0

a **= b  # a = a ** b
print(a)  # 1.0

a //= b  # a = a // b
print(a)  # 0.0
```

## Operadores Bit a Bit

Los operadores bit a bit se utilizan para realizar operaciones en el nivel de bits.

| Operador | Nombre                        | Ejemplo  |
| -------- | ----------------------------- | -------- |
| `&`      | And bit a bit                 | `a & b`  |
| \|       | Or bit a bit                  | a  \| b  |
| `^`      | XOR bit a bit                 | `a ^ b`  |
| `~`      | NOT bit a bit                 | `~a`     |
| `<<`     | Desplazamiento a la izquierda | `a << b` |
| `>>`     | Desplazamiento a la derecha   | `a >> b` |
### Ejemplos
```python
a = 10  # 1010 en binario
b = 4   # 0100 en binario

print(a & b)  # 0 (0000 en binario)
print(a | b)  # 14 (1110 en binario)
print(a ^ b)  # 14 (1110 en binario)
print(~a)     # -11 (complemento a 2)
print(a << 1) # 20 (10100 en binario)
print(a >> 1) # 5 (0101 en binario)
```

## Operadores de Membresía

Los operadores de membresía se utilizan para verificar si un valor o variable se encuentra en una secuencia (lista, tupla, cadena, etc.).

|Operador|Nombre|Ejemplo|
|---|---|---|
|`in`|En|`a in b`|
|`not in`|No en|`a not in b`|
### Ejemplos
```python
frutas = ["manzana", "banana", "cereza"]

print("manzana" in frutas)  # True
print("pera" not in frutas)  # True
```

## Operadores de Identidad

Los operadores de identidad se utilizan para comparar si dos variables son el mismo objeto en memoria.

|Operador|Nombre|Ejemplo|
|---|---|---|
|`is`|Es|`a is b`|
|`is not`|No es|`a is not b`|
### Ejemplos
```python
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)    # True
print(a is c)    # False
print(a is not c) # True
```

