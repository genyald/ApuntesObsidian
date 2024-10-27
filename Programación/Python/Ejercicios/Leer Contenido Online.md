#Python #HTTP #Consulta #With #Open

Tenemos el siguiente [Archivo Online](https://globalmentoring.com.mx/recursos/GlobalMentoring.txt) y tiene una extension `txt`, queremos descargarlo para procesarlo como `UTF-8` y mostrarlo correctamente.

Para leer contenido online usaremos una libreria que nos permite obtener informacion de una `URL` (Uniform Resourse Locator), `urllib.request`.

>Primero importamos `urllib.request: urlopen, Request` y posteriormente definimos el url y los encabezados para hacer la consulta:

```python
from urllib.request import urlopen, Request

url = 'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}
```


> [!question]- Headers
> Los headers son encabezados con los que se hace una consulta http, son necesarios para que el servidor pueda saber informacion sobre el dispositivo que hace la consulta. Se entregan como un diccionario. Los anexados arriba son los del navegador por defecto en mi equipo, desde ege.


>Posteriormente hacemos el debido `request` del `URL`, para simular que accedemos desde un navegador valido, esto devuelve un objeto `request`:

```python
# Hacemos un request del URL
request = Request(url, headers=headers)
```

>Finalmente con `with` consultamos el contenido que devolvio el `Request`:

```python
# Abrimos el url con el request
with urlopen(request) as mensaje:
	contenido = mensaje.read()
	print(contenido)
```

Como se puede observar, el contenido leido no esta decodificado, por lo que hay que hacerlo en `UTF-8`:

```python
# UTF-8
with urlopen(request) as mensaje:
	contenido = mensaje.read()
	contenido = contenido.decode('UTF-8')
	print(contenido)
```

Ahora que ya contamos con todo el contenido decodificado, podriamos guardarlo en un archivo `txt`:

```python
with open('consulta_online_utf8.txt', 'w', encoding='utf-8') as file:
	file.write(contenido)
	print('Archivo guardado exitosamente.')
```

### Interpretar Con Listas lo Leido

Hacemos el request y abrimos el contenido del request, al contenido le podemos aplicar el metodo `.split()` antes de decodificarlo para separarlo por palabra y enviarlo a una lista:

```python
from urllib.request import urlopen, Request

url = 'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0'}

# Hacemos un request del URL
request = Request(url, headers=headers)
lista = []

# Abrimos el url con el request
with urlopen(request) as mensaje:
    contenido = mensaje.read()
    contenido = contenido.decode('UTF-8').split()
    print(contenido)
```