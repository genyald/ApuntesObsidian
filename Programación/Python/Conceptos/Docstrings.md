#Python #Docstrings

En python podemos crear cadenas de multiples lineas, sin embargo, el uso de comentarios y `'''` tiene una aplicación especifica y es documentar nuestras clases, funciones o demas en nuestros archivos de python.

Para hacer uso de los parametros utilizamos `:param parametro_elegido` seguido de nuestros comentarios a documentar y terminamos con un `:`.

```python
class MiClase:
    '''
    Este es un ejemplo de la documentacion de nuestra clase
    '''
    def __init__(self):
        '''
        Metodo de inicio de nuestra clase
        '''
    def mi_metodo(self, param1, param2):
        '''
        Esta es la documentacion de nuestro metodo
        :param param1 Este es el parametro 1:
        :param param2 Este es el parametro 2:
        :return Este es el valor de retorno:
        '''
 
if __name__ == '__main__':
    help(MiClase())
```

>Debemos respetar las tabulaciones.

Ahora podemos hacer uso de `MiClase` importada e introducirla al metodo `help()`:

```python
help(MiClase)
```

Sin embargo, tambien podemos mandar a llamar el metodo dunder de `__docstring__` para ver el docstring de esa funcion de nuestra clase:

```python
print(MiClase.__doc__)
print(''.center(70,'-'))
print(MiClase.__init__.__doc__)
print(''.center(70,'-'))
print(MiClase.mi_metodo.__doc__)
print(''.center(70,'-'))
print(type(MiClase.mi_metodo))
```

>Recuerda que todo en python es un objeto, por lo que mi metodo pertenece a la clase `function`.