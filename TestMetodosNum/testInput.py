import sympy as sp

def evaluarFuncion(funcion, valor):
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
                "sin":sp.sin,
                "cos":sp.cos,
                "sqrt":sp.sqrt,
                "abs":sp.Abs}
    try:
        resultado = eval(funcion,contexto)
        return resultado.evalf() if isinstance(resultado, sp.Basic) else resultado
    except NameError:
        return "Error: Algo no está en el contexto :/"
    except SystemError:
        return "Error: Sintaxis no valida"
    except TypeError:
        return "Error: Valor proporcionado no es compatible con la función"


funcion = "x**2"
valor = 1

x = sp.symbols('x')
derivada = sp.diff(funcion, x)

print(f"La función {funcion} evaluada en el valor {valor} es {evaluarFuncion(funcion, valor)}")
print(f"La derivada de la funcion {funcion} es {derivada}")
print(f"La derivada {derivada} evaluada en el valor {valor} es {evaluarFuncion(str(derivada), valor)}")
