Son un tipo de grafos cuyos ==nodos== corresponden ==una operación== o una variable y ==los arcos== con valores de entrada/salida:

$$f(g(h(x))) \longrightarrow e^{sin(x^2)}$$
$$\therefore\quad f(x) = e^x \quad, \quad g(x)=sin(x)\quad,\quad h(x)=x^2$$
$$e^{sin(x^2)}\begin{cases}
f(x) = e^x \\ g(x)=sin(x)\\ h(x)=x^2
\end{cases}$$
Esta ecuación compuesta, podemos convertirla en un grafo computacional:

![[GrafoComputacional]]

En este caso del Deep Learning, estamos usando la salida de una función en otra función, es una forma factible de representar algorítmicamente cada operación de salida, por ejemplo, las operaciones especificas de una TLU.

