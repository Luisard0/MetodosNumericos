from MetodosNum.NewtonRaphson import NewtonRaphson
# Test para el método de Newton-Raphson

funcion = "exp(x) - (1 / (x**2))"
v_inicial = 1
presicion = 5

newton_raphson = NewtonRaphson(funcion, v_inicial, presicion)
newton_raphson.calcularRaiz()
newton_raphson.mostrarGrafica()