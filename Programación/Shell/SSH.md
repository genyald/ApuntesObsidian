
## Contectarse a un Servidor Linux con SSH

Para conectarte a un servidor Linux usando SSH, sigue estos pasos:

1. **Abre una terminal** en tu máquina local.
2. **Usa el comando `ssh`** seguido del nombre de usuario y la dirección IP del servidor al que deseas conectarte.

La sintaxis general es:

```bash
ssh usuario@direccion_ip
```

Por ejemplo, si tu nombre de usuario es `admin` y la dirección IP del servidor es `192.168.1.100`, el comando sería:

```bash
ssh admin@192.168.1.100
```

3. **Ingresa la contraseña** cuando se te solicite.

Si es la primera vez que te conectas a este servidor, es posible que recibas un mensaje de advertencia sobre la autenticidad del host. Escribe `yes` para continuar.

### Ejemplo paso a paso:

1. Abre la terminal.
2. Escribe el comando de conexión:

```bash
ssh admin@192.168.1.100
```

3. Ingresa la contraseña cuando se te solicite.

### Opciones adicionales:

- **Especificar una clave privada**: Si usas una clave privada para autenticarte, puedes especificarla con la opción `-i`:

```bash
ssh -i /ruta/a/tu/clave_privada admin@192.168.1.100
```

- **Cambiar el puerto**: Si el servidor SSH está escuchando en un puerto diferente al predeterminado (22), puedes especificarlo con la opción `-p`:

```bash
ssh -p puerto admin@192.168.1.100
```

Reemplaza `puerto` con el número de puerto correcto.


> [!question] Para Acceder al Servidor de la Alianza UNAM-HUAWEI
>Consultar Kee-Pass, ahi vienen las credenciales

