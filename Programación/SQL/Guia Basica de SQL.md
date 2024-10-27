#SQL #InstruccionesBasicas

SQL (Structured Query Language) es un lenguaje estándar para gestionar y manipular bases de datos relacionales. Esta guía cubre los conceptos fundamentales y proporciona ejemplos prácticos para cada tipo de consulta.

## Introducción a SQL
SQL se utiliza para realizar varias operaciones en bases de datos como crear, leer, actualizar y eliminar datos (CRUD: Create, Read, Update, Delete).

## Creación de Tablas

### CREATE TABLE
Para crear una nueva tabla, utilizamos el comando `CREATE TABLE`. Aquí tienes un ejemplo básico:

```sql
CREATE TABLE empleados (
    id INT PRIMARY KEY,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    edad INT,
    salario DECIMAL(10, 2)
);
```

Este comando crea una tabla llamada `empleados` con cinco columnas: `id`, `nombre`, `apellido`, `edad` y `salario`. La columna `id` es la clave primaria.

## Inserción de Datos

### INSERT INTO
Para insertar datos en una tabla, usamos `INSERT INTO`:

```sql
INSERT INTO empleados (id, nombre, apellido, edad, salario) 
VALUES (1, 'Juan', 'Pérez', 30, 3000.00);
```

Este comando inserta una nueva fila en la tabla `empleados` con los valores especificados.

## Consultar Datos

### SELECT
Para recuperar datos de una tabla, utilizamos `SELECT`:

```sql
SELECT nombre, apellido FROM empleados;
```

Este comando selecciona las columnas `nombre` y `apellido` de la tabla `empleados`.

### SELECT con condiciones
Podemos agregar condiciones para filtrar los resultados usando `WHERE`:

```sql
SELECT nombre, apellido 
FROM empleados 
WHERE edad > 25;
```

Este comando selecciona las columnas `nombre` y `apellido` de la tabla `empleados` donde la edad es mayor que 25.

### SELECT con ordenación
Para ordenar los resultados, usamos `ORDER BY`:

```sql
SELECT nombre, apellido 
FROM empleados 
ORDER BY apellido ASC;
```

Este comando ordena los resultados por la columna `apellido` en orden ascendente.

### SELECT con agregación
Podemos utilizar funciones agregadas como `COUNT`, `SUM`, `AVG`, `MAX`, `MIN`:

```sql
SELECT COUNT(*) AS total_empleados 
FROM empleados;
```

Este comando cuenta el número total de filas en la tabla `empleados`.

```sql
SELECT AVG(salario) AS salario_promedio 
FROM empleados;
```

Este comando calcula el salario promedio de todos los empleados.

### SELECT con agrupación
Para agrupar los resultados, utilizamos `GROUP BY`:

```sql
SELECT edad, COUNT(*) AS total 
FROM empleados 
GROUP BY edad;
```

Este comando agrupa los resultados por la columna `edad` y cuenta el número de empleados en cada grupo.

### SELECT con condiciones de agrupación
Podemos filtrar los grupos con `HAVING`:

```sql
SELECT edad, COUNT(*) AS total 
FROM empleados 
GROUP BY edad 
HAVING COUNT(*) > 1;
```

Este comando muestra solo los grupos donde el número de empleados es mayor que 1.

## Actualización de Datos

### UPDATE
Para actualizar datos en una tabla, usamos `UPDATE`:

```sql
UPDATE empleados 
SET salario = 3500.00 
WHERE id = 1;
```

Este comando actualiza el salario del empleado con `id` 1 a 3500.00.

## Eliminación de Datos

### DELETE
Para eliminar datos de una tabla, utilizamos `DELETE`:

```sql
DELETE FROM empleados 
WHERE id = 1;
```

Este comando elimina la fila de la tabla `empleados` donde `id` es 1.

## Operaciones Avanzadas

### JOIN
Para combinar filas de dos o más tablas, usamos `JOIN`. Existen varios tipos de joins:

#### INNER JOIN
Retorna filas cuando hay una coincidencia en ambas tablas.

```sql
SELECT empleados.nombre, departamentos.nombre 
FROM empleados 
INNER JOIN departamentos 
ON empleados.departamento_id = departamentos.id;
```

Este comando selecciona los nombres de empleados y departamentos donde hay una coincidencia en `departamento_id`.

#### LEFT JOIN
Retorna todas las filas de la tabla de la izquierda y las filas coincidentes de la tabla de la derecha.

```sql
SELECT empleados.nombre, departamentos.nombre 
FROM empleados 
LEFT JOIN departamentos 
ON empleados.departamento_id = departamentos.id;
```

Este comando selecciona todos los nombres de empleados y los nombres de departamentos donde haya coincidencia o no.

#### RIGHT JOIN
Retorna todas las filas de la tabla de la derecha y las filas coincidentes de la tabla de la izquierda.

```sql
SELECT empleados.nombre, departamentos.nombre 
FROM empleados 
RIGHT JOIN departamentos 
ON empleados.departamento_id = departamentos.id;
```

Este comando selecciona todos los nombres de departamentos y los nombres de empleados donde haya coincidencia o no.

### SUBQUERIES
Una subquery es una consulta dentro de otra consulta.

#### Subquery en SELECT
```sql
SELECT nombre, (SELECT AVG(salario) FROM empleados) AS salario_promedio 
FROM empleados;
```

Este comando selecciona los nombres de empleados y el salario promedio de todos los empleados.

#### Subquery en WHERE
```sql
SELECT nombre 
FROM empleados 
WHERE salario > (SELECT AVG(salario) FROM empleados);
```

Este comando selecciona los nombres de empleados cuyo salario es mayor que el salario promedio de todos los empleados.

### UNION
Combina los resultados de dos o más consultas `SELECT`.

```sql
SELECT nombre FROM empleados 
UNION 
SELECT nombre FROM clientes;
```

Este comando combina los nombres de empleados y clientes en un solo resultado.

## Funciones y Operadores

### Funciones Matemáticas
```sql
SELECT ABS(-5);    -- Retorna 5
SELECT CEIL(4.2);  -- Retorna 5
SELECT FLOOR(4.7); -- Retorna 4
SELECT ROUND(4.567, 2); -- Retorna 4.57
```

Estas funciones realizan operaciones matemáticas básicas.

### Funciones de Cadena
```sql
SELECT LENGTH('Hola');        -- Retorna 4
SELECT LOWER('HOLA');         -- Retorna 'hola'
SELECT UPPER('hola');         -- Retorna 'HOLA'
SELECT SUBSTRING('Hola Mundo', 1, 4); -- Retorna 'Hola'
SELECT CONCAT('Hola', ' ', 'Mundo');  -- Retorna 'Hola Mundo'
```

Estas funciones manipulan cadenas de texto.

### Operadores Lógicos
```sql
SELECT nombre 
FROM empleados 
WHERE edad > 30 AND salario < 4000;

SELECT nombre 
FROM empleados 
WHERE edad < 25 OR salario > 5000;

SELECT nombre 
FROM empleados 
WHERE NOT (edad > 40);
```

Estos operadores se utilizan para combinar condiciones en consultas.

## Creación y Uso de Índices

### CREATE INDEX
Para mejorar el rendimiento de las consultas, podemos crear índices:

```sql
CREATE INDEX idx_nombre 
ON empleados (nombre);
```

Este comando crea un índice en la columna `nombre` de la tabla `empleados`.

## Seguridad y Gestión de Usuarios

### Creación de Usuario
```sql
CREATE USER 'nuevo_usuario'@'localhost' IDENTIFIED BY 'contraseña';
```

Este comando crea un nuevo usuario con una contraseña.

### Asignación de Privilegios
```sql
GRANT SELECT, INSERT, UPDATE, DELETE ON base_de_datos.* TO 'nuevo_usuario'@'localhost';
```

Este comando otorga privilegios al usuario para realizar operaciones en una base de datos específica.

### Revocación de Privilegios
```sql
REVOKE INSERT ON base_de_datos.* FROM 'nuevo_usuario'@'localhost';
```

Este comando revoca el privilegio de inserción del usuario en una base de datos específica.

### Eliminación de Usuario
```sql
DROP USER 'nuevo_usuario'@'localhost';
```

Este comando elimina un usuario de la base de datos.

### Ejecución de Consultas SQL desde un Archivo
Podemos ejecutar un archivo `.sql` que contenga múltiples comandos SQL:

```sql
SOURCE path/to/file.sql;
```

Este comando ejecuta todos los comandos SQL contenidos en el archivo especificado.

## Buenas Prácticas

- **Normalización**: Organiza los datos para reducir la redundancia.
- **Usar índices sabiamente**: Los índices mejoran el rendimiento de las consultas pero pueden ralentizar las operaciones de inserción y actualización.
- **Respaldo Regular**: Realiza copias de seguridad de tus bases de datos regularmente para prevenir la pérdida de datos.
- **Validación de Datos**: Siempre valida los datos antes de insertarlos en la base de datos para evitar inconsistencias.