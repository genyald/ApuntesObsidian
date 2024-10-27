#Python #Ejercicio 


> [!todo] Convertidor de Grados Centrigrados a Fahrenheight
> El ejercico consiste en convertir de grados centigrados a celcius y viceversa con una clase haciendo uso de la sobrecarga de consturctores.

$$F = (C \times{1.8})+32$$
$$C = \frac{F - 32}{1.8}$$

```python
class ConvertTemp:
	MAX_CELCIUS = 100
	MAX_FAHRENHEIT = 213
	
	@classmethod
	def c_f(cls, celcius):
		if celcius > cls.MAX_CELCIUS:
			raise ValueError('Temperatura demasiado alta', celcius)
		else:
			return (celcius * 1.8) + 32
	
	@classmethod
	def f_c(cls, fahrenheiht):
		if fahrenheiht > cls.MAX_FAHRENHEIT:
			raise ValueError('Temperatura demasiado alta', fahrenheiht)
		return (fahrenheiht - 32) / 1.8
	
resultado = ConvertTemp.c_f(15)
print('Valor convertido de C a F: %.2f' % resultado)

resultado2 = ConvertTemp.f_c(70)
print('Valor convertido de F a C: %.2f' % resultado2)
```