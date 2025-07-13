# app.py
from flask import Flask, render_template, request

# ---- LÓGICA NÚCLEO (¡SIN CAMBIOS! ESTO ES EXCELENTE) ----
# Esta función es robusta y reutilizable, un activo de ingeniería.
def tiempo_a_milisegundos(h: int, m: int, s: int) -> int:
    """Convierte horas, minutos y segundos a milisegundos con validación de rango."""
    if not (0 <= h < 24 and 0 <= m < 60 and 0 <= s < 60):
        raise ValueError("Valores de tiempo fuera de rango.")
    return (h * 3600 + m * 60 + s) * 1000

# ---- ARQUITECTURA WEB ----
# 1. Inicialización de la aplicación Flask
app = Flask(__name__)

# 2. Definición de la ruta (endpoint) principal
@app.route('/', methods=['GET', 'POST'])
def conversor_endpoint():
    """
    Gestiona las peticiones a la raíz del sitio.
    - GET: Simplemente muestra la página con el formulario.
    - POST: Procesa los datos del formulario, calcula y muestra el resultado.
    """
    resultado = None
    error = None

    if request.method == 'POST':
        try:
            # 3. Obtener datos del formulario web. request.form es el equivalente a self.horas_var.get()
            # La conversión a 'int' es nuestra primera línea de validación.
            h = int(request.form['horas'])
            m = int(request.form['minutos'])
            s = int(request.form['segundos'])

            # 4. Llamar a nuestra lógica de negocio, igual que antes.
            resultado_ms = tiempo_a_milisegundos(h, m, s)
            resultado = f"{resultado_ms:,.0f} ms".replace(',', '.')

        except ValueError as e:
            # Captura errores de conversión (ej: "abc") o de rango de nuestra función.
            error = "Error: Introduce valores numéricos válidos y dentro del rango (h:0-23, m:0-59, s:0-59)."
        except Exception as e:
            # Buena práctica: capturar cualquier otro error inesperado.
            error = f"Ha ocurrido un error inesperado: {e}"

    # 5. Renderizar la plantilla HTML, pasándole las variables (resultado o error)
    return render_template('index.html', resultado=resultado, error=error)

# --- Punto de Entrada para Ejecución (SOLO para desarrollo local) ---
if __name__ == '__main__':
    # El modo debug recarga automáticamente el servidor al detectar cambios.
    # ¡NUNCA USAR EN PRODUCCIÓN!
    app.run(debug=True)
