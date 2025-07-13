'''
----
SESSION 2025-07-13
----
El reloj muestra h horas, m minutos y s segundos después de la medianoche.

Tu tarea es escribir una función que devuelva el tiempo transcurrido desde la medianoche en milisegundos.

Ejemplo:
h = 0
m = 1
s = 1

resultado = 61000
Restricciones de entrada:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
----
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
----
Por primera vez usaré el if not en python
El operador 'not' significa que si la condición es verdadera la vuelve falsa y viceversa

En este caso sería - Si h no está entre 0 y 24 entonces... o sea if not(0 <= h <= 24)
Quiero decir que si h es menor o igual a 24, está correcto; si m es menor o igual a 60, también está correcto; y si s es menor o igual a 60, igualmente está correcto.

if not
Si [] no está entre []
entonces
----
'''

def past(h, m, s):
    # Validación de rangos
    if not (0 <= h <= 24 and 0 <= m <= 59 and 0 <= s <= 59):
        raise ValueError("Introduce un valor válido, h debe estar entre 0 y 24, m entre 0 y 59, s entre 0 y 59")

    # Definimos las constantes de conversión
    milisegundos_por_segundo = 1000
    milisegundos_por_minuto = 60 * milisegundos_por_segundo  # 60,000
    milisegundos_por_hora = 60 * milisegundos_por_minuto     # 3,600,000

    # Sumatoria Total
    total_milisegundos = (h * milisegundos_por_hora) + (m * milisegundos_por_minuto) + (s * milisegundos_por_segundo)
    return total_milisegundos


