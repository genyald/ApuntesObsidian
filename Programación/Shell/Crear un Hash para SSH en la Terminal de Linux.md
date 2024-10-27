#Linux #Shell 

En Linux, puedes generar claves SSH para la autenticación segura sin contraseña en servidores remotos. Aquí están los pasos y algunos detalles importantes de los comandos.

## **Generar una Clave SSH (hash)**
El comando para crear una nueva clave SSH es `ssh-keygen`. Este comando generará un par de claves, una pública y una privada, que puedes usar para autenticarte en servidores.

**Comando básico**:
```bash
ssh-keygen -t rsa -b 4096 -C "tu_email@example.com"
```

- **`-t rsa`**: Especifica el tipo de clave. En este caso, usamos RSA, que es uno de los algoritmos más comunes.
- **`-b 4096`**: Define el tamaño de la clave. Cuanto mayor sea el número, más segura será la clave. Un valor de 4096 es estándar para mayor seguridad.
- **`-C "tu_email@example.com"`**: Añade un comentario a la clave (normalmente tu correo electrónico) para que puedas identificarla más fácilmente.

> [!success]- Detalles Adicionales del Comando `ssh-keygen`
> - **`-f <ruta>`**: Especifica la ruta del archivo para guardar las claves. Ejemplo:
 > ```bash
>  ssh-keygen -t rsa -b 4096 -C "tu_email@example.com" -f >~/.ssh/mi_clave_personal
>  ```
>- **`-q`**: Ejecuta el comando en modo silencioso (sin salida a la consola).
>- **`-N <frase>`**: Especifica una frase de paso no interactiva (útil para scripts).  Ejemplo:
	>  ```bash
	>  ssh-keygen -t rsa -b 4096 -C "tu_email@example.com" -N "mi_frase_de_paso"
	  >```




## **Ruta de Guardado de la Clave**

Después de ejecutar el comando, te preguntará dónde deseas guardar el archivo de la clave:

```
Enter file in which to save the key (/home/usuario/.ssh/id_rsa):
```

Puedes presionar **Enter** para aceptar la ruta predeterminada (`/home/usuario/.ssh/id_rsa`) o especificar una diferente.

## **Frase de Paso**
Luego te pedirá una **frase de paso** opcional para mayor seguridad. Si no deseas usar una frase, simplemente presiona **Enter**.

```bash
Enter passphrase (empty for no passphrase):
Enter same passphrase again:
```

## **Visualizar la Clave Pública**
Una vez generadas las claves, la pública estará disponible en el archivo `~/.ssh/id_rsa.pub`. Puedes ver su contenido usando:

```bash
cat ~/.ssh/id_rsa.pub
```

## **Copiar la Clave al Servidor**
Para copiar la clave pública a un servidor remoto, usa el siguiente comando:

```bash
ssh-copy-id usuario@servidor
```

Este comando añadirá la clave pública al archivo `~/.ssh/authorized_keys` en el servidor remoto, lo que te permitirá conectarte sin contraseña.

---

> [!Warning] Nota
> La clave privada no debe ser compartida, mientras que la clave pública es la que distribuirás para autenticarte en otros servidores.

---

# Agregar una Clave Privada SSH al Agente SSH

El **agente SSH** es una herramienta que te permite gestionar tus claves SSH privadas, facilitando el proceso de autenticación con servidores sin tener que ingresar repetidamente la frase de paso (passphrase). Una vez que agregas tu clave privada al agente, este se encargará de autenticarte automáticamente cada vez que te conectes a un servidor.

## Pasos para Agregar una Clave Privada al Agente SSH

### 1. **Iniciar el Agente SSH**

Para empezar, es necesario asegurarse de que el **agente SSH** esté corriendo. Esto se logra mediante el siguiente comando:

```bash
eval "$(ssh-agent -s)"
```

#### ¿Qué hace este comando?

- **`ssh-agent -s`**: Lanza el agente SSH y devuelve las variables de entorno necesarias (`SSH_AUTH_SOCK` y `SSH_AGENT_PID`) en un formato de script para el shell.
  
  - **`SSH_AUTH_SOCK`**: Es la ruta del socket Unix que se usa para comunicarse con el agente SSH.
  - **`SSH_AGENT_PID`**: Es el ID de proceso del agente SSH en ejecución.

- **`eval`**: Evalúa la salida de `ssh-agent -s`, configurando las variables de entorno para que el shell pueda interactuar con el agente sin problemas.

#### Ejemplo de salida:
```bash
Agent pid 12345
```

Esto indica que el agente está corriendo y ha sido correctamente inicializado.

---

### 2. **Agregar la Clave Privada al Agente**

Una vez que el agente está activo, es momento de agregar **tu clave privada**. Si la clave que deseas agregar está en la ruta predeterminada (`~/.ssh/id_rsa`), puedes usar el siguiente comando:

```bash
ssh-add ~/.ssh/id_rsa
```

- **Si la clave está en otra ubicación**: Reemplaza la ruta por la de tu archivo de clave.
- **Si la clave tiene una frase de paso (passphrase)**: Se te pedirá que la ingreses al ejecutar este comando.

#### Nota:
La clave privada que agregues debe tener permisos restrictivos, es decir, debe ser legible únicamente por el propietario. Puedes asegurarte de que los permisos son correctos ejecutando:

```bash
chmod 600 ~/.ssh/id_rsa
```

---

### 3. **Verificar las Claves Agregadas**

Para confirmar que la clave privada se ha añadido correctamente al agente, puedes usar el siguiente comando:

```bash
ssh-add -l
```

Esto listará todas las claves que actualmente están cargadas en el agente. Si ves la clave correcta, ¡ya está todo listo para usar!

#### Ejemplo de salida:
```bash
4096 SHA256:xxxxxx /home/usuario/.ssh/id_rsa (RSA)
```

---

## **Eliminar Claves del Agente (Opcional)**

Si deseas eliminar una clave del agente SSH, usa:

```bash
ssh-add -d ~/.ssh/id_rsa
```

Para eliminar **todas** las claves del agente SSH:

```bash
ssh-add -D
```

---

## Cargar la Clave Automáticamente al Iniciar Sesión

Si no quieres agregar la clave manualmente cada vez que inicias sesión, puedes configurar tu shell para que lo haga de manera automática.

1. **Abrir el archivo de configuración del shell**:

   - Si usas **Bash**, edita el archivo `~/.bashrc`.
   - Si usas **Zsh**, edita el archivo `~/.zshrc`.

   ```bash
   nano ~/.bashrc
   ```

2. **Agregar el comando `ssh-add`** al final del archivo:

   ```bash
   eval "$(ssh-agent -s)" > /dev/null
   ssh-add ~/.ssh/id_rsa
   ```

   Esto iniciará el agente SSH y añadirá tu clave privada cada vez que abras una nueva terminal.

3. **Aplicar los cambios** ejecutando:

   ```bash
   source ~/.bashrc
   ```

---

> [!INFO] Notas Finales
> - **Seguridad**: Es recomendable usar una frase de paso (passphrase) para proteger tu clave privada, especialmente si trabajas en entornos compartidos.
>- **Optimización**: Al cargar automáticamente la clave en el agente SSH al iniciar sesión, puedes agilizar el proceso de conexión a servidores remotos.


---