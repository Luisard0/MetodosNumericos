from MetodosNum.Biseccion import Biseccion
# Test pal método de Bisección

limiteA = 0
limiteB = 1
expresion = "(x**3) +x -1"
tolerancia = 0.0001

biseccion = Biseccion(limiteA, limiteB, expresion, tolerancia)
biseccion.calcularRaiz()
biseccion.mostrarGrafica()
print("\nTest passed :)")