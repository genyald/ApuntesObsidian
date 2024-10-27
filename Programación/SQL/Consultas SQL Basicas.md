#SQL 

Cuando estamos usando SQL , lo recomendable es que utilicemos las palabras reservadas con mayusculas, columnas y tablas en minuscula. Esto es para facilitar la lectura de estas mismas.

```sql
SELECT * FROM persona
```


> [!example] Punto y coma
> Si haras mas de una instruccion, cada una debe llevar punto y coma


En este caso selecccionamos todo de la tabla persona, nos devolvera todo el contenido en la tabla. Podemos agregar un filtro `where`, esl cual significa `DONDE`.

```sql
SELECT * FROM persona WHERE id_persona=3
```

## Seleccionar varios registros:
```sql
SELECT * FROM persona WHERE id_persona IN (1,2)
```

## Insertar informacion en sentencia SQL:

```sql
INSERT INTO persona(nombre, apellido, email) VALUES('Juan', 'Mendez', 'jmendez@mail.com') 
```

## Actualizar el valor de celdas en una tabla:

```sql
UPDATE persona SET nombre = 'Jorge', email = 'jfernandez@mail.com' WHERE id_persona=4;
```

## Borrar contenido en la tabla:

```sql
DELETE FROM persona WHERE id_persona=3
```


> [!warning] `DELETE FROM base_de_datos`
> Si no se agrega el `WHERE` estaremos borrando TODA la base de datos, se debe tener extremo cuidado

POR LO TANTO, LAS SENTENCIAS BASICAS SON:

- `SELECT` - Seleccionar registros
- `INSERT` - Agregar registros
- `UPDATE` - Actualizar registros
- `DETELE` - Eliminar registros