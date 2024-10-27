#Python #SQL #DataBases

Un pool de conexiones es un objeto de tipo conexion a nuestra base de datos que esta activo en lo que se le llama el `pool`, en este momento esta creado el objeto y cuando un cliente lo requiera, ejecutara todas las instrucciones a la `BD` para hacer todas las peticiones necesarias, en cuanto se desocupa ahora esta disponible para que otro cliente haga uso de este.

![[pool_conexiones.png]]

Necesitamos crear una clase extra de la clase conexion a la DB, esta conexión se encargara únicamente del pool de conexiones.

>Consultar en VSCode: `\acceso_datos`

```python
from psycopg2 import pool
from sympy import EX
from logger_base import log
import sys

class Conexion:
    __USERNAME = 'postgres'
    __PASSWORD = 'admin'
    __DATABASE = 'test_db'
    __DB_PORT = '5432'
    __HOST = '127.0.0.1'

    # Definimos minimo y maxio de conexines:
    __MIN_CON = 1
    __MAX_CON = 5
    __pool = None
    # Es un proceso pesado, el valor debe ser optimo

    @classmethod
    def getPool(cls):
        if cls.__pool == None:
            try:
                cls.__pool = pool.SimpleConnectionPool(cls.__MIN_CON, cls.__MAX_CON,
                    user = cls.__USERNAME,
                    password = cls.__PASSWORD,
                    host = cls.__HOST,
                    port = cls.__DB_PORT,
                    database = cls.__DATABASE
                    )
                log.debug(f'Creacion del pool Exitosa: {cls.__pool}')
                return cls.__pool
            except Exception as e:
                log.critical(f'Error del tipo: {type(e)}: {e}, el codigo no puede continuar')
                sys.exit()
        else:
            log.debug(f'Conexion del pool ya existe, devuelta: {cls.__pool}')
            return cls.__pool

    @classmethod
    def obtenerConexion(cls):
        conexion = cls.getPool().getconn()
        log.debug(f'Conexion obtenida del pool: {conexion}')
        return conexion

    @classmethod
    def unlockcnn(cls, conexion):
        # Devolvemos al pool la conexion con la DB
        cls.getPool().putconn(conexion)
        log.debug(f'Conexion vuelve al pool en espera: {conexion}')

    @classmethod
    def closeAll(cls):
        cls.getPool().closeall()
        log.debug('Conexiones finalizadas')

if __name__ == '__main__':
    conexion1 = Conexion.obtenerConexion()
    Conexion.unlockcnn(conexion1)
    conexion2 = Conexion.obtenerConexion()
    conexion3 = Conexion.obtenerConexion()
    conexion4 = Conexion.obtenerConexion()
    conexion5 = Conexion.obtenerConexion()
    conexion6 = Conexion.obtenerConexion()


```

# Explicación de Como Usar el Pool de Conexiones

![[Laboratorio Final Capa de Datos - Usuarios#Documentación]]