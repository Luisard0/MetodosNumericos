from MetodosNum.NewtonRaphson import NewtonRaphson
from MetodosNum.Biseccion import Biseccion
from MetodosNum.PuntoFijo import PuntoFijo

"""
    Prototipo de la calculadora/menu implementada
"""

def menu():
    print("-"*40)
    print("Menú:\n[1]: Bisección\n[2]: Punto Fijo\n[3]: Newton-Raphson\n[4]: Salir")
    print("-"*40)
    return int(input("Selecciona una opción: "))


def biseccion():
    intervalo_a = float(input("Introduce el valor del intervalo A: "))
    intervalo_b = float(input("Introduce el valor del intervalo B: "))
    presicion = float(input("Introduce la tolerancia: "))
    funcion = input("Introduce la función: ")

    biseccion = Biseccion(intervalo_a, intervalo_b, funcion, presicion)
    biseccion.calcularRaiz()
    biseccion.mostrarGrafica()


def puntoFijo():
    v_inicial = float(input("Introduce el valor inicial: "))
    funcion = input("Introduce la función: ")
    precision = int(input("Introduce la presicion: "))
    tolerancia = int(input("Introduce la tolerancia: "))
    subfunciones = []
    N = int(input("Introduce el número de subfunciones: "))
    for i in range(N):
        subfunciones.append(input(f"Introduce la sufunción {i+1}: "))

    puntoFijo = PuntoFijo(funcion, v_inicial, precision, tolerancia, subfunciones)
    puntoFijo.calcularRaiz()
    puntoFijo.mostrarGrafica()

def newton_Raphson():
    v_inicial = float(input("Introduce el valor inicial: "))
    presicion = int(input("Introduce la presición: "))
    funcion = input("Introduce la función: ")

    newton_raphson = NewtonRaphson(funcion, v_inicial, presicion)
    newton_raphson.calcularRaiz()
    newton_raphson.mostrarGrafica()


print("Calculadora con Métodos Numéricos :)")

while True:
    metodo = menu()
    if metodo == 1: biseccion()
    elif metodo == 2: puntoFijo()
    elif metodo == 3: newton_Raphson()
    else:
        print("Saliendo del programa :D")
        break
    print("-"*40)
    op = input("Desea continuar?\n[S] si\t[N] no\n:")
    if op == "N" or op == "n": break

print("Fin :D")