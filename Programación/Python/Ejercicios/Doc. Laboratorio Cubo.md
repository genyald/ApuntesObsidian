#Python #Ejercicio 


> [!example] EJERCICIO:
> Crear una clase llamada cubo con sus respectivos atributos (alto, ancho y profundidad)

---
Primero creamos una clase llamada *Cubo*, la cual recibe y asigna los valores de *alto, ancho y profundidad* a la misma clase a la hora creación del objeto.

```python
class Cubo:     
    def __init__(self, alto, ancho, profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad 
```

>[!success]- Clases
>Recuerda que las clases se empiezan con Mayusculas, las funciones y objetos comienzan con minúsculas, finalmente sigue la notación camello.

Posterior creamos un método de clase llamado *volumen*, el cual devuelve la multiplicación de la variable *alto*, *ancho* y *profundidad*.

```python
#... 
    def volumen(self):      # Creamos un metodo de clase que calcula el volumen
        return self.ancho * self.alto * self.profundidad
```

Comenzamos el programa, asignamos '*S*' como valor por defecto para la variable reinicio y creamos una lista vacía llamada *cubo*. 

```python
print('# Ejerecicio: Crear una clase llamada cubo con sus respectivos atributos (alto, ancho y profundidad)')   
reinicio = 'S'  # Hacemos que por defecto el valor de reinicio sea 'S' para que se ejecute el while al menos una vez
cubo = []       # Una lista que contendra los apuntadores a los objetos creados
```

Iniciamos un ciclo while que evalúa la respuesta de preguntar si deseamos agregar otro objeto de la clase llamada cubo. El valor por defecto de reinicio es para que se ejecute por lo menos una vez el ciclo while.

```python
while reinicio == 'S' or reinicio == '':    # Volvemos a ejecutar el while si se le dio respuesta positiva al reinicio
    alto = int(input('Dame el valor del alto de tu cubo: '))
    ancho = int(input('Dame el valor del ancho de tu cubo: '))
    profundidad = int(input('Dame el valor de la profundidad de tu cubo: '))
    cubo.append(Cubo(alto, ancho, profundidad))     # A la lista cubo, le agregamos un objeto creado con la clase Cubo, con los atributos escaneados
    reinicio.upper = input('Desea agregar otro objeto Cubo?: [S/n]: ')
...
```

La linea explicada, ==cubo.append()== **agrega  el contenido del argumento a la lista cubo**, *ese argumento es la creación de un objeto*, por lo que estamos creando un apuntador a un objeto en una lista,  cuando esto se repite únicamente esta creando un objeto, el cual su apuntador es almacenado en la lista, aunque, seria mas eficiente una tulpa ya que no modificamos sus valores.

```python
...
else:
    for cubAct in range(len(cubo)):     # Cuando acaba el while, leemos el tama;o de cubo, eso lo convertimos en un rango con ese valor
        print(f'El valor del volumen del cubo {cubAct+1} es igual a {cubo[cubAct].volumen()}')
```

![[LaboCuboDraw 4.png]]

Cuando termina el ciclo while, iniciamos un ciclo for, la variable  cubAct maneja el numero de iteración actual, por lo que siempre sera un entero, pero, cubo es una lista, tenemos que preguntar con len() el tamaño de la lista y usarlo como un rango para el ciclo.

Finalmente,  imprimimos dentro del ciclo, le sumamos uno a la iteración ya que esta empieza desde la lista 0 y así la recorremos una decima. Cuando mandamos a llamar la lista cubo con el índice de el numero de la iteración actual, con un punto y el método del objeto volumen, estamos diciendo que ejecute el método de ese objeto actual. Lo hará cuantos objetos hayamos creado.

___

>[!quote]- Código Completo
>![[Laboratorio Cubo]]
[](Laboratorio%20Cubo.md)#### Ejercicio: Crear una clase llamada cubo con sus respectivos atributos (alto, ancho y profundidad)

---