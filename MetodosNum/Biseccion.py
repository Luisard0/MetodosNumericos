from MetodosNum.Metodo_Numerico import Metodo_Numerico

class Biseccion(Metodo_Numerico):
    """
        Implementa el método numérico de Bisección para encontrar raíces de funciones continuas.

        Esta clase extiende la funcionalidad de la clase base `Metodo_Numerico` y utiliza
        el método de bisección para calcular una raíz aproximada de una función en un intervalo
        dado, bajo un nivel de precisión especificado.
    """

    def __init__(self, a, b, funcion, presicion):
        """
            * a (float): Extremo inferior del intervalo inicial [a, b].
            * b (float): Extremo superior del intervalo inicial [a, b].
            * funcion (str): Función a evaluar como una cadena
            * presicion (float): Tolerancia aceptable para el error relativo.
        """
        super().__init__(funcion)
        self.a = a
        self.b = b
        self.presicion = presicion


    def calcularRaiz(self):
        # Calcula la raíz aproximada usando el método de bisección y muestra
        # los pasos iterativos, incluyendo las aproximaciones y errores.

        print("[Método: Bisección]")
        print("-" * 40)

        f_a = super().calcularFuncion(self.funcion, float(self.a))
        f_b = super().calcularFuncion(self.funcion, float(self.b))

        if self.esMismoSigno(f_a, f_b):
            print(f"A y B evaluados en la función {self.funcion} son del mismo signo")
            return

        temp = 0
        cnt = 1                                                                           # Contador
        print(f"{'Iteración ':<12}{'Raiz Aprox.':<16}{'Error':<16}")
        print("-" * 40)

        while True:
            raiz = self.calcularC(self.a, self.b)
            error = self.calcularError(temp, raiz)

            if self.presicion >= error: break

            print(f"{cnt:<10}\t{raiz:<15.8f}\t{error:<15.5f}")
            f_raiz = super().calcularFuncion(self.funcion, raiz)

            self.aproximaciones_x.append(raiz)
            self.aproximaciones_y.append(f_raiz)

            if f_raiz < 0 and f_a < 0:                                                   # Mismo signo, cambio de valores
                (self.a, temp) = (raiz, raiz)
                f_a = f_raiz
            else:
                (self.b, temp) = (raiz, raiz)
                f_b = f_raiz
            cnt += 1

    @staticmethod
    def calcularError(a, b):
        # Calcula el error relativo entre dos valores.
        return abs((b - a) / b)

    @staticmethod
    def calcularC(a, b):
        # Calcula el punto medio entre `a` y `b`.
        return (a + b) / 2

    @staticmethod
    def esMismoSigno(a, b):
        # Determina si dos valores tienen el mismo signo.
        return  (a > 0 and b> 0) or (a < 0 and b < 0)

    def mostrarGrafica(self):
        # Muestra una gráfica de las aproximaciones calculadas y los valores de la función en cada iteración.
        super().mostrarFuncion(self.aproximaciones_x, self.aproximaciones_y, "Aproximaciones de C", "f(c)")

