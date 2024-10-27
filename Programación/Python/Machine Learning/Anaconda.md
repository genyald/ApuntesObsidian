#Anaconda #EntronoVirtual

Anaconda es una plataforma popular que facilita el manejo de entornos virtuales y la instalación de paquetes, especialmente en proyectos de ciencia de datos y machine learning. Te permite trabajar con diferentes versiones de Python y librerías sin que interfieran entre sí. Es como un "organizador" de tus entornos y herramientas, asegurando que cada proyecto tenga su propio espacio aislado.

## Instalación de Anaconda en Linux

### Descarga de Anaconda
Primero, necesitas descargar el instalador de Anaconda desde su sitio oficial. Puedes hacerlo con el comando `wget` directamente desde la terminal. Recuerda que debes usar el enlace correcto según la versión actual:

```bash
wget https://repo.anaconda.com/archive/Anaconda3-2023.09-Linux-x86_64.sh
```

**Nota**: Asegúrate de estar en el directorio donde quieras descargarlo. 
### Instalación
Para iniciar la instalación, debes ejecutar el script que acabas de descargar. Hazlo con el siguiente comando:

```bash
bash Anaconda3-2023.09-Linux-x86_64.sh
```

**Cosas a tener en cuenta**:
- Te pedirá que leas y aceptes los términos de la licencia, así que sigue las instrucciones en pantalla.
- Elige la ubicación por defecto cuando te pida un directorio de instalación, a menos que prefieras otro lugar.
- Acepta que el instalador modifique tu archivo `.bashrc`. Esto permitirá que Anaconda se active automáticamente cuando abras la terminal.

### Activar Anaconda
Al terminar la instalación, necesitas activar los cambios en `.bashrc` para que conda sea reconocido en la terminal:

```bash
source ~/.bashrc
```

Con esto, `conda` debería estar listo. Verifica su versión para confirmar que todo fue bien:
```bash
conda --version
```

---

## Uso de Conda

### Actualizar Conda
Es importante tener `conda` siempre actualizado para evitar problemas con versiones antiguas. Para actualizarlo, usa:

```bash
conda update conda
```

### Crear un entorno
Los entornos son clave en Anaconda. Son espacios aislados donde puedes instalar diferentes versiones de paquetes sin que interfieran con otros proyectos. Para crear un entorno, ejecuta:

(Puedes ejecutar `conda search python` para preguntar por las versiones disponibles).

```bash
conda create --name mi_entorno python=3.10
```

En este ejemplo, creas un entorno llamado `mi_entorno` con Python 3.10. Esto es útil si tienes proyectos que requieren versiones específicas de Python.

### Activar / Desactivar un entorno
Una vez que creas un entorno, debes activarlo para trabajar en él:

```bash
conda activate mi_entorno
```

Cuando termines, puedes desactivar el entorno y volver al entorno base (o salir de cualquier entorno activo):

```bash
conda deactivate
```

### Listar entornos
Para ver todos los entornos que tienes instalados (incluido el base), usa:

```bash
conda env list
```

Esto te será útil si olvidas el nombre de alguno de tus entornos.

---

## Gestión de Paquetes

### Instalar un paquete
Para instalar paquetes dentro de un entorno, usa `conda install` seguido del nombre del paquete:

```bash
conda install numpy
```

Esto instalará `numpy` en tu entorno activo. Recuerda que cada entorno tiene su propio conjunto de paquetes, por lo que si lo instalas en un entorno, no estará disponible en otros.

### Buscar un paquete
Si no estás seguro de si un paquete está disponible, puedes buscarlo:

```bash
conda search numpy
```

### Actualizar un paquete
Es recomendable mantener tus paquetes actualizados. Para actualizar un paquete específico, ejecuta:

```bash
conda update numpy
```

### Eliminar un paquete
Si ya no necesitas un paquete, puedes eliminarlo:

```bash
conda remove numpy
```

---

## Administrar Entornos

### Clonar un entorno
Si tienes un entorno bien configurado y necesitas crear uno idéntico para otro proyecto, puedes clonarlo:

```bash
conda create --name nuevo_entorno --clone mi_entorno
```

Esto crea `nuevo_entorno` con las mismas dependencias y versiones que `mi_entorno`. Útil para replicar configuraciones sin tener que configurar todo desde cero.

### Exportar un entorno
Puedes exportar un entorno a un archivo `YAML` para compartirlo o replicarlo en otro sistema. Hazlo con:

```bash
conda env export > entorno.yml
```

### Importar un entorno
Si tienes un archivo `YAML` que describe un entorno, puedes crear uno nuevo con las mismas características ejecutando:

```bash
conda env create -f entorno.yml
```

### Eliminar un entorno
Cuando ya no necesites un entorno, puedes eliminarlo para liberar espacio:

```bash
conda env remove --name mi_entorno
```

---

## Uso de pip en entornos conda
Aunque `conda` es el gestor de paquetes principal, también puedes usar `pip` dentro de un entorno para instalar paquetes que no estén disponibles en los repositorios de conda:

```bash
pip install nombre_paquete
```

Recuerda siempre usar `pip` *después* de haber instalado los paquetes principales con `conda` para evitar conflictos.

---

## Canales adicionales

### Uso de conda-forge
Si necesitas un paquete que no está en el canal oficial de Anaconda, puedes instalarlo desde `conda-forge` (un canal comunitario con muchos más paquetes):

```bash
conda install -c conda-forge nombre_paquete
```

---

## Configuraciones adicionales

### Evitar activación automática del entorno base
Anaconda activará automáticamente el entorno base cada vez que abras la terminal. Si prefieres que esto no suceda, puedes desactivar esta opción:

```bash
conda config --set auto_activate_base false
```

Con esto, solo se activarán los entornos cuando tú lo indiques explícitamente con `conda activate`.

### Limpiar caché de conda
Conda puede acumular archivos temporales y versiones antiguas de paquetes. Para limpiar el caché y liberar espacio, usa:

```bash
conda clean --all
```

Esto eliminará archivos no necesarios y optimizará el espacio.

## Instalar y Ejecutar Jupyter en WSL

- **Instalar Jupyter Notebook**:
   Asegúrate de que tienes Anaconda o Miniconda instalado en WSL. Luego, puedes instalar Jupyter Notebook ejecutando:

   ```bash
   conda install jupyter
   ```

- **Activar el Entorno**:
   Si creaste un entorno específico para Jupyter, actívalo con:

   ```bash
   conda activate mi_entorno
   ```

- **Iniciar Jupyter Notebook**:
   Para iniciar el servidor de Jupyter Notebook y permitir que escuche en todas las interfaces, utiliza:

   ```bash
   jupyter notebook --ip=0.0.0.0 --no-browser
   ```

   Este comando hace que el servidor esté disponible en `0.0.0.0`, lo que significa que aceptará conexiones de cualquier dirección IP.

- **Acceder Desde el Navegador Host**:
   Abre tu navegador en Windows y dirígete a `http://localhost:8888` (o al puerto que hayas configurado). Esto redirigirá tu solicitud al servidor Jupyter que se ejecuta en WSL.
