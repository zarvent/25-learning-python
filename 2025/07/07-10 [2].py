# Sesion 2025-07-10
'''
Aprendido hoy:
# 'pass' es como decirle a python "no hagas nada"
# 'append' sirve para agregar un elemento al final de una lista existente en Python. Por ejemplo: mi_lista.append(4) agrega el número 4 al final de la lista mi_lista.
'''

# Creamos la funcion 'maps'
def maps(a):
    # Creamos una lista vacia
    lista_resultado = []
    # Creamos bucle for que hace que recorra cada numero de la lista
    for number in a:
        # Ahora necesitamos "guardar" el nuevo valor * 2
        lista_resultado.append(number * 2)
    return lista_resultado

