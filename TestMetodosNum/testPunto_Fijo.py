from MetodosNum.PuntoFijo import PuntoFijo

# Test para el método de Punto fijo

funcion = "(x**2)-(2*x)-3"
v_inicial = 4
precision = 10
tolerancia = 3
subfunciones = ["((2*x) + 3)**(1/2)", "3 / (x-2)"]

puntoFijo = PuntoFijo(funcion, v_inicial, precision, tolerancia, subfunciones)
puntoFijo.calcularRaiz()
puntoFijo.mostrarGrafica()

print("Test passed :D")