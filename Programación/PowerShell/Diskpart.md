
`diskpart` es una herramienta de línea de comandos para gestionar discos, particiones y volúmenes en Windows. Es útil para tareas como formatear discos, crear y eliminar particiones, y cambiar letras de unidad.

Estos son unos de los comandos básicos de diskpart:

- **Abrir `diskpart`:**
   ```bash
   diskpart
   ```

- **Listar discos:**
   Muestra todos los discos conectados.
   ```bash
   list disk
   ```

- **Seleccionar un disco:**
   Selecciona el disco con el que se desea trabajar (ej: disco 0).
   ```bash
   select disk 0
   ```

- **Listar particiones:**
   Muestra todas las particiones del disco seleccionado.
   ```bash
   list partition
   ```

- **Crear partición primaria:**
   Crea una partición primaria en el disco seleccionado.
   ```bash
   create partition primary
   ```

- **Formatear partición (NTFS):**
   Formatea la partición seleccionada con el sistema de archivos NTFS.
   ```bash
   format fs=ntfs quick
   ```

- **Asignar letra de unidad:**
   Asigna una letra de unidad a la partición.
   ```bash
   assign letter=E
   ```

- **Eliminar partición:**
   Borra la partición seleccionada.
   ```bash
   delete partition
   ```