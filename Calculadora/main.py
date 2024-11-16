import tkinter as tk
from tkinter import ttk, messagebox
from MetodosNum.NewtonRaphson import NewtonRaphson
from MetodosNum.Biseccion import Biseccion
from MetodosNum.PuntoFijo import PuntoFijo
"""
Menú pero con interfaz gráfica que permite al usuario seleccionar entre los métodos de Bisección, Punto Fijo 
y Newton-Raphson para encontrar raíces de funciones continuas. Proporciona entradas dinámicas 
según el método seleccionado y muestra gráficas de los resultados.

Módulos Importados:
* tkinter: Biblioteca para crear interfaces gráficas.
* ttk: Extensión de tkinter para widgets avanzados.
* messagebox: Módulo de tkinter para mostrar mensajes emergentes.

Funciones:
* ejecutar_biseccion():
    Ejecuta el método de Bisección utilizando los valores ingresados por el usuario.
    Muestra una gráfica con los resultados y mensajes de éxito o error.

* ejecutar_punto_fijo():
    Ejecuta el método de Punto Fijo utilizando los valores ingresados y subfunciones definidas dinámicamente.
    Muestra una gráfica con los resultados y mensajes de éxito o error.

* ejecutar_newton_raphson():
    Ejecuta el método de Newton-Raphson utilizando los valores ingresados por el usuario.
    Muestra una gráfica con los resultados y mensajes de éxito o error.

* cambiar_metodo(event):
    Actualiza dinámicamente las entradas de la interfaz gráfica según el método numérico seleccionado.

"""
# Variables globales para las entradas
entry_a = entry_b = entry_tol = entry_funcion = entry_inicial = entry_precision = entry_subfunciones = None
entry_subfunciones_list = []

# Función para manejar el método Bisección
def ejecutar_biseccion():
    """
        Ejecuta el método de Bisección con los valores ingresados en la interfaz.

        Llama a la clase `Biseccion` para calcular la raíz de la función en el intervalo definido
        y muestra los resultados en una gráfica.

        Muestra un mensaje de éxito o error al finalizar la ejecución.

        :raises Exception: Si ocurre un error durante la ejecución del método.
    """
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        tolerancia = float(entry_tol.get())
        funcion = entry_funcion.get()

        biseccion = Biseccion(a, b, funcion, tolerancia)
        biseccion.calcularRaiz()
        biseccion.mostrarGrafica()

        messagebox.showinfo("Éxito", "El método Bisección se ejecutó correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error ejecutando Bisección: {e}")

# Función para manejar el método Punto Fijo
def ejecutar_punto_fijo():
    """
        Ejecuta el método de Punto Fijo con los valores ingresados en la interfaz.

        Llama a la clase `PuntoFijo` para calcular la raíz de la función usando subfunciones definidas
        dinámicamente por el usuario y muestra los resultados en una gráfica.

        Muestra un mensaje de éxito o error al finalizar la ejecución.

        :raises Exception: Si ocurre un error durante la ejecución del método.
    """
    try:
        v_inicial = float(entry_inicial.get())
        funcion = entry_funcion.get()
        precision = int(entry_precision.get())
        tolerancia = int(entry_tol.get())
        N = int(entry_subfunciones.get())

        # Obtener subfunciones dinámicamente
        subfunciones = [entry_subfunciones_list[i].get() for i in range(N)]

        punto_fijo = PuntoFijo(funcion, v_inicial, precision, tolerancia, subfunciones)
        punto_fijo.calcularRaiz()
        punto_fijo.mostrarGrafica()

        messagebox.showinfo("Éxito", "El método Punto Fijo se ejecutó correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error ejecutando Punto Fijo: {e}")

# Función para manejar el método Newton-Raphson
def ejecutar_newton_raphson():
    """
       Ejecuta el método de Newton-Raphson con los valores ingresados en la interfaz.

       Llama a la clase `NewtonRaphson` para calcular la raíz de la función y muestra
       los resultados en una gráfica.

       Muestra un mensaje de éxito o error al finalizar la ejecución.

       :raises Exception: Si ocurre un error durante la ejecución del método.
    """
    try:
        v_inicial = float(entry_inicial.get())
        funcion = entry_funcion.get()
        precision = int(entry_precision.get())

        newton_raphson = NewtonRaphson(funcion, v_inicial, precision)
        newton_raphson.calcularRaiz()
        newton_raphson.mostrarGrafica()

        messagebox.showinfo("Éxito", "El método Newton-Raphson se ejecutó correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error ejecutando Newton-Raphson: {e}")

# Función para actualizar los elementos de entrada según el método seleccionado
def cambiar_metodo(event):
    """
        Actualiza dinámicamente los elementos de entrada según el método seleccionado en el menú.

        Borra los widgets existentes y crea nuevos campos de entrada para Bisección, Punto Fijo
        o Newton-Raphson, según corresponda.

        :param event: Evento generado por la selección en el menú desplegable.
    """
    metodo = metodo_var.get()

    # Limpiar los widgets actuales en frame_inputs
    for widget in frame_inputs.winfo_children():
        widget.destroy()

    global entry_a, entry_b, entry_tol, entry_funcion, entry_inicial, entry_precision, entry_subfunciones, entry_subfunciones_list

    if metodo == "Bisección":
        # Bisección
        entry_a = tk.Entry(frame_inputs)
        entry_b = tk.Entry(frame_inputs)
        entry_tol = tk.Entry(frame_inputs)
        entry_funcion = tk.Entry(frame_inputs)

        tk.Label(frame_inputs, text="Intervalo A:").grid(row=0, column=0, pady=5)
        entry_a.grid(row=0, column=1, pady=5)

        tk.Label(frame_inputs, text="Intervalo B:").grid(row=1, column=0, pady=5)
        entry_b.grid(row=1, column=1, pady=5)

        tk.Label(frame_inputs, text="Tolerancia:").grid(row=2, column=0, pady=5)
        entry_tol.grid(row=2, column=1, pady=5)

        tk.Label(frame_inputs, text="Función:").grid(row=3, column=0, pady=5)
        entry_funcion.grid(row=3, column=1, pady=5)

        tk.Button(frame_inputs, text="Ejecutar Bisección", command=ejecutar_biseccion).grid(row=4, columnspan=2, pady=10)

    elif metodo == "Punto Fijo":
        # Punto Fijo
        entry_inicial = tk.Entry(frame_inputs)
        entry_funcion = tk.Entry(frame_inputs)
        entry_precision = tk.Entry(frame_inputs)
        entry_tol = tk.Entry(frame_inputs)
        entry_subfunciones = tk.Entry(frame_inputs)

        tk.Label(frame_inputs, text="Valor inicial:").grid(row=0, column=0, pady=5)
        entry_inicial.grid(row=0, column=1, pady=5)

        tk.Label(frame_inputs, text="Función:").grid(row=1, column=0, pady=5)
        entry_funcion.grid(row=1, column=1, pady=5)

        tk.Label(frame_inputs, text="Precisión:").grid(row=2, column=0, pady=5)
        entry_precision.grid(row=2, column=1, pady=5)

        tk.Label(frame_inputs, text="Tolerancia:").grid(row=3, column=0, pady=5)
        entry_tol.grid(row=3, column=1, pady=5)

        tk.Label(frame_inputs, text="Número de subfunciones:").grid(row=4, column=0, pady=5)
        entry_subfunciones.grid(row=4, column=1, pady=5)

        def generar_subfunciones():
            for widget in frame_inputs.grid_slaves():
                if int(widget.grid_info()["row"]) > 4:
                    widget.destroy()

            global entry_subfunciones_list
            entry_subfunciones_list = []
            for i in range(int(entry_subfunciones.get())):
                tk.Label(frame_inputs, text=f"Subfunción {i + 1}:").grid(row=5 + i, column=0, pady=5)
                entry = tk.Entry(frame_inputs)
                entry.grid(row=5 + i, column=1, pady=5)
                entry_subfunciones_list.append(entry)

            # Botón para ejecutar Punto Fijo
            tk.Button(frame_inputs, text="Ejecutar Punto Fijo", command=ejecutar_punto_fijo).grid(
                row=5 + int(entry_subfunciones.get()), columnspan=2, pady=10
            )

        tk.Button(frame_inputs, text="Generar subfunciones", command=generar_subfunciones).grid(row=5, columnspan=2, pady=10)

    elif metodo == "Newton-Raphson":
        # Newton-Raphson
        entry_inicial = tk.Entry(frame_inputs)
        entry_funcion = tk.Entry(frame_inputs)
        entry_precision = tk.Entry(frame_inputs)

        tk.Label(frame_inputs, text="Valor inicial:").grid(row=0, column=0, pady=5)
        entry_inicial.grid(row=0, column=1, pady=5)

        tk.Label(frame_inputs, text="Función:").grid(row=1, column=0, pady=5)
        entry_funcion.grid(row=1, column=1, pady=5)

        tk.Label(frame_inputs, text="Precisión:").grid(row=2, column=0, pady=5)
        entry_precision.grid(row=2, column=1, pady=5)

        tk.Button(frame_inputs, text="Ejecutar Newton-Raphson", command=ejecutar_newton_raphson).grid(row=3, columnspan=2, pady=10)

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora de Métodos Numéricos")
root.geometry("400x500")

# Selección de método
tk.Label(root, text="Selecciona un método:", font=("Arial", 12)).pack(pady=10)
metodo_var = tk.StringVar()
metodo_menu = ttk.Combobox(root, textvariable=metodo_var, values=["Bisección", "Punto Fijo", "Newton-Raphson"])
metodo_menu.bind("<<ComboboxSelected>>", cambiar_metodo)
metodo_menu.pack()

# Frame para las entradas dinámicas
frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=20)

# Inicia el bucle de Tkinter
root.mainloop()
