Las variables de clase y los parámetros de clase son dos conceptos diferentes. ==Los parámetros son los valores que le otorgamos a la clase al momento de inicializar una instancia==, en cambio, ==las variables de clase son valores que se comparten entre clases==. Todas las instancias o subclases que hagamos compartirán estos valores ente ellas.

```python
class MiClase:
	variable_clase = 'Valor de variable de clase'
	
	def __init__(self, variable_instancia):
		self.variable_instancia = variable_instancia
```

Como las variables de clase se asocian con una clase en si misma y no en un objeto, podemos acceder a ellas directamente sin haber hecho una instancia. Están declaradas dentro de la misma clase, asi mismo se acceden.

```python
print(MiClase.variable_clase)
```

Para acceder al valor de la variable de instancia:

```python
miObjeto = MiClase('Valor de Instancia')
miObjeto2 = MiClase('Valor de Instancia 2')
print(miObjeto.variable_instancia)
print(miObjeto2.variable_instancia)
```

Acceder a la variable de clase desde nuestro objeto:

```python
print(miObjeto.variable_clase)
print(miObjeto2.variable_clase)
```


> [!summary] Variable de clase al vuelo
> `Al vuelo = En cualquier momento`. Es lo mismo que definir una variable de clase, pero conforme avanzamos en el codigo y no estrictamente al declararla.
> ```python
> MiClase.variable_clase2 = 'Variable de clase 2'
> print(miObjeto.variable_clase2 + ', ' + miObjeto2.variable_clase2)
>```
