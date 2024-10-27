#Vim #ComandosBásicos 
## Global

- `:h[elp] palabra_clave` - abrir ayuda para palabra clave
- `:sav[eas] archivo` - guardar archivo como
- `:clo[se]` - cerrar archivo actual
- `:ter[minal]` - abre una ventana de terminal
- `K` - abrir página del manual (man page) de la palabra bajo el cursor

> [!info] Ejecuta `vimtutor` en una terminal para aprender los primeros comandos de Vim.

## Mover el cursor
- `h` - mover el cursor hacia la izquierda
- `j` - mover el cursor hacia abajo
- `k` - mover el cursor hacia arriba
- `l` - mover el cursor hacia la derecha
- `gj` - mover el cursor hacia abajo (texto multilínea)
- `gk` - mover el cursor hacia arriba (texto multilínea)
- `H` - moverse hacia la parte superior de la pantalla
- `M` - moverse hacia el centro de la pantalla
- `L` - moverse hacia la parte inferior de la pantalla
- `w` - saltar hasta el inicio de la siguiente palabra
- `W` - saltar hasta el inicio de la siguiente palabra (incluso con puntuación)
- `e` - saltar hasta el final de la siguiente palabra
- `E` - saltar hasta el final de la siguiente palabra (incluso con puntuación)
- `b` - regresar al inicio de una palabra
- `B` - regresar al inicio de una palabra (incluso con puntuación)
- `ge` - saltar hacia atrás hasta el final de una palabra
- `gE` - saltar hacia atrás hasta el final de una palabra (las palabras pueden contener puntuación)
- `%` - ir al carácter asociado (pares por defecto: '()', '{}', '[]')
- `0` - saltar al inicio de la línea
- `^` - saltar al primer carácter no-espacio de la línea
- `$` - saltar al final de la línea
- `g_` - saltar al último carácter no-espacio de la línea
- `gg` - saltar a la primera línea del documento
- `G` - saltar a la última línea del documento
- `5gg` o `5G` - saltar a la línea 5
- `gd` - saltar a la declaración local
- `gD` - saltar a la declaración global
- `fx` - saltar a la siguiente ocurrencia del carácter 'x'
- `tx` - saltar a la ocurrencia previa del carácter 'x'
- `Fx` - saltar a la aparición anterior del carácter 'x'
- `Tx` - saltar a después de la aparición anterior del carácter 'x'
- `;` - repetir el movimiento anterior de f, t, F o T
- `,` - repetir el movimiento anterior de f, t, F o T, hacia atrás
- `}` - saltar al párrafo siguiente (o función/bloque, en modo edición)
- `{` - saltar al párrafo previo (o función/bloque, en modo edición)
- `zz` - desplazar el cursor (sin moverlo) hacia el centro de la pantalla
- `zt` - desplazar el cursor (sin moverlo) hacia la parte superior de la pantalla
- `zb` - desplazar el cursor (sin moverlo) hacia la parte inferior de la pantalla
- `Ctrl + e` - mover la pantalla hacia abajo una línea (sin mover el cursor)
- `Ctrl + y` - mover la pantalla una línea hacia arriba (sin mover el cursor)
- `Ctrl + b` - retroceder una pantalla
- `Ctrl + f` - avanzar una pantalla
- `Ctrl + d` - avanzar cursor media pantalla
- `Ctrl + u` - retroceder cursor media pantalla

> [!info] **Tip**: Escribe un número antes del comando de movimiento para repetirlo. Por ejemplo, `4j` mueve el cursor hacia abajo 4 líneas.

## Modo insertar
- `i` - insertar antes del cursor
- `I` - insertar al inicio de la línea
- `a` - insertar después del cursor
- `A` - insertar al final de la línea
- `o` - insertar una nueva línea debajo de la línea actual
- `O` - insertar una nueva línea encima de la línea actual
- `ea` - insertar después de palabra
- `Ctrl + h` - eliminar el carácter antes del cursor durante el modo de inserción
- `Ctrl + w` - eliminar palabra antes del cursor durante el modo de inserción
- `Ctrl + j` - comenzar una nueva línea durante el modo de inserción
- `Ctrl + t` - sangrar (mover a la derecha) línea un ancho de cambio durante el modo de inserción

- `Ctrl + d` - desangrar (mover a la izquierda) línea un ancho de turno durante el modo de inserción
- `Ctrl + n` - insertar (auto completar) la siguiente coincidencia antes del cursor durante el modo de inserción
- `Ctrl + p` - insertar (auto completar) coincidencia anterior antes del cursor durante el modo de inserción
- `Ctrl + rx` - insertar el contenido del registro x
- `Ctrl + ox` - ingresar temporalmente al modo normal para emitir un comando de modo normal x.
- `Esc` or `Ctrl + c` - salir del modo insertar

## Editar
- `r` - reemplazar un carácter
- `R` - reemplazar más de un carácter, hasta que se presione `ESC`
- `J` - juntar siguiente línea con la actual
- `gJ` - juntar siguiente línea con la actual sin espacio entre ellas
- `gwip` - aplicar formato en párrafo
- `g~` - alternar mayúsculas/minúsculas hasta movimiento
- `gu` - cambiar a minúsculas hasta movimiento
- `gU` - cambiar a mayúsculas hasta movimiento
- `cc` - cambiar (reemplazar) toda la línea
- `c$` o `C` - cambiar (reemplazar) hasta el final de la línea
- `ciw` - cambiar (reemplazar) palabra completa
- `cw` o `ce` - cambiar (reemplazar) una palabra
- `s` - eliminar carácter y reemplazar texto
- `S` - eliminar línea y reemplazar texto (igual que `cc`)
- `xp` - transponer dos letras (suprimir y pegar)
- `u` - deshacer
- `U` - deshacer completamente la última línea modificada
- `Ctrl + r` - rehacer
- `.` - repetir el último comando

## Modo visual
- `v` - iniciar modo visual, seleccionar líneas y ejecutar un comando (p. ej. y-yank)
- `V` - iniciar modo visual seleccionando líneas completas
- `o` - moverse al otro extremo de la zona seleccionada
- `Ctrl + v` - iniciar modo visual de bloque
- `O` - moverse a la otra esquina del bloque
- `aw` - seleccionar una palabra
- `ab` - seleccionar un bloque con ()
- `aB` - seleccionar un bloque con {}
- `at` - seleccionar un bloque con etiquetas <>
- `ib` - seleccionar un bloque interno con ()
- `iB` - seleccionar un bloque interno con {}
- `it` - seleccionar un bloque interior con etiquetas <>
- `Esc` o `Ctrl + c` - salir del modo visual

> [!info] **Tip**: En lugar de `b` o `B` también puedes usar `(` o `{` respectivamente.

## Comandos visuales
- `>` - mover texto hacia la derecha
- `<` - mover texto hacia la izquierda
- `y` - copiar texto seleccionado
- `d` - eliminar texto seleccionado
- `~` - alternar minúsculas/mayúsculas
- `u` - cambiar el texto marcado a minúsculas
- `U` - cambiar el texto marcado a mayúsculas
## Registros
- `:reg[isters]` - mostrar el contenido de los registros
- `"xy` - copiar en el registro X
- `"xp` - pegar el contenido del registro X
- `"+y` - copiar en el registro del portapapeles del sistema
- `"+p` - pegar desde el registro del portapapeles del sistema

> [!info] **Tip**: Los registros se guardan en `~/.viminfo` y se cargarán la próxima vez que ejecutes Vim.

> [!info] **Registros especiales**:
- `0` - última copia
- `"` - registro sin nombre, última eliminación o copia
- `%` - nombre de archivo actual
- `#` - nombre de archivo alternativo
- `*` - contenido del portapapeles (X11 primario)
- `+` - contenido del portapapeles (X11)
- `/` - último patrón de búsqueda
- `:` - última línea de comandos
- `.` - último texto insertado
- `-` - último pequeño (menos de una línea) eliminar
- `=` - registro de expresión
- `_` - registro de agujero negro
## Marcas
- `:marks` - mostrar marcas
- `ma` - definir posición actual para la marca A
- `` a`` - saltar a la posición de la marca A
- `ya` - copiar texto a la posición de la marca A
- `` 0`` - ir a la posición donde se había salido previamente de Vim
- `` `"` `` - ir a la posición en la que se editó por última vez este archivo
- `` `.` `` - ir a la posición del último cambio en este archivo
- `` ```` - ir a la posición antes del último salto
- `:ju[mps]` - lista de saltos
- `Ctrl + i` - ir a la nueva posición en la lista de saltos
- `Ctrl + o` - ir a la posición anterior en la lista de saltos
- `:changes` - lista de cambios
- `g,` - ir a la nueva posición en la lista de cambios
- `g;` - ir a la posición anterior en la lista de cambios
- `Ctrl + ]` - saltar a la etiqueta debajo del cursor

> [!info] **Tip**: Para saltar a una marca, puedes usar una tilde (` `` ` ) o un apóstrofo (`'`). Usar un apóstrofo salta al inicio (primer carácter no-espacio) de la línea que contiene la marca.

## Macros
- `qa` - grabar macro en el registro `a`
- `q` - detener la grabación de la macro
- `@a` - ejecutar macro en el registro `a`
- `@@` - reje la última macro

## Copiar y pegar
- `yy` - copiar una línea
- `2yy` - copiar dos líneas
- `yw` - copiar desde la posición del cursor hasta el inicio de la siguiente palabra
- `yiw` - copiar la palabra en la posición del cursor
- `yaw` - copiar la palabra y el espacio que la rodea
- `y$` o `Y` - copiar hasta el final de la línea
- `p` - pegar después del cursor
- `P` - pegar antes del cursor
- `gp` - pegar después del cursor y mover después del nuevo texto
- `gP` - pegar antes del cursor y mover después del nuevo texto
- `dd` - cortar una línea
- `2dd` - cortar dos líneas
- `dw` - cortar desde la posición del cursor hasta el inicio de la siguiente palabra
- `diw` - cortar la palabra en la posición del cursor
- `daw` - cortar la palabra y el espacio que la rodea
- `:3,5d` - cortar desde la línea 3 hasta la línea 5

> [!info] **Tip**: Puedes usar rangos en los comandos de cortar:
- `:.,$d` - desde la línea actual hasta el final del archivo
- `:.,1d` - desde la línea actual hasta el inicio del archivo
- `:10,1d` - desde la décima línea hasta el inicio del archivo

- `:g/{pattern}/d` - cortar todas las líneas que contengan el patrón
- `:g!/{pattern}/d` - cortar todas las líneas que no contengan el patrón
- `d$` o `D` - cortar hasta el final de la línea
- `x` - cortar un carácter

## Sangría del texto
- `>>` - sangrar (mover a la derecha) una línea
- `<<` - desangrar (mover a la izquierda) una línea
- `>%` - sangrar un bloque con `()` o `{}` (cursor sobre llave)
- `<%` - desangrar un bloque con `()` o `{}` (cursor sobre llave)
- `>ib` - sangrar el bloque interior con `()`
- `>at` - sangrar un bloque con etiquetas `< >`
- `3==` - resangrar 3 líneas
- `=%` - volver a sangrar un bloque con `()` o `{}` (cursor sobre llave)
- `=iB` - volver a sangrar el bloque interior con `{}`
- `gg=G` - volver a sangrar todo el buffer
- `]p` - pegar y ajustar la sangría a la línea actual

## Salir
- `:w` - guardar archivo sin salir
- `:w !sudo tee %` - guardar archivo usando sudo
- `:wq` o `:x` o `ZZ` - guardar archivo y salir
- `:q` - salir (no funciona si hay cambios sin guardar)
- `:q!` o `ZQ` - salir descartando los cambios no guardados
- `:wqa` - guardar y salir en todas las pestañas

## Buscar y reemplazar
- `/pattern` - buscar patrón
- `?pattern` - buscar patrón hacia atrás
- `\vpattern` - patrón 'muy mágico' (very magic): los caracteres no alfanuméricos son interpretados como caracteres de expresiones regulares
- `n` - repetir la búsqueda en la misma dirección
- `N` - repetir la búsqueda en la dirección contraria
- `:%s/old/new/g` - reemplazar en todo el archivo
- `:%s/old/new/gc` - reemplazar en todo el archivo con confirmación
- `:noh[lsearch]` - desactivar el realce (highlight) de los resultados de búsqueda

## Buscar en varios archivos
- `:vim[grep] /pattern/ {file}` - buscar un patrón en varios archivos

> [!info] **Ejemplo**:
- `:vim[grep] /foo/ **/*`

- `:cn[ext]` - ir al resultado siguiente
- `:cp[revious]` - ir al resultado previo
- `:cope[n]` - abrir ventana con una lista de los resultados
- `:ccl[ose]` - cerrar la ventana de corrección rápida

## Pestañas
- `:tabnew` o `:tabnew {archivo}` - abrir archivo en una nueva pestaña
- `Ctrl + wT` - mover la ventana actual a su propia pestaña
- `gt` o `:tabn[ext]` - ir a la pestaña siguiente
- `gT` o `:tabp[revious]` - ir a la pestaña anterior
- `#gt` - ir a la pestaña número #
- `:tabm[ove] #` - mover la pestaña actual a la posición #
- `:tabc[lose]` - cerrar la pestaña actual
- `:tabo[nly]` - cerrar todas las pestañas excepto la actual
- `:tabdo` command - ejecutar `command` en todas las pestañas (p. ej., `:tabdo q` - cierra todas las pestañas abiertas)

## Trabajar con varios archivos
- `:e[dit] archivo` - editar un archivo en un nuevo buffer
- `:bn[ext]` - ir al buffer siguiente
- `:bp[revious]` - ir al buffer anterior
- `:bd[elete]` - eliminar buffer (cerrar archivo)
- `:b[uffer]#` - ir a un buffer por número
- `:b[uffer] archivo` - ir a un buffer por archivo
- `:ls` o `:buffers` - mostrar todos los buffers abiertos
- `:sp[lit] archivo` - abrir archivo en un nuevo buffer y dividir la ventana
- `:vs[plit] archivo` - abrir archivo en un nuevo buffer y dividir la ventana verticalmente
- `:vert[ical] ba[ll]` - editar todos los buffers como ventanas verticales
- `:tab ba[ll]` - editar todos los buffers como pestañas
- `Ctrl + ws` - dividir ventana
- `Ctrl + wv` - dividir ventana verticalmente
- `Ctrl + ww` - cambiar de ventana
- `Ctrl + wq` - cerrar ventana
- `Ctrl + wx` - intercambiar la ventana actual con la siguiente
- `Ctrl + w=` - hacer que todas las ventanas tengan la misma altura y ancho
- `Ctrl + wh` - mover el cursor a la ventana izquierda (división vertical)
- `Ctrl + wl` - mover el cursor a la ventana derecha (división vertical)
- `Ctrl + wj` - mover el cursor a la ventana de abajo (división horizontal)
- `Ctrl + wk` - mover el cursor a la ventana de arriba (división horizontal)
- `Ctrl + wH` - extender el ancho de la ventana (vertical) hacia la izquierda
- `Ctrl + wL` - extender el ancho de la ventana (vertical) hacia la derecha
- `Ctrl + wJ` - extender el alto de la ventana (horizontal) hacia abajo
- `Ctrl + wK` - extender el alto de la ventana (horizontal) hacia arriba

## Diferencia
- `zf` - definir manualmente un pliegue hasta el movimiento
- `zd` - eliminar pliegue debajo del cursor
- `za` - alternar pliegue debajo del cursor
- `zo` - abrir pliegue debajo del cursor
- `zc` - cerrar pliegue debajo del cursor
- `zr` - reducir (abrir) todos los pliegues en un nivel
- `zm` - doblar más (cerrar) todos los pliegues en un nivel
- `zi` - alternar la funcionalidad de plegado
- `]c` - saltar al inicio del próximo cambio
- `[c` - saltar al inicio del cambio anterior
- `do` o `:diffg[et]` - obtener diferencia (de otro buffer)
- `dp` o `:diffpu[t]` - poner diferencia (a otro buffer)
- `:diffthis` - hacer que la ventana actual forme parte de diff
- `:dif[fupdate]` - actualizar diferencias
- `:diffo[ff]` - desactivar el modo diff para la ventana actual

> [!info] **Tip**: Los comandos de plegar (`za`) operan en un nivel. Para operar en todos los niveles, usa letras mayúsculas (p. ej. `zA`).

> [!info] **Tip**: Para ver las diferencias de archivos, puedes iniciar Vim directamente en el modo diferencias ejecutando `vimdiff` en una terminal. Incluso se puede configurar como `git difftool`.
