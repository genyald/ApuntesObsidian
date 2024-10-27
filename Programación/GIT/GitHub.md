#GIT #GitHub 

Github es un sistema de gestión de proyectos basado en git y la nube, cuenta con el mismo principio del uso de git con la ventaja de poder trabajar simultáneamente con otros colaboradores.

- Tenemos nuestro repositorio en la nube, o repositorio remoto, para descargarlo hacemos lo que se conoce como `git clone <url>`. Este se clona completo, con todas las ramas y demás.
- Cuando el proyecto esta en local, lo trackeamos y continuamos con su desarrollo en la rama que nos corresponde.
- Cuando terminemos de trabajar y queramos enviar nuestro progreso a producción, hacemos un `git push`. Esto se hace con las versiones que desarrollamos en local.

Pero la verdadera pregunta es, ¿Cómo funciona el hecho de que varias personas puedan subir su parte y los progresos de todos siguen funcionando? Bueno, eso es gracias a `git pull`. 

- `Git Pull` actualiza nuestro repositorio local fusionando los cambios efectuados durante nuestro desarrollo local por parte de los colaboradores, su funcionamiento es el siguiente:

		- Hacemos un Fetch (Traemos la actualizacion de la nube)
		- Fusionamos nuestra ultima version local con un merge

![[git_push_fetch.png]]

Entonces, `git pull` hace un `git fetch` y un `git merge` a nuestro repositorio local.

## Primeros Pasos

Para comenzar, debemos crear un proyecto, un proyecto es un conjunto de repositorios. Estos proyectos pueden estar dentro de una `organización`. También tenemos `gist`, el cual es un pedazo pequeño de código que podemos compartir.  

Para crear cualquier cosa de este tipo, hacemos click en el icono superior derecho `'+'`. 

- Al crear un repositorio:
	- Git-ignore es un archivo que enlista los archivos que serán ignorados completamente por git, se usa normalmente para agregar imágenes, archivos para las pruebas, etc.
	- README es un markdown que se abre automáticamente al abrir el repositorio en GitHub.

Esto lo podemos omitir a primera instancia para poder subir directamente nuestro repositorio local y de esta forma evitar conflictos a primera instancia.

## Enviar y Traer Repositorio Local a GitHub

Podemos enviar el trabajo completo que tengamos de algún proyecto completo a GitHub, para ello debemos seguir los siguientes pasos:

- Primero, nuestro trabajo o repositorio local debe tener por lo menos un commit y no debe tener archivos sin guardar.
- Debemos convertir `master` a `main` oficialmente, para ello usamos la sentencia:

```bash
git branch -M main
```

- Creamos el `origen` remoto, el cual es la direccion `https` de nuestro repositorio, lo agregamos con el comando:

```bash
git remote add origin https://github.com/genyald/TestGit.git
```

Este comando hace que remotamente, creemos un origen, el cual proviene de la url. Ahora, con el comando `git remote -v` podemos conocer mas detalles de la url que asignamos como origen remoto.

- Podemos verificar si esta agregado correctamente al `fetch` y al `pull` con el comando:

```bash
git remote -v
```

> [!question] Quitar Algo del Origen Remoto
> Para eliminar algo del origen remoto, podemos consultar los comandos remotos con `git remote -h`, para eliminar el origen basta con insertar `git remote remove origin`.

- Ahora, enviamos al repositorio remoto con:

```bash
git push -u origin main
```

La razón por la que agregamos `-u` es el parámetro abreviado `--set-upstream`. La opción `--set-upstream` en git push vincula tu rama local a la rama remota correspondiente. Esto significa que, en el futuro, puede usar solo `git pull` o `git push` sin especificar la rama, por lo que estarán sincronizadas, en caso de no usarlo, debemos hacer `git pull origin main` para traer los cambios de origen a main. Estamos trayendo al origen (el repositorio no local) el contenido de `main`, que es nuestra rama principal.

> [!warning] Si Ya Existian Archivos Previos
> Para el caso en el que ya existan archivos en el repositorio, como `README.md`, primero debemos hacer un `git pull --alow-unrelated-histories` (que es un `fetch` y un `merge`) (`--alow-unrelated-histories` para poder traer los archivos que no tienen un historial de un commit), para traer el contenido del repositorio y unirlo, por lo que habrá que solucionar conflictos si por ejemplo, ya fue creado de manera diferente este `README.md`. Una vez realizado esto, ya podemos hacer nuestro `git push`.

### Mediante SSH

Para poder hacer uso de `secure shell`, debemos contar con una llave publica `ssh`. 

![[Breve Explicacion de Llaves Publicas y Privadas (Cifrado Asimétrico)#^acf48a]]

SSH es superior en cuanto al nivel de seguridad. En HTTPS, un usuario que use nuestro ordenador podría acceder a git en nuestra terminal y malograr nuestros proyectos o  hacer password cracking, por ello `ssh` es una opción mas viable si necesitamos alta seguridad.

![[Crear un Hash para SSH en la Terminal de Linux#**Generar una clave SSH (hash)**]]

Una vez bien configurado el cliente ssh con la llave privada y dada de alta la llave publica dentro de la pagina de github, ahora debemos cambiar el origen:

```bash
git remote set-url origin git@github.com:genyald/TestGit.git
```

Esto cambiara nuestra forma de manejar github a ssh automaticamente, podemos comprobarlo con:

```bash
git remote -v
```

Cuando esto este configurado, ahora podemos hacer `git push`, `git pull`, etc.


> [!Warning] SIEMPRE: Antes de Hacer `push`
> Es importante hacer un `pull` antes de un `push`, en dado caso que hayan conflictos al hacer el pull, debemos hacer un `fetch` y un `merge` manualmente. Aunque también podemos hacer un `pull --rebase` para hacer lineal la solución de conflictos uno por commit, para hacer lineal los cambios.


## TAGS

Los tags son eso, etiquetas que se usan normalmente para etiquetar la versión de nuestro código, esto es sumamente útil en GitHub, debido a que con un click podemos descargar una versión especifica de nuestro repositorio. Para agregar un tag, necesitamos saber el hash del commit a etiquetar:

```shell
git tag -a v1.0 -m 'Primera version' <hash>
```

Visualizarlas en git es complicado, necesitamos ejecutar la sentencia:

```shell
git tag
```

Sin embargo, esto solamente nos enlistará las referencias de los tags a los commit's, no nos dará a que hash de commit esta unido este tag, por lo que no es muy útil. Para saber en cual hash esta presente el tag, usamos:

```shell
git show-ref --tags
```

Sin embargo, en GitHub se usa normalmente para agregar las versiones o relases, de esta manera es mas fácil saber que versión de código representa cada commit. 

#### **Eliminar un TAG**:

> [!example] TAG PARA BORRAR
> Click en `Run`:
>```bash
git tag -a v11.1 -m 'Un tag inservible para borrar'
>```

Para eliminar un tag, podemos hacerlo desde GitHub o __desde la terminal__, con el comando:

```bash
git tag -d v11.1
```

Para subir los cambios de un `tag` eliminado, podemos hacer uso de estos dos comandos:

```bash
git push origin -d v11.1
```

O especificando aplicar un cambio especifico por carpeta:

```bash
git push origin :refs/tags/v11.1
```
### Subir Etiqueta

- Primeramente agregamos las etiquetas a nuestro repositorio:
```bash
git tag -a v1.0 -m 'Primera version' 5e38af4
```
- Después hacemos un `pull origin main`, para evitar conflictos al subir los tags:
```bash
git push origin --tags
```
Si tenemos configurado el `--set-up-stream` basta solamente con hacer un `git push --tags`.

## Subir Repositorio con Ramas Secundarias

Cuando hacemos normalmente un `push origin main`, solamente estamos trabajando o subiendo la rama principal que es main, por lo que para GitHub no existe en este caso, la rama appBar, entonces, para subir el repositorio con las ramas secundarias y demás debemos posicionarnos en la rama secundaria y hacer un push a origen de appBar:

```bash
git checkout appBar
git push -u origin appBar 
```

El `-u` es para poder hacer un `push` solamente con estar en appBar sin necesidad de decir de donde a donde hara el push, esto es muy util, solo con el checkout nos ponemos en la rama donde deseamos subir los cambios.

Sin embargo, si se debe subir rama por rama, para ello debemos de usar el push para llevar la rama al origen, que en este caso es remoto. A continuacion, un ejemplo en el que creamos una rama secundaria, hacemos commit y la subimos al repositorio:

```bash
git branch Despedida
git checkout Despedida
echo 'Nos vemos' > adios.txt
git add adios.txt
git git commit -m 'Mensaje de despedida'
git push -u origin Despedida
```

Con esto creamos la rama Despedida, nos desplazamos a esta, hacemos el archivo de texto de despedida, lo agregamos al `stage`, hacemos un commit y finalmente subimos la rama principal al repositorio y usamos el upstream para eficientizar futuros push o pull's.

## Colaboradores en GitHub

En nuestro repositorio de GitHub podemos agregar colaboradores desde los ajuste de el mismo. Tenemos que enviarle una invitación para colaborar al usuario y este debe de aceptarla. Una vez hecho esto, el colaborador puede hacer push y pull's libremente, inclusive si el repositorio es privado.

Es importante destacar que el otro usuario debe tener configuradas sus credenciales `https` o `ssh`.

Cuando un colaborador hace su pull, hace que nuestro repositorio local no este actualizado, por ello hacemos un pull (fetch y merge) antes de hacer otro push.

## Pull Request

En un entorno de desarrollo real, tenemos la rama `main`, la cual es una rama de producción, esta rama es la etapa final de desarrollo, es la mas importante.

Para ejercer un cambio a main, no hacemos nunca directamente un `push`, hacemos uso de los `pull request`, estos consisten en hacer una solicitud para unir a la rama de trabajo nuestros cambios. 

En un entorno real, estos `pull request` no se envían hacia nuestra rama `main`, se usa una rama alterna que es una copia idéntica, esta funciona como un entorno de prueba para encontrar errores antes de enviar a `main`. Para enviar los cambios de la rama de pruebas o `develop` también se usan `pull request`, estos cambios son encargados a un DevOps, que se especializa en corregir código y aprobar los cambios.

El flujo de trabajo descrito se puede apreciar asi:

![[workflow_github.png]]

Entonces, realmente la rama `develop` va a funcionar como `main` a menos a nivel programador local.

### Hacer un Pull Request

Un `pull request` es solicitar que se 'jalen' los cambios de la rama que desarrollamos a la linea principal, osea, hacemos un `request` a `main` para que haga un `pull`. En GitLab es conocido como `merge request`.

Ahora, imaginemos que en nuestra aplicación surge un bug importante, bueno, para solucionarlo haremos una rama secundaria llamada `BugTexto`:

```shell
git branch BugTexto
git checkout BugTexto
```

Posteriormente comenzamos a solucionar el bug, tal vez después de unos cuantos commit's lo consigamos. Cuando deseamos enviar esta solucion a la rama principal, hacemos un `pull request`. 

Entonces, básicamente desarrollamos en una rama secundaria creada y el `pull request` es la solicitud de que `main` una los cambios a si misma. 

Para hacer un `pull request` necesitamos hacerlo mediante GitHub. En la seccion de `Pull Request` elegimos las dos ramas a combinar, los usuarios que van a revisar (`reviewers`) y aprobar los cambios, asi como asignarle `tags`, `issues`, `proyectos` (agrupación de proyectos) y `milestone` o objetivos.

El `reviewer` va a aprobar los cambios, agregar comentarios o sugerir algunas modificaciones. Cuando lo hayamos hecho hacemos un push a nuestra rama como lo haríamos normalmente, a el `reviewer` le aparecen estos commit's, finalmente comentamos al respecto para que sea notificado y finalmente apruebe el `pull request`. Finalmente hay una persona encargada de hacer los merge's a los `pull request` aprobados.

Una vez que los cambios fueron unidos, podemos usar la opción de `delete branch` que esta en la seccion de nuestro `pull request`, para cerrar esta rama que por ejemplo, fue para un bug especifico de la aplicación; También puede ser restaurada posteriormente.

> [!Warning] No se usa Mege en GitHub
> Eso significa que en repositorios nunca se usa merge, solamente para proyectos locales, el merge en github se maneja mediante `pull request's`.


## Colaborando en Proyectos Open Source

Un proyecto publico es considerado un proyecto de codigo abierto, a pesar de tal vez contar con su propia tecnologia privada de parte del desarollador, cualquier persona puede colaborar para solucionar un error o aportar una mejora. Aunque tambien podemos colaborar haciendo reportes de issues.

Para colaborar en un proyecto con nuestros propios pull request se siguen los siguientes pasos:

- Hacer un `fork` del proyectos al que queremos colaborar, esto nos creara una copia idéntica del proyecto pero hacia nuestros repositorios.
- Implementar nuestros commit's, tal vez hacer una rama secundaria para nuestros aportes.
- Cuando este avanzado nuestro proyecto, GitHub nos avisara que tenemos `n` commit's mas que en el repositorio original y nos permitirá hacer `pull request` al repositorio original, esto debe de pasar por todos los `reviewers` presentes en el proyectos.

> [!question] Actualizar un `Fork`
> Los forks no se acutalizan de manera automatica, por lo que debemos agregar al `git remote` nuestro repositorio original:
> ```bash
>git remote add (nombre) (link del repo a agregar)
>```
>Ahora, para actualizar el local y hacer el push a nuestro `fork` actualizado:
>```bash
>git pull (nombre) main
>git push origin main
>```
>(Acaban de agregar la opción de actualizar el `fork` desde GitHub) 

## Issues

Los `Issues` son reportes de mal funcionamiento o comportamiento inusual en nuestro código. Se puede controlar el `issue` para que no puedan seguir comentando al respecto, cerrarlo o marcarlo como corregido, inclusive comentarlos.

Para marcar nuestro `issue` como corregido, hacemos un commit de la correcion, en la descripcion o mensaje de nuestro comit acostumbran usar las palabras:

- `fixes`
- `resolves`
- `closes`
- `Fix Bug`

Seguido de `#` y el numero de `issue` presente en GitHub, por ejemplo, el issue `Agregar error de creador #4` se soluciona:

```bash
git commit -am 'Se agrega nombre de creador | Fixes #4'
```

Cuando hagamos un `push` de los cambios, el `issue` se cerrará automáticamente, dando por hecho que ese commit soluciona este error.

> [!tip] Asociar Comentarios a Issues
> Podemos citar otros `issues` abiertos o cerrados con el uso de `#`. Por ejemplo, si alguien abre un `issue` repetido que ya se soluciono, podemos cerrarlo (o no) con un comentario citando la solución: `This issue has fixed on #5`.
### Labels en Issues

Podemos hacer uso de `labels` en la sección de `issues` para poder seccionar el área correspondiente de el `issue` informado, por ejemplo el `label`: `bug`. Al momento de abrir un `issue` le agregamos esta etiqueta para una fácil sección y administración por parte de los desarrolladores; esto es una muy buena practica dentro de GitHub.

También podemos crear nuestra propia `label` en la sección de `labels` de los `issues`, inclusive asignarle su propio color en hexadecimal.

Cuando creamos un `issue`, en la sección de `labels`, agregamos a las que corresponde nuestro `issue`. Cuando buscamos `issues` podemos filtrarlos por labels, siendo esto muy útil.

## Milestone

Los `milestones` son objetivos, funcionan agrupando `issues` y tienen una fecha objetivo. Entonces conforme se van cerrando la barra de progreso aumenta, hasta que llegue al 100%, es una buena herramienta para fijar objetivos y seccionar los `issues` a parte de las etiquetas. También nos marca cuantos dias vamos de atraso conforme esos objetivos.

Para crearlos, solo basta con ir a la sección `issues` y después a `milestone`, de ahí abrimos uno, fijamos nombre, descripción, fecha objetivo y los `issues` que va a contener este. Una vez completado, se puede cerrar y si lo eliminamos, es definitivo (eliminarlo no cierra los `issues` que contiene).
## Uso de **.gitignore**

Es un archivo que indica a Git qué archivos o directorios ignorar para evitar que sean rastreados o incluidos en el repositorio.

- Líneas vacías o con `#` son ignoradas (comentarios).
- Se pueden usar patrones para ignorar archivos/directorios.

### Ejemplos
- Ignorar archivos específicos:  
  ```bash
  archivo.log
  ```
- Ignorar por extensión:  
  ```bash
  *.log
  ```
- Ignorar un directorio:  
  ```bash
  /directorio/
  ```
- Excluir de ser ignorado (negación `!`):  
  ```bash
  !importante.txt
  ```

### Ubicación
1. **Proyecto**: En la raíz o subdirectorios.
2. **Global**: Usar `git config --global core.excludesfile ~/.gitignore_global`.

#### Ejemplos comunes
- Ignorar compilaciones:  
  ```bash
  /build/
  *.exe
  ```
- Ignorar entornos virtuales:  
  ```bash
  /venv/
  ```


## README.md

Es un archivo de texto en formato `Markdown` que proporciona una descripción del proyecto. Es lo primero que los colaboradores o usuarios ven al acceder a un repositorio.

>Acostumbra seguir este orden dentro de los repositorios:
### Estructura básica

1. **Título del Proyecto**:  
   ```markdown
   # Nombre del Proyecto
   ```

2. **Descripción**:  
   Breve introducción al proyecto, sus objetivos y funcionalidades.

3. **Instalación**:  
   Instrucciones para instalar el proyecto o configurarlo en el sistema local.
   ```bash
   git clone https://github.com/usuario/proyecto.git
   ```

4. **Uso**:  
   Ejemplos o comandos para ejecutar el proyecto:
   ```bash
   python app.py
   ```

5. **Contribución**:  
   Guías sobre cómo contribuir al proyecto (pull requests, issues).

6. **Licencia**:  
   Tipo de licencia del proyecto (MIT, GPL, etc.).
   ```markdown
   ## Licencia
   Este proyecto está bajo la licencia MIT.
   ```

7. **Autor(es)**:  
   Información sobre los creadores del proyecto y sus contactos.


## GitHub Pages

GitHub Pages es un servicio gratuito que permite alojar sitios web estáticos directamente desde un repositorio de GitHub. Ideal para portafolios, blogs o documentación de proyectos.

1. **Repositorios soportados**:
   - Puedes desplegar GitHub Pages desde la rama principal (`main/master`) o una carpeta específica como `docs/`.

2. **Creación del sitio**:
   - Ve a la configuración del repositorio.
   - En "GitHub Pages", selecciona la rama o carpeta de donde deseas servir el sitio.
   - GitHub generará una URL para acceder a tu sitio (ejemplo: `https://usuario.github.io/repo`).

3. **Personalización**:
   - Puedes crear tu sitio usando HTML, CSS, JavaScript, o usar generadores estáticos como **Jekyll**, que es compatible de manera nativa.
   - Usa un archivo `index.html` o `README.md` como página principal.

4. **Temas**:
   - GitHub Pages ofrece temas prediseñados que se pueden aplicar fácilmente a tu sitio con Jekyll, permitiendo un diseño profesional sin mucho esfuerzo.

### Pasos para Configurarlo
1. Crea un repositorio público llamado `usuario.github.io`.
2. Añade tu contenido HTML, Markdown o utiliza Jekyll.
3. Activa GitHub Pages en la pestaña "Settings" → "Pages".
4. Accede a tu sitio en `https://usuario.github.io`.

### Usos Comunes:
- **Portafolios personales**.
- **Documentación de proyectos**.
- **Blogs** utilizando **Jekyll** o frameworks estáticos similares.

### Ejemplo Rápido de Uso
```bash
git clone https://github.com/usuario/usuario.github.io
cd usuario.github.io
echo "Hello World" > index.html
git add .
git commit -m "Initial commit"
git push
```

## Wikis en GitHub

En nuestro repostiorio, existe la seccion de Wikis, esta sirve para documentar nuestro codigo, hacer una guia de su uso y demas. Podemos crearla solo agregando un home y escribiendo en markdown todo el contenido, aunque tambien es compatible con otros lenguajes, este es el mas eficiente de escribir.

Podemos agregar referencias con el logo de :LiLink: presente en el texto, basta solamente con escribir el nombre del la pagina de la wiki que queremos referenciar e inclusive el link, funciona igual que el markdown de [[Formatos en Obsidian|Obsidian]].

## GitHub Proyects

**GitHub Projects** es una herramienta de gestión de proyectos que permite organizar y planificar el trabajo dentro de un repositorio o para múltiples repositorios. Utiliza tableros estilo *kanban* donde puedes crear y gestionar tareas (llamadas *issues* o *pull requests*) mediante tarjetas que se mueven a través de diferentes columnas, según su estado.

### ¿Cuándo usar GitHub Projects?

Utiliza **GitHub Projects** cuando necesitas:
- **Organizar y priorizar tareas**: Visualizar el progreso de tu proyecto.
- **Asignar tareas a miembros del equipo**: Definir responsables para cada tarea.
- **Colaborar con otros desarrolladores**: Facilitar la coordinación entre los equipos.

Es útil para proyectos de desarrollo, pero también se puede aplicar a cualquier otro tipo de trabajo colaborativo.

### Componentes de GitHub Projects

#### - **Tableros (Projects)**
Son el espacio donde se organiza todo el trabajo. Puedes tener varios proyectos activos al mismo tiempo para gestionar distintos flujos de trabajo o funcionalidades dentro de un mismo repositorio.

#### - **Columnas**
Las columnas representan las diferentes fases o estados del trabajo. Por ejemplo:
- **To Do (Por hacer)**: Tareas pendientes.
- **In Progress (En progreso)**: Tareas en desarrollo.
- **Done (Hecho)**: Tareas finalizadas.

Puedes personalizar estas columnas para que se adapten a tu flujo de trabajo.

#### - **Tarjetas (Cards)**
Cada tarjeta en un tablero representa una tarea. Estas tarjetas pueden ser:
- **Issues**: Problemas, mejoras o solicitudes dentro del proyecto.
- **Pull Requests**: Solicitudes de cambios o aportaciones al código.
- **Notas (Notes)**: Recordatorios o tareas que no están directamente vinculadas a un issue o pull request.

#### - **Etiquetas (Labels)**
Permiten clasificar las tareas según su tipo o prioridad. Por ejemplo, puedes usar etiquetas como `bug`, `enhancement`, `urgent`, etc. Esto ayuda a organizar mejor el trabajo.

#### - **Milestones (Hitos)**
Son grandes objetivos o metas dentro del proyecto. Los milestones agrupan tareas relacionadas para un lanzamiento o una fase importante del proyecto.
### Automatizaciones y Vistas

#### - **Automatizaciones**
Puedes automatizar algunas acciones, como mover tarjetas de una columna a otra cuando se cierre un issue o cuando se apruebe un pull request. Esto reduce el trabajo manual y facilita el seguimiento del progreso.

#### - **Vistas de Proyectos**
Existen diferentes formas de ver tu proyecto:
- **Tableros estilo Kanban**: Para visualizar el flujo de trabajo.
- **Listas**: Para ver todos los elementos de manera ordenada.
- **Calendario**: Para planificar y hacer seguimiento de fechas de entrega o deadlines.

### **Colaboración**

GitHub Projects permite la **colaboración en equipo**:
- **Asignación de tareas**: Puedes asignar tarjetas a diferentes miembros del equipo.
- **Comentarios y discusión**: En cada tarjeta, los desarrolladores pueden dejar comentarios, adjuntar documentos y discutir sobre los avances.
- **Integración con Issues y Pull Requests**: Cada cambio en los issues o pull requests relacionados se refleja automáticamente en las tarjetas, manteniendo todo actualizado.

### **Mejores Prácticas**

- **Definir un flujo de trabajo claro**: Decide desde el inicio cuántas columnas usarás y cuáles serán las reglas para mover tareas entre ellas.
- **Usar etiquetas y milestones**: Ayuda a mantener la organización y claridad.
- **Revisar y actualizar frecuentemente**: Es importante que todo el equipo esté comprometido con la actualización de las tarjetas para reflejar el progreso real.