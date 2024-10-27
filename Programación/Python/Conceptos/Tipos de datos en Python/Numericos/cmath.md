El modulo `cmath` en python proporciona funciones especificas para operar con numero complejos, es similar a math pero con complejos, como lo dicta su nombre.

```python
import cmath

z = 3 + 7j
```


>Todas las funciones aritméticas con complejos están naturalmente presentes en las funciones estándar de python.
## Parte real y parte imaginaria

Para acceder a la parte real t a la parte imaginaria usamos los atributos `.real` y `.imag`:

```python
z_real = z.real
z_imag = z.imag
print(z_real)
print(z_imag)
```
## Funciones

#### Raiz cuadrada
```python
square = cmath.sqrt(z)
print(square)
```

### Logaritmo natural

```python
log = cmath.log(z)
print(log)
```

### Exponencial

Calcular la exponencial de un numero complejo:

```python
exp = cmath.exp(z)
print(exp)
```

### Trigonométricas e hiperbólicas

```python
# Funciones trigonometricas
seno = cmath.sin(z)
coseno = cmath.cos(z)
tangente = cmath.tan(z)

# Funciones hiperbolicas
seno_hiperbolico = cmath.sinh(z)
coseno_hiperbolico = cmath.cosh(z)
tangente_hiperbolico = cmath.tanh(z)

print(seno_hiperbolico, coseno_hiperbolico, tangente_hiperbolico)
```

## Conversión de Polares y Rectangulares

### Rectangulares a Polares

Se usa `cmath.polar` para convertir de forma rectangular a polar. Devuelve una tupla `(r, phi)` donde `r` es el modulo y `phi` es el angulo en radianes.

```python
modulo, fase = cmath.polar(z)
print(modulo, fase)
```

### Polares a rectangulares

Se usa `cmath.rect` para convetir un numero de su forma polar (modulo y angulo) a su forma rectangular (a + bj).

```python
# Polar: 5 ∟ π/4
z_polar = cmath.rect(5, cmath.pi/4)
print(z_polar)
```

## Fase y Modulo

```python
# Para obtener unicamente la fase:
phase = cmath.phase(z)

# Para obtener unicamente el modulo
module = abs(z)

print(module, phase)
```