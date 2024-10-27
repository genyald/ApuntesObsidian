#PowerShell #Windows
## ¿Qué es Chocolatey?

Chocolatey es una herramienta de gestión de paquetes para Windows que simplifica la instalación, actualización y desinstalación de software. Te permite instalar software de forma rápida y sencilla desde la línea de comandos, similar a cómo funcionan los gestores de paquetes en sistemas operativos basados en Unix, como APT en Ubuntu o Homebrew en macOS. ^QueEs

## Uso básico de Chocolatey

> **Instalación de paquetes**: 
```bash
choco install googlechrome
```

> **Actualización de paquetes**:

```bash
choco upgrade googlechrome
```
> **Desinstalación de paquetes**::
```bash
choco uninstall googlechrome
```
> **Buscar paquetes**: 
```bash
choco search firefox
```

> **Listar todos los paquetes**: 
```bash
choco list
```
## Opciones avanzadas

- **Instalación en ubicación personalizada**: Puedes especificar la ubicación de instalación de un paquete utilizando el parámetro `-ia`, `--params`, `-installArguments`, o directamente en el comando de instalación. Por ejemplo:
```bash
choco install <nombre_del_paquete> --params "'/InstallLocation=C:\Programas'
```

## Apéndice

- **Creación de paquetes**: Si necesitas distribuir tu propio software a través de Chocolatey, puedes crear tu propio paquete Chocolatey. Puedes encontrar información detallada sobre cómo hacerlo en la documentación oficial de Chocolatey.

- **Configuración avanzada**: Puedes personalizar la configuración de Chocolatey editando el archivo `chocolatey.config`. Este archivo te permite configurar opciones como los directorios de cache, los directorios de instalación y otros parámetros avanzados.

>[!info]- Notas adicionales
>- Asegúrate de ejecutar Chocolatey desde una línea de comandos con permisos de administrador para evitar problemas de permisos durante la instalación y actualización de paquetes.
>
>- Revisa la documentación oficial de Chocolatey para obtener información detallada sobre su uso y características avanzadas.