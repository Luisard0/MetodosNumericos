import sympy as sp
from MetodosNum.Metodo_Numerico import Metodo_Numerico

class PuntoFijo(Metodo_Numerico):
    """
        Implementa el método numérico de Punto fijo para encontrar raíces de funciones.

        Esta clase extiende la funcionalidad de la clase base `Metodo_Numerico` y utiliza
        el método de Punto fijo para calcular las raices aproximadas de una función.
        Utiliza cada subfunción proporcionada para verificar si es convergente de acuerdo a una tolerancia.
        Para cada subfunción se calcula su raiz aproximada, siempre que sea convergente.
    """

    def __init__(self, funcion, v_inicial, presicion, tolerancia, subfunciones):
        """
            * funcion (str): Función original de la que se desprenden las subfunciones.
            * v_inicial (float): Valor inicial desde donde empiezan las iteraciones.
            * presicion (int): Interaciones para la presición de la raiz de la subfunión.
            * tolerancia (int): Tolerancia para la convergencia de la subfunción. Iteraciones para encontrar la convergencia.
            * subfunciones (str[]): Lista de subfuniones de la funión original.
        """
        super().__init__(funcion)
        self.v_inicial = v_inicial
        self.sub_funciones = subfunciones
        self.presicion = presicion
        self.tolerancia = tolerancia


    def esConvergente(self, subfuncion):
        # Determina si la subfunción es convegente de acuerdo a la tolerancia.
        x = sp.symbols('x')
        g_prima = str(sp.diff(subfuncion, x))
        flag = False
        v_temp = self.v_inicial
        for _ in range(self.tolerancia):
            temp = abs(super().calcularFuncion(g_prima, v_temp))
            flag = temp < 1
            if flag: break
            v_temp = temp
        return flag                                                 # Ultimo valor de la flag


    def calcularRaiz(self):
        # Calcula la raiz de la subfunción de acuerdo a su convergencia.

        print("[Método: Punto fijo]")
        print("-" * 40)

        for subF in self.sub_funciones:
            if not self.esConvergente(subF):
                print(f"La función {subF} no es convergente")
                continue

            print(f"Función: {subF}\nRaíz 0: {self.v_inicial}")
            raiz = self.v_inicial

            for i in range(self.presicion):
                temp = super().calcularFuncion(subF, raiz)

                self.aproximaciones_x.append(raiz)
                self.aproximaciones_y.append(super().calcularFuncion(self.funcion,raiz))

                print(f"Raíz {i + 1:<2}: {temp:<10.5f}  |  Error: {self.calcularError(raiz, temp):<10.5f}")
                raiz = temp

            print("\n")   # pa´que no se junten


    @staticmethod
    def calcularError(a, b):
        # Calcula el error entre raices.
        return abs(b -a)

    def mostrarGrafica(self):
        # Muestra una gráfica de las aproximaciones calculadas para las subfunciones
        super().mostrarFuncion(self.aproximaciones_x,self.aproximaciones_y, "Raices", "f(x)", self.sub_funciones)



