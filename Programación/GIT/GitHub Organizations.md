#GIT #GitHub #Organization
## ¿Qué es una GitHub Organization?

Una GitHub Organization es una cuenta compartida que permite colaborar en múltiples proyectos, centralizando la gestión de repositorios y permisos de equipo. Está diseñada para grupos de personas que trabajan en conjunto, como empresas, comunidades de código abierto o equipos de desarrollo, proporcionando un control más granular sobre el acceso a repositorios y configuraciones.

## ¿Cuándo usar GitHub Organizations?

Se recomienda usar una GitHub Organization cuando:
- Tienes un equipo o empresa con múltiples colaboradores y proyectos.
- Necesitas una gestión centralizada de permisos y acceso.
- Quieres controlar la propiedad de los repositorios, evitando que dependan de cuentas personales.
- Quieres aplicar políticas y configuraciones compartidas para todos los repositorios y miembros.

## Componentes Clave de GitHub Organizations

### Repositorios (Repositories)
En una organización, los repositorios  pueden ser públicos o privados. Todos los repositorios creados bajo una organización pertenecen a esta, no a un individuo. Esto asegura la continuidad y control del código, incluso si un miembro del equipo deja el grupo.

### Equipos (Teams)
Los __equipos__  son grupos de personas dentro de la organización que pueden compartir acceso a uno o más repositorios. Los equipos permiten gestionar los permisos de acceso de manera más eficiente:
- __Team Owners__ (Propietarios del equipo): Controlan la organización, pueden crear repositorios y gestionar equipos.
- __Team Members__ (Miembros del equipo): Colaboran en los repositorios asignados, según los permisos otorgados.

### Roles y Permisos   
`GitHub Organizations` ofrece varios niveles de control sobre los repositorios:
- __Propietario (Owner)__: Tiene control total sobre la organización. Puede añadir/quitar miembros, crear repositorios y ajustar configuraciones.
- __Administrador (Admin)__: Controla un repositorio específico, puede hacer cambios en su configuración y gestionar issues y pull requests.
- __Mantainer (Responsable)__: Gestiona un equipo en particular, pero no tiene acceso total sobre la organización.
- __Colaborador (Collaborator)__: Puede contribuir a los repositorios con permisos definidos (lectura, escritura o administración).

### Roles de Repositorio   
En los `repositorios`, los permisos pueden ser ajustados para:
- __Read__: Solo permite ver el código y los issues/pull requests.
- __Triage__: Permite categorizar issues y pull requests, pero no realizar cambios en el código.
- __Write__: Permite contribuir al código, enviar cambios y gestionar issues.
- __Maintain__: Gestiona el repositorio, incluyendo configuración y borrado de ramas.
- __Admin__: Control total sobre el repositorio.

### Acceso Basado en Equipos 
Cada equipo puede tener diferentes niveles de acceso a los repositorios. Esto permite gestionar los permisos a gran escala. Por ejemplo, un equipo de desarrolladores puede tener acceso de escritura a los repositorios de código, mientras que un equipo de QA puede tener acceso de solo lectura.

## Gestión de Miembros y Equipos

### Añadir y gestionar miembros
Como propietario o administrador de una organización, puedes añadir miembros a través de sus cuentas de GitHub. Una vez dentro, los miembros pueden ser asignados a diferentes equipos y roles.

### Creación y gestión de equipos
Dentro de una organización, puedes crear equipos para reflejar la estructura de tu grupo (por ejemplo, un equipo de desarrollo, un equipo de diseño, etc.). Estos equipos pueden tener acceso específico a ciertos repositorios.

### Acceso a proyectos y permisos por defecto
Se pueden definir permisos por defecto para los nuevos miembros o repositorios. Esto permite configurar si, por ejemplo, todos los miembros pueden ver y contribuir a los repositorios públicos.

## Colaboración y Herramientas

### Colaboración en Repositorios
Al ser parte de una organización, los miembros pueden colaborar en proyectos a través de *issues*, *pull requests*, *discussions* y revisiones de código. Los equipos pueden mencionarse para revisar o discutir código, facilitando la colaboración en grupos más grandes.

### GitHub Actions
Las `GitHub Actions` permiten automatizar tareas como pruebas, despliegue o cualquier flujo de trabajo. Dentro de una organización, puedes compartir workflows entre repositorios, creando automatizaciones consistentes para todos los proyectos.

### Projects y Milestones
Al igual que en los repositorios individuales, las `GitHub Organizations` pueden usar *Projects* para gestionar tareas y flujos de trabajo. Puedes organizar proyectos que abarcan múltiples repositorios, lo que es útil para grandes desarrollos.

### GitHub Discussions
Una herramienta útil para fomentar la comunicación dentro de la organización. Permite tener debates o preguntas dentro de la organización o de proyectos específicos, separando las discusiones generales de los issues técnicos.

## Seguridad y Políticas

### Autenticación y Autorización

Las organizaciones pueden configurar políticas de seguridad más estrictas:
- Autenticación en dos factores (2FA): Puedes requerir que todos los miembros usen 2FA para mejorar la seguridad.
- SAML Single Sign-On (SSO): Integración con sistemas corporativos de SSO, que permite a los empleados acceder con las credenciales corporativas.

### Permisos a Nivel de Organización  
Puedes establecer políticas globales para controlar cómo los miembros interactúan con los repositorios. Por ejemplo, puedes decidir si los miembros pueden crear repositorios o si deben solicitar aprobación.

### Auditoría y Logs
Las organizaciones pueden acceder a registros detallados (logs de auditoría) sobre las acciones realizadas por los miembros. Esto es útil para mantener un registro de cambios o resolver problemas de seguridad.

## Transferencia y Propiedad de Repositorios

Los repositorios personales pueden ser transferidos a una organización, lo que es útil cuando un proyecto crece y necesita más control administrativo. Esta transferencia asegura que el repositorio ya no dependa de una sola cuenta personal.

## Planificación y Escalabilidad

Las `GitHub Organizations` están diseñadas para escalar. A medida que el equipo crece, puedes añadir más miembros, dividir el trabajo en más equipos y mantener una estructura organizada. Además, puedes integrar herramientas externas como Jira , Slack  o Trello para mejorar la comunicación y gestión del proyecto.

## Costos y Planes de GitHub Organizations

GitHub ofrece planes de pago para organizaciones que requieren funcionalidades avanzadas, como repositorios privados ilimitados, mayor capacidad de almacenamiento, y mejores controles de seguridad. Los planes gratuitos incluyen algunas de estas características, pero pueden tener limitaciones.