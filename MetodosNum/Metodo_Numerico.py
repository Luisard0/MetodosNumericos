# Clase padre de los métodos numericos
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


class Metodo_Numerico:
    """
        Clase padre principal que define algunas caracteriscas fundamentales de los método numéricos implementados.
    """
    def __init__(self, funcion):
        """
            * funcion (Str): Una expresión matematica en forma de función.
            * aproximaciones_x (float[]): Lista de aproximaciones de la raiz. Pa´la gráfica
            * aproximaciones_y (float[]): Lista de aproximaciones de la raiz evaluada en la función. Pa´la gráfica (X2)
        """
        self.funcion = funcion
        self.aproximaciones_x = []
        self.aproximaciones_y = []

    def calcularFuncion(self, funcion, valor):
        """
        Evalúa una función matemática proporcionada como cadena en un valor dado.

        Evalúa una expresión matemática en un contexto seguro que incluye funciones
        y constantes comunes de SymPy. Si el resultado es simbólico, se devuelve
        su evaluación numérica.

        :param str funcion: Función matemática como cadena (por ejemplo, "x**2 + sin(x)").
        :param float valor: Valor numérico que se asignará a la variable `x` en la función.
        :return: Resultado de la evaluación de la función.
        :rtype: float
        """
        # Posibles expresiones matematicas usadas en el input y devuletas
        contexto = {"x": valor,
                    "exp": sp.exp,
                    "log": sp.log,
                    "pi": sp.pi,
                    "sin": sp.sin,
                    "cos": sp.cos,
                    "sqrt": sp.sqrt,
                    "abs": sp.Abs}
        try:
            resultado = eval(funcion, contexto)
            return resultado.evalf() if isinstance(resultado, sp.Basic) else resultado
        except NameError:
            return "Error: Algo no está en el contexto :/"
        except SystemError:
            return "Error: Sintaxis no valida"
        except TypeError:
            return "Error: Valor proporcionado no es compatible con la función"

    def mostrarFuncion(self, aproximaciones_x, aproximaciones_y, x_label = "Aproximaciones en x", y_label = "Aproximaciones en y", subfunciones = None):
        # Muestra la gráfica de la función y subfunciones (si las tiene), las raices en la función.

        x = np.linspace(-10, 10, 400)                                           # Dominio de la función
        expresion_sympy = sp.sympify(self.funcion)
        # expresion_latex = sp.latex(expresion_sympy)
        expresion_legible = sp.pretty(expresion_sympy, use_unicode=True, wrap_line = True)

        y = np.array([self.calcularFuncion(self.funcion, valor) for valor in x]) # Linea de la función

        plt.figure(figsize=(6, 6.5))
        plt.plot(x, y, label=self.funcion)
        if subfunciones is not None:
            y = eval("x")
            plt.plot(x, y, label="y = x")
            for subfuncion in subfunciones:
                y = eval(subfuncion)
                plt.plot(x,y, label = subfuncion)
        plt.title(f"Gráfica de \n{expresion_legible}")

        plt.plot(aproximaciones_x, aproximaciones_y, 'o', color='red', label="Aproximaciones de la raíz")
        plt.axhline(0, color = 'gray', linestyle = '--')
        plt.axvline(0, color = 'gray', linestyle = '--')
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.legend()
        plt.grid(True)
        plt.show()