#Python #Logging

El concepto de loggin sirve para poder enviar información sobre los acontecimientos ocurridos en nuestro código, nos ayuda a depurarlo o enviar información especifica dependiendo del comportamiento a un `log` file.

| Nivel      | Cuando se Usa                                                                                                                                                                   |
| :--------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `DEBUG`    | Informacion detallada del comportamiento del código, este se recomienda solo en desarollo ya que puede brindar demasiada información sobre el comportamiento de nuestro codigo. |
| `INFO`     | Informa que algo esta trabajando como deberia de.                                                                                                                               |
| `WARNING`  | Informa sobre un error que puede ocurrir a futuro pero el programa se sigue ejecutando como se espera.                                                                          |
| `ERROR`    | Informa un problema mas serio, alguna función no pudo ser ejecutada.                                                                                                            |
| `CRITICAL` | El problema mas grave, indica que el programa no puede continuar ejecutandose                                                                                                   |


> [!summary] Debug es el principal usado en el desarollo, los demas son de produccion. Por defecto, el logging esta activado de `warning` hacia adelante.

Para poder apreciar su funcionamiento:

```python
import logging as log
```

Tenemos los tres modos a continuacion:

>`DEBUG`

```python
log.basicConfig(level=log.DEBUG)

log.debug('Mensaje a nivel debug')
log.info('Mensaje a nivel de info')
log.warning('Mensaje a nivel de warning')
log.error('Mensaje a nivel de error')
log.critical('Mensaje a nivel critico')
```

>`INFO`

```python
import logging as log

log.basicConfig(level=log.INFO)

log.debug('Mensaje a nivel debug')
log.info('Mensaje a nivel de info')
log.warning('Mensaje a nivel de warning')
log.error('Mensaje a nivel de error')
log.critical('Mensaje a nivel critico')
```

>`CRITICAL`

```python
log.basicConfig(level=log.CRITICAL)

log.debug('Mensaje a nivel debug')
log.info('Mensaje a nivel de info')
log.warning('Mensaje a nivel de warning')
log.error('Mensaje a nivel de error')
log.critical('Mensaje a nivel critico')
```

(Ejecutar en VSCode, aqui no funciona muy bien)
## Configurar un Handler (Manejador)

Podemos agregar un `Handler` para que el log sea una salida al archivo, este usa la funcion `open()` internamente.

```python
import logging as log

log.basicConfig(level = log.DEBUG,
				format = '%(asctime)s: %(levelname)s [%(filename)s: %(lineno)s] %(message)s',
				datefmt = '%I:%M:%S %p',
                # Configuramos los handlers que vamos a utilizar
                handlers = [
                    # Hacemos un archivo como handler
                    log.FileHandler('.\\acceso_datos\\capa_datos.log'),
                    # Hacemos que la consola tambien sea el handler
                    log.StreamHandler()
                ]
                )

if __name__ == '__main__':
    log.debug('Mensaje a nivel debug')
    log.info('Mensaje a nivel de info')
    log.warning('Mensaje a nivel de warning')
    log.error('Mensaje a nivel de error')
    log.critical('Mensaje a nivel critico')
```

| Attribute name  | Format                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------- | ------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| args            | You shouldn’t need to format this yourself. | The tuple of arguments merged into `msg` to produce `message`, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary).                                                                                                                                                                                                                                                                                                                                          |
| asctime         | `%(asctime)s`                               | Human-readable time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time).                                                                                                                                                                                                                                        |
| created         | `%(created)f`                               | Time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") was created (as returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time "time.time")).                                                                                                                                                                                                                                                                               |
| exc_info        | You shouldn’t need to format this yourself. | Exception tuple (à la `sys.exc_info`) or, if no exception has occurred, `None`.                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| filename        | `%(filename)s`                              | Filename portion of `pathname`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| funcName        | `%(funcName)s`                              | Name of function containing the logging call.                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| levelname       | `%(levelname)s`                             | Text logging level for the message (`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`).                                                                                                                                                                                                                                                                                                                                                                                                                  |
| levelno         | `%(levelno)s`                               | Numeric logging level for the message ([`DEBUG`](https://docs.python.org/3/library/logging.html#logging.DEBUG "logging.DEBUG"), [`INFO`](https://docs.python.org/3/library/logging.html#logging.INFO "logging.INFO"), [`WARNING`](https://docs.python.org/3/library/logging.html#logging.WARNING "logging.WARNING"), [`ERROR`](https://docs.python.org/3/library/logging.html#logging.ERROR "logging.ERROR"), [`CRITICAL`](https://docs.python.org/3/library/logging.html#logging.CRITICAL "logging.CRITICAL")). |
| lineno          | `%(lineno)d`                                | Source line number where the logging call was issued (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| message         | `%(message)s`                               | The logged message, computed as `msg % args`. This is set when [`Formatter.format()`](https://docs.python.org/3/library/logging.html#logging.Formatter.format "logging.Formatter.format") is invoked. Usa el mensaje que hemos agregado `log.warning('Hola')`                                                                                                                                                                                                                                                    |
| module          | `%(module)s`                                | Module (name portion of `filename`).                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| msecs           | `%(msecs)d`                                 | Millisecond portion of the time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord "logging.LogRecord") was created.                                                                                                                                                                                                                                                                                                                                                        |
| msg             | You shouldn’t need to format this yourself. | The format string passed in the original logging call. Merged with `args` to produce `message`, or an arbitrary object (see [Using arbitrary objects as messages](https://docs.python.org/3/howto/logging.html#arbitrary-object-messages)).                                                                                                                                                                                                                                                                      |
| name            | `%(name)s`                                  | Name of the logger used to log the call.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| pathname        | `%(pathname)s`                              | Full pathname of the source file where the logging call was issued (if available).                                                                                                                                                                                                                                                                                                                                                                                                                               |
| process         | `%(process)d`                               | Process ID (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| processName     | `%(processName)s`                           | Process name (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| relativeCreated | `%(relativeCreated)d`                       | Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded.                                                                                                                                                                                                                                                                                                                                                                                                         |
| stack_info      | You shouldn’t need to format this yourself. | Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record.                                                                                                                                                                                                                                                                                                             |
| thread          | `%(thread)d`                                | Thread ID (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| threadName      | `%(threadName)s`                            | Thread name (if available).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| taskName        | `%(taskName)s`                              | [`asyncio.Task`](https://docs.python.org/3/library/asyncio-task.html#asyncio.Task "asyncio.Task") name (if available).                                                                                                                                                                                                                                                                                                                                                                                           |