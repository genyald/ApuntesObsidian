#Shell #Linux

En Linux, podemos hacer uso de un comando muy poderoso para `mapear` unos comandos con otros. Para ello hacemos uso de `alias`.

Por ejemplo, queremos que cada vez que hagamos uso de `ls` realmente agreguemos la sentencia `ls -la` para que nos liste todos los elementos presentes en la carpeta. Para ello  hacemos uso del comando:

```shell
alias ls='ls -la'
```

Ahora, cada que ejecutemos un `ls` nos agregará la sentencia `-la`. Esto nos podría servir inclusive para evitar escribir `python3` y directamente hacer un alias: `alias python3='/usr/bin/python3'` para solamente ejecutar `python`.

## Eliminar un Alias

Podemos eliminar un alias que ya no necesitemos, realmente los alias se almacenan en el documento de texto oculto en `/home/g3n0s/.bashrc` (depende de que terminal tengamos).

```bash
unalias ls
```

Con esto eliminamos el alias anterior, aunque si estamos usando WSL, como es nuestro caso, lo mejor es editar el archivo `~/.bashrc` y al final agregar:

```
# Personal Aliases
alias ls='ls -la'
alias python='/usr/bin/python3/'
alias cat='/usr/bin/cat'
```
\
Cuando hayamos finalizado de editar el documento, hacemos uso de `source ~/.bashrc` para que se efectúen los cambios, ahora cuando escribamos `alias` para enlistarlos, apareceran los que hemos declarado.

> [!example] Uso de `~`
> Cuando usamos `~` en una terminal basada en UNIX como lo es Shell, nos estamos refiriendo a la ubicacion de home, esto es un atajo para no escribir `/home/g3n0s`, por lo que si escribimos `~/Desktop`, nos estamos refiriendo explícitamente a la ubicación en `/home/g3n0s/Desktop`.


