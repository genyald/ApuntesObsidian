#Python #Ejercicio 

El ejercico consta del siguiente diagrama UML:

![[catalogo_peliculas.png]]

El codigo final de test_catalogo_peliculas es el siguiente (Correr en VSCode):

```python
from dominio.Pelicula import Pelicula
from servicio.CatalogoPeliculas import CatalogoPeliculas
import time

chose = None
while chose != 4:
    try:
        print(' Prgrama catalogo de peliculas '.center(50, '-'))
        print('''
    Seleccione una opcion:
    1) Agregar Pelicula
    2) Listar Peliculas
    3) Eliminar catalogo completo
    4) Salir
            ''')
        chose = int(input('Opcion elegida [1, 2, 3, 4]: '))
        if chose == 1:
            varpelicula = str(input('Dame el nombre de tu pelicula a agregar: '))
            peli = Pelicula(varpelicula)
            CatalogoPeliculas.agregar_pelicula(peli)
            print(f'{peli} - agregada correctamente...')
        elif chose == 2:
            try:
                print('\n')
                print('Listado de Peliculas '.center(50, '*'))
                print('\n' +  CatalogoPeliculas.listar_peliculas())
            except FileNotFoundError:
                print(''.center(50, '-'))
                print('El archivo aun no existe, prueba agregando una pelicula al catalogo')
        elif chose == 3:
            CatalogoPeliculas.eliminar()
            print('Catalogo eliminado correctamente...')
    except ValueError:
        print(''.center(50, '-'))
        print(f'Error, opcion no valida, elige un valor valido...')
        time.sleep(1.5)
else:
    print(''.center(50, '-'))
    print('Saliendo del programa... Adios')
```

