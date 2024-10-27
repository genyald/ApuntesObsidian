#Python #Ejercicio
```python
# Ejerecicio: Crear una clase llamada cubo con sus respectivos atributos (alto, ancho y profundidad)

class Cubo:     # Creamos una clase llamada cubo, la cual asigna los valores de alto, ancho y profundidad a la misma clase
    def __init__(self, alto, ancho, profundidad):
        self.alto = alto
        self.ancho = ancho
        self.profundidad = profundidad 

    def volumen(self):      # Creamos un metodo de clase que calcula el volumen
        return self.ancho * self.alto * self.profundidad

print('# Ejerecicio: Crear una clase llamada cubo con sus respectivos atributos (alto, ancho y profundidad)')   
reinicio = 'S'  # Hacemos que por defecto el valor de reinicio sea 'S' para que se ejecute el while al menos una vez
cubo = []       # Una lista que contendra los apuntadores a los objetos creados

while reinicio == 'S' or reinicio == '':    # Volvemos a ejecutar el while si se le dio respuesta positiva al reinicio
    alto = int(input('Dame el valor del alto de tu cubo: '))
    ancho = int(input('Dame el valor del ancho de tu cubo: '))
    profundidad = int(input('Dame el valor de la profundidad de tu cubo: '))
    cubo.append(Cubo(alto, ancho, profundidad))     # A la lista cubo, le agregamos un objeto creado con la clase Cubo, con los atributos escaneados
    # print(cubo)
    reinicio = input('Desea agregar otro objeto Cubo?: [S/n]: ').upper()    # Escaneamos si deseamos agregar un nuebo objeto cubo, el resultado lo volvemos mayusculas y lo almacenamos en al variable reinicio
else:
    for cubAct in range(len(cubo)):     # Cuando acaba el while, leemos el tama;o de cubo, eso lo convertimos en un rango con ese valor, por lo que cubAct tendra el valor de la iteraccion actual que estamos ejecutando
        print(f'El valor del volumen del cubo {cubAct+1} es igual a {cubo[cubAct].volumen()}')  # Imprimimos el valor de la iteraccion mas uno y el valor del resultado del metodo volumen en el objeto almacenado en la iteraccion actual con el valor de nuestra lista
```