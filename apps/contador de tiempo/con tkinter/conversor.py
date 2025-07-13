'''
Importamos el módulo 'tkinter' y le damos el alias 'tk'.
 'tkinter' es una biblioteca estándar de Python que permite crear interfaces gráficas (ventanas, botones, etc.).
 Al usar 'as tk', podemos escribir 'tk.Algo' en vez de 'tkinter.Algo', haciendo el código más corto y fácil de leer.
 Usamos ttk para widgets con un aspecto más moderno
'''

import tkinter as tk
from tkinter import ttk

# ---- LOGICA NUCLEO ----
def tiempo_a_milisegundos(h:int, m:int, s:int) -> int:
    if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
        raise ValueError("Valores fuera de rango.")
    return (h * 3600 + m * 60 + s) * 1000

# ---- APLICACION GUI ----
class ConversorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        # Configuración de la ventana principal
        self.title("Conversor de Tiempo")
        self.geometry("400x350")
        self.resizable(False, False)

        # Estilos
        style = ttk.Style(self)
        style.configure("TLabel", font=("Helvetica", 12))
        style.configure("TButton", font=("Helvetica", 12, "bold"))
        style.configure("TEntry", font=("Helvetica", 12))
        style.configure("Header.TLabel", font=("Helvetica", 16, "bold"))
        style.configure("Result.TLabel", font=("Helvetica", 14), background="lightgreen", borderwidth=5, relief="ridge", padding=10)
        style.configure("Error.TLabel", font=("Helvetica", 14), background="lightcoral", borderwidth=5, relief="ridge", padding=10)

        # Widgets
        main_frame = ttk.Frame(self, padding= "20 20 20 20")
        main_frame.pack(expand=True, fill="both")

        # Títulos
        ttk.Label(main_frame, text="Conversor a Milisegundos", style="Header.TLabel").pack(pady=(0, 5))
        ttk.Label(main_frame, text="Introduce un tiempo para calcular").pack(pady=(0, 20))

        # Formulario de entrada
        form_frame = ttk.Frame(main_frame)
        form_frame.pack(pady=10)

        ttk.Label(form_frame, text="Horas (h):").grid(row=0, column=0, sticky="w", padx=5)
        self.horas_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.horas_var, width=10).grid(row=0, column=1, padx=5)

        ttk.Label(form_frame, text="Minutos (m):").grid(row=1, column=0, sticky="w", padx=5)
        self.minutos_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.minutos_var, width=10).grid(row=1, column=1, padx=5)

        ttk.Label(form_frame, text="Segundos (s):").grid(row=2, column=0, sticky="w", padx=5)
        self.segundos_var = tk.StringVar()
        ttk.Entry(form_frame, textvariable=self.segundos_var, width=10).grid(row=2, column=1, padx=5)

        # Botón de Cálculo
        ttk.Button(main_frame, text="Calcular", command=self.calcular_y_mostrar, style="TButton").pack(pady=20)

        # Etiqueta de Resultado
        self.resultado_label = ttk.Label(main_frame, text="", anchor="center")
        self.resultado_label.pack(fill="x", ipady=5)

    def calcular_y_mostrar(self):
        """
        Función callback: se ejecuta al presionar el botón.
        Obtiene los datos, los valida, llama a la lógica y muestra el resultado.
        """
        try:
            # 1. Obtener y convertir datos de la GUI. Puede lanzar ValueError si no son números.
            h = int(self.horas_var.get())
            m = int(self.minutos_var.get())
            s = int(self.segundos_var.get())

            # 2. Llamar a nuestra lógica de negocio robusta. Puede lanzar ValueError por rangos.
            resultado_ms = tiempo_a_milisegundos(h, m, s)

            # 3. Formatear y mostrar el resultado exitoso
            resultado_formateado = f"Resultado:\n{resultado_ms:,.0f} ms".replace(',', '.')
            self.resultado_label.config(text=resultado_formateado, style="Result.TLabel")

        except ValueError:
            # 4. Capturar CUALQUIER error de valor (conversión o rango) y mostrar un mensaje amigable
            self.resultado_label.config(text="Error:\nIntroduce valores numéricos válidos.", style="Error.TLabel")
        except Exception as e:
            # Captura de errores inesperados (buena práctica)
            self.resultado_label.config(text=f"Error inesperado:\n{e}", style="Error.TLabel")


# --- Punto de Entrada de la Aplicación ---
if __name__ == "__main__":
    app = ConversorApp()
    app.mainloop()
