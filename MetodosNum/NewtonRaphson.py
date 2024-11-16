from MetodosNum.Metodo_Numerico import Metodo_Numerico
import sympy as sp

class NewtonRaphson(Metodo_Numerico):
    """
        Implementa el método numerico de Newton-Raphson para encontrar la raiz de la función.

        Esta clase extiende la funcionalidad de la clase base `Metodo_Numerico` y utiliza
        el método de Newton-Raphson para calcular una raíz aproximada de un valor inicial dado,
        bajo un nivel de precisión especificado.
    """

    def __init__(self, funcion, v_inicial, presicion):
        """
            * funcion (String): función a evaluar como una cadena
            * v_incial (float): Valor con el que se empieza a iterar en la función
            * presición (float): Número de iteraciones para mayor presición
        """
        super().__init__(funcion)
        self.v_inicial = v_inicial
        self.presicion = presicion

    def calcularRaiz(self):
        # Calcula la raiz iterando sobre el valor inicial. Se asume que la función es continua.
        print("[Método: Newton-Raphson]")
        print("-"*40)
        x = sp.symbols('x')
        derivada_f = str(sp.diff(self.funcion, x))
        temp = self.v_inicial
        print(f"{'Iteración ':<10}  {'Raiz Aprox.':<15}{'Error':<15}")
        print("-" * 40)
        for i in range(self.presicion):
            raiz = temp - ((super().calcularFuncion(self.funcion, temp)) / (super().calcularFuncion(derivada_f, temp)))
            error = self.calcularError(temp, raiz)
            print(f"{i+1:<11}{raiz:<16.8f}{error:<16.10f}")
            self.aproximaciones_x.append(raiz)
            self.aproximaciones_y.append(super().calcularFuncion(self.funcion, raiz))
            temp = raiz

    @staticmethod
    def calcularError(a, b):
        # Calcula el error entre dos valores, entre dos raices.
        return abs(b - a)

    def mostrarGrafica(self):
        # Muestra una gráfica de las aproximaciones calculadas y los valores de la función en cada iteración.
        super().mostrarFuncion(self.aproximaciones_x, self.aproximaciones_y, "Raices de la función", "f(x)")
