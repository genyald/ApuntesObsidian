#Python #Ejercicio 

En este ejercicio, se debe crear una funciona para calcular el total de un pago incluyendo un impuesto apolicado:
$$PagoTotal = PagoSinImpuesto + PagoSinImpuesto \times{\frac{impuesto}{100}}$$

```python
def calcularImpuesto(pago, impuesto):
	impuestoTotal = pago + pago*(impuesto/100)
	return impuestoTotal

pago = float(input('Cuando debes pagar?: '))
impuesto = float(input('A que porcentaje de impuesto?: '))
print(f'Tu total a pagar con impuestos es de {calcularImpuesto(pago, impuesto)}')
```