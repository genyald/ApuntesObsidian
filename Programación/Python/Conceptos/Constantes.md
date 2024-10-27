#Python #Constantes

Todos los datos en python son dinamicos, eso significa que como tal no existe el concepto de constante. Es una convencion a la que se llega, en la cual, si una variable esta escrita completamente con mayusculas y los espacios por `_`, significa que no se debe modificar esta. Esto aplica tanto para variables como para atributos:

```python
MI_CONSTANTE = 'Valor de una constante'

class Math:
	PI = 3.1416

print(MI_CONSTANTE)
print(Math.PI)
```