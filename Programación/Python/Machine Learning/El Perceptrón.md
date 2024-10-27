#MachineLearning #Perceptrón

El perceptrón es la evolución de [[La Neurona de Mcculloch y Pitts]]. Propuesto por Frank Rosenblatt en 1958, posteriormente refinado por Marvin Minsky y Seymour Papert. Consta de varias `TLU's` (Threhold Logic Unit) con diversas entradas, esta vez con un peso asignado y el `treshold` o limite de activación esta involucrado en la misma ecuación, por lo tanto, se calcula automáticamente y por defecto su peso es de uno.

![[perceptron.png]]

El perceptrón hace una suma parametrizada de las entradas, pero también plantea un mecanismo para ajustar estos pesos automáticamente, ósea, __aprender__. La gran ventaja de este es que ahora no solo recibe valores binarios, sino que tiene la capacidad de recibir valores numéricos.

La formula de su comportamiento de agregación es el siguiente:

$$\sum_{i=1}^n{W_i}*{X_i}=W_1*X_1+W_2*X_2+...+W_n*X_n+b$$

> El termino `b` es conocido como `bias term` (termino de parcialidad), que es el equivalente al limite de activación o al `treshold`. Teóricamente también se debe multiplicar por `W` sin embargo, en la mayoría de casos se usa el valor `1`, por eso se queda la `b` sola.

A este resultado se le conoce como `Z(x1, x2, .. xn)`, la gran ventaja de usar el perceptrón es que podemos usar `n` neuronas para solucionar un problema, aunque este esta planteado como una sola capa (output layer). Por ende, así como [[La Neurona de Mcculloch y Pitts]] solo puede solucionar problemas linealmente separables.

Esta formula esta contemplando una sola Threshold Logic Unit, por ende, si contásemos con mas TLU's, deberíamos enumerar las `W`'s por entradas, por lo que la función de activación (para dos entradas) seria:

$$
h_w(x)_1=a_1(X_1W_{11}+X_2W_{21}+b_3)
$$
$$
h_w(x)_2=a_2(X_1W_{12}+X_2W_{22}+b_2)$$
$$h_w(x)_3=a_3(X_1W_{13}+X_2W_{23}+b_1)$$

En la salida, para este caso, tendremos tres tipos de salidas binarias, la ventaja de esto es que podemos tener una salida de clasificatoria, por ejemplo, una neurona puede estar entrenada para identificar un numero especifico en una imagen, por lo que cuando este numero se presente, tendremos un uno en en la salida específicamente en esa. Esto es útil para la clasificación, inclusive podríamos tener letras como salidas si usamos código ASCII.

Existen dos principales criterios de activación del perceptrón, ambos son funciones escalón:

> Función de activación _Heaviside_:

^05892c

$$
H(x) =
\begin{cases}
1, & \text{si } x \geq 0 \\
0, & \text{si } x < 0
\end{cases}
$$
![[heaviside_func.png|450]]
> Función de activación _Sign function_:

$$
\text{sign}(x) =
\begin{cases}
1, & \text{si } x > 0 \\
0, & \text{si } x = 0 \\
-1, & \text{si } x < 0
\end{cases}
$$

![[sign_func 1.png|400]]
A los coeficientes de multiplicacion tambien se les conoce como parametros del modelo. Ya que normalmente estos se calculan al momento de entrenar el modelo y no se asignan manualmente.

## Construcción del Modelo

Para construir el modelo, se utiliza una formula para poder aproximar los pesos a un valor que mejore el comportamiento de nuestras `TLU's` y así pueda llevar a cabo predicciones, esta formula es:

$$w_{ij}=w_{ij}+\eta(y_j-\hat{y}_j)x_i$$ ^bfd3b4

Un ejemplo de uso, en el que tenemos dos entradas (`x1 y x2` {contando `bias termn`}) y las llevamos a tres neuronas, para los valores de la primer `TLU` quedaría así nuestro remplazo:

$$TLU_{1}\Rightarrow (W_{11}, W_{21}, b)$$
Estos datos se inicializan aleatoriamente:
$$W_{11} = -1,\quad W_{21}=0,\quad b_1=-0.5$$
$$\hat{y}\quad-\quad\text{Salida esperada (label)}=0$$
$$x_{1}= \text{2 - Valor de ejemplo}$$
Ahora, nosotros conocemos la salida $\hat{y}$, imaginemos que es `1`, para este caso, las entradas $x_1=1$ y $x_2=5$, tal que la sumatoria: $-1*1+0*5+(-0.5) = -1.5$, y suponiendo que estamos usando la [[El Perceptrón#^05892c|función de activación heaviside]], nuestra salida seria 0, eso quiere decir que nuestra predicción esperada (`1`) no es correcta. 

Para este caso, debemos aplicar la [[El Perceptrón#^bfd3b4|función]] señalada:

$$W_{11} = W_{11} + \eta (y_1-\hat{y_1})x_{1} \quad = \quad (-1) + 0.5(1-0)2 = 0$$
- $\eta$  - Corresponde al radio de aprendizaje (`learning rate`), un numero muy grande, puede ocasionar que nos pasemos del valor optimo.
- $y$  - Corresponde a la salida (label) ya esperada.
- $\hat{y}$  - Corresponde a la salida actual del modelo.

Ahora, el nuevo valor de $W_{11}$ será `0`, lo cual ajusta nuestro modelo de tal manera que su siguiente predicción sea mas acercada al resultado esperado.

## Limitaciones del Perceptrón

- Su resultado es estático, no proporciona una probabilidad de acierto.
- Solo construye limites de decisión lineal.
- Algunos problemas sencillos, como la XOR no pueden ser solucionados con este.
- Muchos de los conflictos presentes en el Perceptrón se solucionan con el Perceptrón Multicapa.