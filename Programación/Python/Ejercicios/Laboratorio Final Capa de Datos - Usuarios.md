#Python #Ejercicio #DataBases #PostgreSQL 


> [!SUMMARY] La actividad consiste en usar `DAO` y `CRUD` para crear una capa de datos, el diagrama UML es el siguiente:

![[01-laboratorio_usuarios.png]]

El codigo final es el siguiente:

>Consultar/Ejecutar en VSCode: `C:\VSCProyects\laboratorio_usuarios`

```python
from UsuarioDAO import *

class MenuApp:
    @classmethod
    def Menu(cls):
        seleccion = None
        while seleccion != 5:
            print(' Laboratorio Usuarios '.center(50, '-'))
            print('Elija una de las siguientes opciones:\n\t1)Listar Usuarios\n\t2)Agregar Usuario\n\t3)Actualizar Usuario\n\t4)Eliminar Usuario\n\t5)Salir')
            seleccion = int(input('Opcion elegida: '))
            print('')
            if seleccion == 1:
                usuarios = UserDAO.select()
                for usuario in usuarios:
                    print(usuario)
            elif seleccion == 2:
                user = str(input('Inserta el usuario y la contraseña para el nuevo registro: ')).replace(' ', '').split(',')
                print('')
                user = User(user=user[0], password=user[1])
                UserDAO.insert(user)
                print(f'Usuario: {user} | insertado correctamente.\n')
            elif seleccion == 3:
                update = str(input('Ingresa el nombre y la contraseña, seguido del id a actualizar: ')).replace(' ', '').split(',')
                print('')
                update = User(user=update[0], password=update[1], user_id=update[2])
                UserDAO.update(update)
                print(f'Usuario: {update} actualizado correctamente.\n')
            elif seleccion == 4:
                user = input('Dame el id de usuario a eliminar (para cancelar, ingresa \'C\'): ')
                print('')
                if user == 'C':
                    print('Operacion cancelada')
                    continue
                else:
                    user = int(user)
                user = User(user_id=user)
                UserDAO.delete(user)
                print(f'Usuario: {user} eliminado.\n')
        else:
            print('Programa terminado.')
            
MenuApp.Menu()
```

## Documentación

Primero importamos `pool` de la biblioteca `psycopg2`, despues mandamos a llamarlo con:

```python
cls.pool = pool.SimpleConectionPool(
conexiones_minimas, conexiones_maximas, host, ususario, contraseña, puerto, database
)
```

Posteriormente llamamos a `conn1 = cls.pool.getconn()` para solicitarle una conexion al pool y asignarla a `conn1`.

En el otro archivo (`CursorPool`) hacemos los metodos para el `Context Manager`, de esta manera usando [with](app://obsidian.md/Manejo%20de%20Contexto%20%60with%60) hacemos que al empezar se inicie el método que nos devuelve un cursor:

```python
cursor = conn1.cursor()
```

Finalmente cuando salimos del with se cierra el cursor (`cursor.close())` y la conexion se va a un metodo que libera el cursor con:

```python
conn1.putconn()
```

Ademas en el `with` comprobamos al salir si hubo un error presente en el codigo, si hay una excpecion se hace el `conn1.rollback()` y si fue exitosa la ejecucion se realiza un `conn1.commit()`. Esto se conecta a un programa principal que usa `DAO` y `CRUD`.