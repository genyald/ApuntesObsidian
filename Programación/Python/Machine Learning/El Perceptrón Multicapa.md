#Perceptrón #PerceptrónMulticapa

El perceptrón multicapa o `Deep feedforward network` es el modelo mas popular dentro del Deep Learning, se le llama `feedforward` porque no lleva ningún tipo de feedback (sistema de lazo abierto). Esta compuesto por una `input layer` y una o mas capas de `TLU's`. 

Su principio es igual que el de el perceptrón de una capa, cuenta con sus inputs ($x_1,x_2,...,x_n,b$), utiliza una función de error que se usa para la función de optimización (calculo de pesos o aprendizaje) y contiene una salida. 

Sus principales agregados son:
- A la capa de TLU's intermedias se le denomina `hidden layer`.
- A la capa final de `TLU's` se le denomina `output layer`.
- Todas las capas, excepto la output layer incluyen la `bias neuron` o `bias termn`.
- Todas las capas están subsecuentemente conectadas.
- Cuando una Red Neuronal Artificial (ANN) tiene dos o mas hidden layers, se le denomina `Deep Neural Network` (DNN).
- Cada una de las capas estan enumeradas con la letra $l$. Esta variable representa el numero total de capas presente en nuestra red neuronal.
## Funcionamiento

En 1986,  D. E. Rumelhart presenta un algoritmo que revoluciona la forma de entrenar al perceptrón multicapa, ya que su mayor limitante es que no existia la forma adecuada de entrenarlo, el algoritmo `backpropagation`. Su principal funcionamiento se basa con una diferencia del perceptrón: La función de activación, la cual es conocida como función sigmoide:

$$\text{Sigmoid Function} \quad-\quad f(x)=\frac{1}{1+e^{-x}}$$


Gráficamente, la función sigmoide se ve de la siguiente manera:

```functionplot
---
title: Sigmoid Function
xLabel: g(z)
yLabel: z
bounds: [-6,6,-0,1]
disableZoom: false
grid: false
disableZoom: true
lock: true
---
f(x)= 1/(1+E^(-x))
```

Su funcionamiento es muy analógico al perceptrón común, sin embargo, en la salida tendremos un resultado continuo y no uno binario. Esto quiere decir, que en la salida obtendremos __la probabilidad de que nuestra entrada pertenezca a nuestra clase__, la principal ventaja de esto es que ya no obtendremos una salida que esta limitado a ser completamente lineal.


> [!info] Otras funciones de activación
> Existen las funjciones $tanh(z)$ y la $ReLU(z)$.

Su entrenamiento también es muy similar al del perceptrón común, tenemos una función de error que proviene de la inicialización aleatoria de los pesos, comparada con el resultado esperado. Posteriormente esta función se usa para optimizar todo el sistema, esperando cada vez aproximarse mas al resultado esperado. 

![[DNN.png]]

Para la primer neurona de la capa de entrada de 2 entradas y $l$ de 3 capas:

$$Z_1^{[1]}=W_{11}^{[1]}*a_1^{[0]}+W_{21}^{[1]}*a_2^{[0]}+b_1^{[1]}$$

Ahora, esta es la salida de la suma ponderada de la primer TLU, esto quiere decir que debe pasar por la función sigmoide para ser activada:

$$a_1^{[1]}=\text{sigmoide}(Z_{1^{[1]}})\quad \therefore \quad Z_1^{[2]}=W_{11}^{[2]}*a_1^{[1]}+W_{21}^{[2]}*a_2^{[1]}+W_{31}^{[2]}*a_3^{[1]}+b_1^{[2]}$$

Eso quiere decir que se calcula $a$ para cada neurona, que se usara para la siguiente capa, por lo que el modelo implica muchísimas multiplicaciones, sumas y funciones de activación en cada TLU. __Este es el algoritmo `backpropagation`__.

Un ejemplo practico seria el `reconocimiento de un automovil` en una imagen de 300 x 400 pixeles (px). Eso quiere decir que tendremos una capa de entrada de 120,000 TLU's. Si tuviésemos solamente una TLU como `output layer`/`hidden layer`, quiere decir que tendríamos hasta $W_{120,000}$ como parámetro de entrada de el perceptrón multicapa, su salida seria la función sigmoide con la probabilidad de que haya presente un automóvil en la imagen. En este teórico caso, tendríamos un `bias neuron` que sumaria una entrada extra.

![[foward_propagation.png]]

Si tuviésemos dos capas escondidas y tres TLU's en cada una, entonces deberíamos tener una `bias neuron` en cada capa, por lo que para una entrada de 120,000 + 1 parámetros por TLU en la primer capa, ósea 360,003 parámetros de entrada . En la capa subsecuente, tendríamos 3 de mas, mas la b que se dirige a cada una, tendríamos un total de 120,019 parámetros de entrada.

## Función de Coste

La función de coste o la función de error es la que se encarga de medir la cercanía de la salida del algoritmo de `foward propagation` con la etiqueta esperada. Esta función de coste/error es usada para ajustar los pesos del modelo y la próxima vez esperar un resultado mas cercano a lo esperado. 

Si tuviésemos en un eje la salida y en otra la función de coste, tendríamos dos salidas, una para la que $\hat{y}$ vale 0 y otra donde vale 1:

$$\text{Si} \quad \hat{y} \rightarrow 1$$

<iframe src="https://www.desmos.com/calculator/7qkakne5uv?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

$$\hat{y}=1 \quad , \quad L(\hat{y}, y)=-log(\hat{y}) $$
En este caso, el valor de $\hat{y}$ es igual a uno, entonces, si en nuestra salida estamos teniendo 1, la función de coste tiende a cero, sin embargo, entre mas nos alejemos del resultado esperado, nuestra función de coste tendera a a infinito.

$$\text{Si} \quad \hat{y} \rightarrow 0$$
<iframe src="https://www.desmos.com/calculator/huy2kfdqa8?embed" width="500" height="500" style="border: 1px solid #ccc" frameborder=0></iframe>

$$\hat{y}=0 \quad , \quad L(\hat{y},y)=-log(1-\hat{y})$$

Si unimos estas dos ecuaciones, podemos llegar a la siguiente función de error:

Si la etiqueta $\hat{y}$ es correcta, entonces la función de coste será cero, Si la función de coste se aleja del valor esperado (0), se aproxima a infinito. 

Las funciones de error de cada comportamiento serán las siguientes:

$$\hat{y}=1 \quad , \quad L(\hat{y}, y)=-log(\hat{y}) $$
$$\therefore \quad \hat{y}= -log(sigmoid(X_1*W_1+...+X_n*W_n+b))$$
Y para una $\hat{y}$ negativa:
$$\hat{y}=0 \quad , \quad L(\hat{y},y)=-log(1-\hat{y})$$
$$L(\hat{y}, y)=-y*log(\hat{y})-(1-y)log(1-\hat{y})$$
El $-y$ es para quitar el primer termino si $y \rightarrow 0$. El $(1-y)$ es para eliminar el segundo termino si $y \rightarrow 0$, de esta manera, integramos ambas funciones de error en una misma, si $y \rightarrow 1$ quiere decir que usaremos la primer función de error, si $y \rightarrow 0$ entonces estamos usando la segunda.

Entonces, el error global de todas las etiquetas se calcula así:

$$J(W,B)=\frac{1}{m}\sum\limits^m_{i=1}L(\hat{y}^{[i]},y^{[i]})$$

Prácticamente consiste en calcular los errores para todos los ejemplos y dividirlos entre el total de estos. Ósea el promedio de todos los errores computados.

Esta misma ecuación de error, desarrollada, contemplando la formula de $L(\hat{y}^{[i]},y^{[i]})$, llegamos a la formula llamada $\text{Funcion de Coste de Entropia Cruzada Binaria}$ (`Cross Entropy Loss`):

$$J(W,B)=-\frac{1}{m}\sum\limits^m_{i=1}y^{[i]}*log({\hat{y}^{[i]}})+(1-y)*log(1-\hat{y})$$
## Gradiente Descendente

La función de gradiente descendente es la función de optimización mas utilizada en el machine learning y deep learning, esta parte de la función de la $\text{Funcion de Coste de Entropia Cruzada Binaria}$, si aplicamos esta funciona a una TLU, podemos aproximarnos al minimo de nuestra funcion de error, mediante la siguiente formula:

$$W=W-\eta\frac{dJ}{dW}$$
Su comportamiento, si $\eta$ fuese muy pequeño, sería muy semejante a una parábola.

```functionplot
---
title: Gradiente Descendente
xLabel: w
yLabel: J(w)
bounds: [-2,2,0,2]
disableZoom: true
grid: false
---
f(x)=x^2
```

Esto se debe, a que estamos asignando el valor del siguiente peso a la resta de el radio de aprendizaje ($\eta$) multiplicado por la pendiente en ese intervalo. Lo cual hace que, al multiplicar por la derivada inversa, nos aproximemos más a el mínimo de la función. Recordar que $\frac{dx}{dy}=0$ cuando nos encontramos en un mínimo o máximo de una función.

> [!info] Existen más funciones de error.

Si desarrollamos la ecuación, queda tal que:

$$W=W-\eta(x(\hat{y}-y))$$
## Ejemplo de Optimización Gradiente Descendente

A continuación, un ejemplo explicado de la implementación del algoritmo de gradiente descendente para con una sola TLU para simplificar la explicación.

![[Perceptron_TLU.excalidraw]]

Primero, considerando una TLU de dos entradas ($x_{1},x_2,b$):
- Calculamos el `fordward propagation` para $\hat{y}$ con pesos inicializados aleatoriamente:
$$\hat{y}^{[i]}=\text{sigmoid}(x_1^{{[i]}}*W_1+x_2^{[i]}+b)$$
- Usamos la función de `Cross Entropy Loss` para conocer el error de la `foward propagation` y __lo sumamos al error anterior ($J$):__
$$L(\hat{y},y)=L + (-y^{[i]}*log({\hat{y}^{[i]}})+(1-y)*log(1-\hat{y}))$$
- Calculamos la función de optimización para cada peso y __sumamos el resultado anterior__:
$$d_{w1}=d_{w1}+\frac{dJ}{dw_1}\quad\therefore \quad dw_1=dw_1+x_1^{[i]}(\hat{y}^{[i]}-y^{[i]})$$

$$d_{w2}=d_{w2}+\frac{dJ}{dw_2}\quad\therefore \quad dw_2=dw_2+x_2^{[i]}(\hat{y}^{[i]}-y^{[i]})$$
$$d_{b}=d_{b}+\frac{dJ}{db}\quad\therefore \quad d_b=d_b+1(\hat{y}^{[i]}-y^{[i]})$$
- Hacemos esto para cada uno de nuestro parámetros o entradas hasta tener sumados los errores $L$ y los cambios $d_{w1}$ y finalmente, calculamos los nuevos pesos $W$:

$$W_1=W_1-\eta*d_{w1} \quad , \quad W_2=W_2-\eta*d_{w2} \quad,\quad b=b-\eta*db$$
- Una vez completado esto, tendremos una iteración del gradiente descendente, por lo que para aproximarnos aun mas a el error mínimo, debemos hacer nuevamente todo el proceso con nuestros datos de entrenamiento para poder reducir el error.


## Origen del Gradiente Descendente

El gradiente descendente parte del principio fundamental de calcular el cambio o pendiente de nuestra presicion, ajustan el peso o valor de $W$ para poder ajustarse y mejorar la precisión. Ahora, para poder calcular la pendiente, requerimos llegar a la derivada:

$$\frac{\delta{L}}{\delta w_1}$$
La cual, en este caso seria, el cambio en el error con respecto al peso de $W_1$, esto se deberá repetir para cada uno de los pesos, claro, considerando que haremos `back propagation`.

$$\frac{dL}{dW_1}=\frac{dZ}{dW_1}\cdot\frac{da}{dZ}\cdot\frac{dL}{da}$$

Esto es aplicando la regla de la cadena, partiendo del grafo:

![[Grafo.ExplicacionPerceptronMulticapa]]

Entonces, toca calcular las respectivas derivadas:

$$\frac{dL}{dW_1}=\frac{d}{dW_1}[x_1w_1+x_2w_2+b]\cdot\frac{d}{dZ}[\frac{1}{1+e^{-z}}]\cdot\frac{d}{da}[-ylog(a)-(1-y)\cdot log(1-a)]$$

Esto es igual a:

$$\frac{\delta{L}}{\delta w_1}=(\frac{1-y}{1-a}-\frac{y}{a})\cdot(a(1-a))\cdot x_1$$
Desarollando y simplificando:

$$\frac{\delta{L}}{\delta w_1}=(a-y)\cdot x_1$$
$a$ es igual a la funcion de salida sigmoide total para una sola TLU, por lo que podemos concluir que para la salida total de un modelo es:

$$\frac{\delta{L}}{\delta w_1}=w_1-\eta(\hat{y}-y)\cdot x_1$$
Llegando finalmente a la función de gradiente descendente multiplicándolo por el `learning rate` ($\eta$) invertido para cada vez aproximarse mas al mínimo error posible.