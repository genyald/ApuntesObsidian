#Python #Ejercicio 

![[mundo_pc.png]]

```python
from Computadora import Computadora
from Keyboard import Teclado
from Monitor import Monitor
from Raton import Raton

class Orden:
    contadorOrdenes = 0
    def __init__(self, *computadora):
        self._idOrden = Orden.aumentarOrden()
        self._computadoras = list(computadora)
    @classmethod
    def aumentarOrden(cls):
        cls.contadorOrdenes += 1
        return cls.contadorOrdenes
        
    @property
    def computadoras(self):
        return self._computadoras
    @computadoras.setter
    def computadoras(self, setcomputadoras):
        self._computadoras = list(setcomputadoras)
		
    def agregarComputadora(self, addcompu):
        self._computadoras.append(addcompu)
		
    def __str__(self):
        computadoras_str = ''
        for comp in self._computadoras:
            computadoras_str += '    ' + comp.__str__() + '\n'
        return f'\nOrden {self._idOrden}:\n\n{computadoras_str}\n' + ''.center(90, '-')
    
if __name__ == '__main__':
    monitor1 = Monitor('AOC', 24)
    teclado1 = Teclado('USB', 'HyperX')
    raton1 = Raton('HyperX', 'USB')
    monitor2 = Monitor('Asus', 32)
    teclado2 = Teclado('Bluetooth', 'Logitech')
    raton2 = Raton('Logitech', 'Bluetooth')
    computadora2 = Computadora('Asus', monitor2, teclado1, raton2)
    computadora1 = Computadora('HP', monitor2, teclado1, raton1)
    orden1 = Orden(computadora1, computadora2)
    print(orden1)
    orden2 = Orden(computadora2)
    print(orden2)
    orden1.agregarComputadora(computadora2)
    print(orden1)
```


> [!example] Clases Usadas:
>[[Computadora.py]], [[Keyboard.py]], [[Monitor.py]], [[Raton.py]], [[Input.py]]

