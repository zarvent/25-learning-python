'''
Importamos el módulo 'tkinter' y le damos el alias 'tk'.
 'tkinter' es una biblioteca estándar de Python que permite crear interfaces gráficas (ventanas, botones, etc.).
 Al usar 'as tk', podemos escribir 'tk.Algo' en vez de 'tkinter.Algo', haciendo el código más corto y fácil de leer.
 Usamos ttk para widgets con un aspecto más moderno
'''

# Importamos la biblioteca principal de interfaces gráficas y le damos el alias 'tk'
import tkinter as tk
# Importamos 'ttk', un submódulo de tkinter que ofrece widgets con mejor apariencia
from tkinter import ttk

# ---- LOGICA NUCLEO ----
# Definimos una función que convierte horas, minutos y segundos a milisegundos
# h: horas (int), m: minutos (int), s: segundos (int)
def tiempo_a_milisegundos(h:int, m:int, s:int) -> int:
    # Validamos que los valores estén en el rango correcto
    if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
        raise ValueError("Valores fuera de rango.")  # Si no, lanzamos un error
    # Calculamos el total de milisegundos y lo devolvemos
    return (h * 3600 + m * 60 + s) * 1000

# ---- APLICACION GUI ----
# Creamos una clase para la aplicación, que hereda de la ventana principal de tkinter
class ConversorApp(tk.Tk):
    def __init__(self):
        # Inicializamos la ventana principal
        super().__init__()
        # Título de la ventana
        self.title("Conversor de Tiempo")
        # Tamaño de la ventana
        self.geometry("400x350")
        # No permitir cambiar el tamaño
        self.resizable(False, False)

        # Estilos visuales para los widgets
        style = ttk.Style(self)
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12, "bold"))
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))
        style.configure("Result.TLabel", font=("Helvetica", 14), background="lightgreen", borderwidth=5, relief="ridge", padding=10)
        style.configure("Error.TLabel", font=("Helvetica", 14), background="lightcoral", borderwidth=5, relief="ridge", padding=10)

        # Creamos el marco principal con padding
        main_frame = ttk.Frame(self, padding= "20 20 20 20")
        main_frame.pack(expand=True, fill="both")

        # Títulos de la app
        ttk.Label(main_frame, text="Conversor a Milisegundos", style="Header.TLabel").pack(pady=(0, 5))
        ttk.Label(main_frame, text="Introduce un tiempo para calcular").pack(pady=(0, 20))

        # Formulario de entrada de datos
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(pady=10)

        # Etiqueta y campo para horas
        ttk.Label(form_frame, text="Horas (h):").grid(row=0, column=0, sticky="w", padx=5)
        self.horas_var = tk.StringVar()  # Variable para guardar el valor ingresado
        ttk.Entry(form_frame, textvariable=self.horas_var, width=10).grid(row=0, column=1, padx=5)

        # Etiqueta y campo para minutos
        ttk.Label(form_frame, text="Minutos (m):").grid(row=1, column=0, sticky="w", padx=5)
        self.minutos_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.minutos_var, width=10).grid(row=1, column=1, padx=5)

        # Etiqueta y campo para segundos
        ttk.Label(form_frame, text="Segundos (s):").grid(row=2, column=0, sticky="w", padx=5)
        self.segundos_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.segundos_var, width=10).grid(row=2, column=1, padx=5)

        # Botón para calcular el resultado
        ttk.Button(main_frame, text="Calcular", command=self.calcular_y_mostrar, style="TButton").pack(pady=20)

        # Etiqueta donde se mostrará el resultado o el error
        self.resultado_label = ttk.Label(main_frame, text="", anchor="center")
        self.resultado_label.pack(fill="x", ipady=5)

    def calcular_y_mostrar(self):
        """
        Esta función se ejecuta cuando el usuario presiona el botón "Calcular".
        Obtiene los datos del formulario, los valida, llama a la función de conversión y muestra el resultado.
        """
        try:
            # Obtenemos los valores ingresados y los convertimos a enteros
            h = int(self.horas_var.get())
            m = int(self.minutos_var.get())
            s = int(self.segundos_var.get())

            # Llamamos a la función de conversión
            resultado_ms = tiempo_a_milisegundos(h, m, s)

            # Formateamos el resultado para mostrarlo bonito
            resultado_formateado = f"Resultado:\n{resultado_ms:,.0f} ms".replace(',', '.')
            self.resultado_label.config(text=resultado_formateado, style="Result.TLabel")

        except ValueError:
            # Si hay un error (por ejemplo, texto en vez de número), mostramos un mensaje de error
            self.resultado_label.config(text="Error:\nIntroduce valores numéricos válidos.", style="Error.TLabel")
        except Exception as e:
            # Capturamos cualquier otro error inesperado
            self.resultado_label.config(text=f"Error inesperado:\n{e}", style="Error.TLabel")


# --- Punto de Entrada de la Aplicación ---
# Este bloque se ejecuta solo si el archivo se corre directamente (no si se importa como módulo)
if __name__ == "__main__":
    # Creamos una instancia de la aplicación
    app = ConversorApp()
    # Iniciamos el bucle principal de la interfaz gráfica
    app.mainloop()
