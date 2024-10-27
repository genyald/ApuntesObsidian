---
autor: Genos
---
## Texto

^baf2c7

- *El texto cursivo se hace con los asteriscos*
- **El texto en negritas se hace con asteriscos
- ~~Para tachar Texto se encierra en '~'~~
- ==Se encierra en == el texto a subrayar==

>Si colocamos el símbolo de '>' estamos agregando importancia a un párrafo para hacer una especie de nota

### Linea de Separación

La linea de separación se coloca con tres guiones bajos.
___
### Listas

- [ ] Elemento 1 de lista
	- [ ] Elemento 2 de lista con tabulación al inicio
- [x] Elemento 3 de lista

___

## Etiquetas

Sirven para categorizar los temas, de esta manera, podemos tener todo lo relacionado a un tema a solo un click para tener correlacionado, sin necesidad de vincularlo en nuestro cerebro artificial, se agregan con un # seguido del texto sin espacios de la etiqueta, si agregas un / significa que pertenece a una etiqueta de un grupo mas grande.

[[obsidian/format]]

## Callouts

>[!note] Recuerda
>Para formar una nota aun mas impactante usamos el carácter >[!Nota]

Estos son los tipos de [Callouts](https://help.obsidian.md/Editing+and+formatting/Callouts)
### Callout Desplegable

>[!info]- Desplegable
>Para formar una nota desplegable como esta usamos la misma que la de arriba pero le agregamos el carácter - al final

## Imagenes

Elegir tamaño de una imagen importada, solo agregamos un | y el tamaño en pixeles [imagen|300x300], por ejemplo seguido de una coma para elegir (LargoxAncho): (Debe estar descargada)

![[Pasted image 20230810233251.png|300x200]]


## Citas

Si al importar un archivo para visualizarlo le ponemos una # podremos importar solamente una parte del texto, la cual esta dividida por # del titulo.

Con el caracter ^ podemos citar solamente un parrafo de otro apunte.

Si al terminar nuestro apunte le ponemos ^ y las palabras, estamos destacando este texto para que pueda ser mandado a llamar mas adelante. ^LlamarParrafo

Lo mando a llamar:

```
![[Formatos en Obsidian#^LlamarParrafo]]
```

![[Formatos en Obsidian#^LlamarParrafo]]

## Links e Hipervinculos

### Hipervinculo visual

Para crear hipervínculos visuales, agregamos unos corchete {titulo} y en seguida dentro de parentesis nuestro hipervinculo a considerar.  [Ubuntu](https://www.ubuntu.com 'Hola') (Usamos 'Hola') para que sea el texto mostrado al poner el raton encima.

### Podemos 

### Citar otros apuntes

Para vincular texto a un nuevo texto o entrada de texto dentro de nuestra bobeda, podemos simplemente usar doble corchetes [[PRUEBA]]

Si agregamos el símbolo de exclamación a la entrada de texto de nuestra bobeda, automáticamente la incluirá a nuestro texto:

![[PRUEBA]]

### Traer el vinculo en crudo

Si al agregar el hipervínculo, agregas un simbolo de exclamacion de por ejemplo una imagen, esta automáticamente se introducirá en nuestro texto:
![Ubuntu_Logo](https://icons.iconarchive.com/icons/papirus-team/papirus-apps/512/distributor-logo-ubuntu-icon.png)

## Código

**Para crear bloques de codigo solo tienes que agregar tres veces el simbolo que esta debajo del espacio, de esta manera, esto se vuelve codigo que se puede copiar:**

```bash
sudo apt-get install metasploit-framework
```

## Comentarios

```
%%Este comentario es solo visible en modo edición%%
```


## HTML

Obsidian es compatible con muchas sentencias `html`, como `<sup> super </sup>`:

Texto<sup> hola </sup>
Hola<sub>Texto</sub>
