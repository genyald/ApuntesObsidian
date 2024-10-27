#Python #Ejercicio 

Desarollar un programa en python que calcule estas dos funciones controlado por el usuario:

$$F = (C \times{1.8})+32$$
$$C = \frac{F - 32}{1.8}$$


```python
def CToF(temp):
	return (temp * 1.8) + 32

def FToC(temp):
	return (temp - 32)/1.8

print('Programa para convertir de fahrenheit a celcius y viceversa')
procedimiento = str(input('Que desea hacer?: C -> F [CF] o F -> C [FC]: ')).upper()
if procedimiento == 'CF':
	temp = float(input('Dame el valor en Celcius que convertire a Fahrenheit: '))
	tempTrans = CToF(temp)
	print(f'{temp} grados Celcius equivale a {tempTrans:.2f} grados Farenheit')   # Imprime solo dos digitos flotantes
elif procedimiento == 'FC':
	temp = float(input('Dame el valor en Fahrenheit que convertire a Celcius: '))   # Imprime solo dos digitos flotantes
	tempTrans = FToC(temp)
	print(f'{temp} grados Farenheit equivale a {tempTrans:.2f} grados Celcius')
else:
	print('Valor no valido')
```