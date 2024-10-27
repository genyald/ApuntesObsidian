#MachineLearning #PrimerNeurona #MccullochYPitts

La neurona de Mcculloch y Pitts es la primer neurona artificial informática. Esta esta dividida en dos partes o secciones, la sección de *agregación* y la sección de *decisión*:

![[neurona_mp.png]]

Para definir si una neurona MP se activara o no, necesitamos definir un `treshold` que es en si un limite de activacion. Por ejemplo, para el caso de un `treshold` de 3, cuando tres condiciones `z(x`<sup>1</sup>,`x`<sup>2</sup>, `x`<sup>3</sup>,`x`<sup>4</sup>, `x`<sup>5</sup>`)` se cumplan, tendremos una salida de `1` lógico. 

La formula matemática se ve asi:

$$Z(x_1,x_3,x_4,x_5)=Z(X)=$$
$$\sum_{i=1}^{n=4}x_{i}=x_1+x_2+x_3+x_4+x_5$$

Siendo `n = Numero de caracteristicas de entrada (5)`.

Entonces, podemos decir que `a(Z(X))` es igual a uno si `Z(X) >= treshold` e igual a cero si `Z(X) < treshold`.

> *La Neurona MP tiene dos tipos de entradas*:

- Excitadores: Son los que se suman a la salida para llegar al `treshold` y poner en uno la salida.
- Inhibidores: Son los que bloquean directamente la salida, es como una AND al final.