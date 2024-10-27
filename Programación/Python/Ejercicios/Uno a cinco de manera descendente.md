>Hacer una fuincion que reciba un numero y lo imprima de manera descendente hasta el ultimo valor.

```python
def imprimir(numero):
	if numero >= 1:
		print(numero)
		imprimir(numero -1)
		
	elif numero < 0:
		print('Error, rango invalido')
		return
# El caso de sero es else vacio, por lo que no hace nada, se acaba la func
numerodado = int(input('Dame el numero que quieres imprimir de manera descendente: '))
imprimir(numerodado)
```