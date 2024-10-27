#Linux #ComandosBásicos

En este apunte, se describen algunos de los comandos esenciales para la navegación, gestión de archivos, y administración de sistemas en Linux. Estos comandos forman la base para interactuar con el sistema operativo desde la terminal.

## Comandos de Teclado

A continuacion, una lista de comandos usados en el prompt de linux que pueden resultar sumamente utiles:

- `ctrl + r` - Sirve para buscar en el historial de comandos ejecutados.
- `ctrl + c` - Cancela la operacion/comando actual ejecutado.
- `ctrl + t` - Introduce un espacio a la izquierda de la ultima tecla presionada.
- 
## Navegación y Gestión de Archivos

###  ls

Lista los archivos y directorios en el directorio actual.

```bash
ls
```

- `ls -l` - Muestra detalles como permisos, propietario y tamaño.
- `ls -a` - Incluye archivos ocultos.
> [!info] **Consejo**: Usa `ls -lh` para mostrar tamaños de archivo en un formato legible para humanos.

###  pwd 

Muestra la ruta del directorio actual.

```bash
pwd
```

###  cd 

Cambia el directorio actual.

```bash
cd /ruta/del/directorio
```

- `cd ..` - Sube un nivel.
- `cd ~` - Va al directorio home del usuario.

###  mkdir 

Crea un nuevo directorio.

```bash
mkdir nombre_del_directorio
```

###  rmdir 

Elimina un directorio vacío.

```bash
rmdir nombre_del_directorio
```

###  touch 

Crea un archivo vacío o actualiza la fecha de modificación de un archivo existente.

```bash
touch nombre_del_archivo
```

###  cp 

Copia archivos o directorios.

```bash
cp origen destino
```

- `cp -r` - Copia recursivamente directorios.

###  mv 

Mueve o renombra archivos o directorios.

```bash
mv origen destino
```

###  rm 

Elimina archivos o directorios.

```bash
rm nombre_del_archivo
```

- `rm -r` - Elimina recursivamente directorios y su contenido.
> [!warning] **Precaución**: Usa `rm -rf` con cuidado, ya que elimina sin pedir confirmación.

###  find 

Busca archivos y directorios.

```bash
find /ruta -name "nombre_del_archivo"
```

## Visualización de Archivos

###  head 

Muestra las primeras líneas de un archivo.

```bash
head nombre_del_archivo
```

- `head -n 10` - Muestra las primeras 10 líneas.

###  tail 

Muestra las últimas líneas de un archivo.

```bash
tail nombre_del_archivo
```

- `tail -f` - Sigue mostrando nuevas líneas añadidas al archivo en tiempo real.

###  cat 

Muestra el contenido de archivos.

```bash
cat nombre_del_archivo
```

###  wc 

Cuenta líneas, palabras y caracteres en archivos.

```bash
wc nombre_del_archivo
```

- `wc -l` - Cuenta solo las líneas.
- `wc -w` - Cuenta solo las palabras.

###  grep 

Busca patrones dentro de archivos.

```bash
grep "patrón" nombre_del_archivo
```

- `grep -r` - Busca recursivamente en directorios.

## Editores de Texto

###  vi  y  vim 

Editores de texto avanzados con modos de comando.

```bash
vi nombre_del_archivo
```

```bash
vim nombre_del_archivo
```

###  nano 

Editor de texto simple y fácil de usar.

```bash
nano nombre_del_archivo
```

## Compresión y Archivos

###  tar 

Crea y extrae archivos tar.

```bash
tar -cvf archivo.tar /ruta/del/directorio
```

- `tar -xvf` - Extrae un archivo tar.

## Gestión de Procesos

###  ps 

Muestra información sobre los procesos actuales.

```bash
ps
```

- `ps aux` - Muestra todos los procesos en detalle.

###  top 

Muestra los procesos en tiempo real.

```bash
top
```

###  htop 

Versión interactiva de `top`, más fácil de usar.

```bash
htop
```

###  vmstat 

Muestra estadísticas de memoria virtual.

```bash
vmstat
```

###  free 

Muestra la cantidad de memoria libre y usada en el sistema.

```bash
free
```

- `-h` para lectura mas humana.

###  lscpu 

Muestra información sobre la CPU.

```bash
lscpu
```

## Información del Sistema

###  df 

Muestra el uso del espacio en disco.

```bash
df
```

- `df -h` - Muestra el uso en un formato legible.

###  du 

Muestra el uso del espacio en disco por archivos y directorios.

```bash
du
```

- `du -h` - Muestra el uso en un formato legible.

###  whoami 

Muestra el nombre del usuario actual.

```bash
whoami
```

###  uname 

Muestra información sobre el sistema.

```bash
uname
```

- `uname -a` - Muestra toda la información disponible.

###  hostname 

Muestra o establece el nombre del host.

```bash
hostname
```

###  passwd 

Cambia la contraseña del usuario.

```bash
passwd
```

## Permisos y Administración

###  chmod 

Cambia los permisos de archivos y directorios.

```bash
chmod 755 nombre_del_archivo
```

###  sudo 

Ejecuta comandos con privilegios de superusuario.

```bash
sudo comando
```

###  history 

Muestra el historial de comandos.

```bash
history
```

###  man 

Muestra el manual de usuario para comandos.

```bash
man comando
```

---