Para agregar una formula en latex solo tienes que empezar con dos veces el simbolo de pesos/dolar ($)

>Ejemplo:

$$
x = \frac{x}{2}\frac{dx}{dy}
$$

>Segundo ejemplo:

$$
\frac{x-2}{x-2} =a^{x\delta}
$$


# Guía Básica de LaTeX para Fórmulas Matemáticas

## Configuración del Documento:

\documentclass{article}
\usepackage{amsmath} % Para habilitar el entorno matemático
\begin{document}

## Entornos de Fórmulas Matemáticas:

- En línea: $...$ o \(...\)
- En bloque: \[...\] o \begin{equation}...\end{equation}

## Operadores Básicos:

- Suma: +
- Resta: -
- Multiplicación: \times o *
- División: \div o /
- Exponenciación: ^
- Raíz cuadrada: \sqrt{...}

## Símbolos Especiales:

- Fracciones: \frac{numerador}{denominador}
- Sumatorias: \sum_{inicio}^{fin}
- Productorias: \prod_{inicio}^{fin}
- Integrales: \int_{inicio}^{fin}

## Letras y Símbolos:

- Letras griegas: \alpha, \beta, \gamma, ...
- Letras del alfabeto: a, b, c, ...
- Símbolos especiales: \in, \notin, \forall, \exists, ...

## Ecuaciones en Múltiples Líneas:

\begin{align*}
Ecuación1 \\
Ecuación2 \\
Ecuación3 \\
\end{align*}

## Subíndices y Superíndices:

- Subíndices: _
- Superíndices: ^

## Matrices:

\begin{matrix}
a & b \\
c & d \\
\end{matrix}

## Fórmulas Especiales:

- Ecuación cuadrática: x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}