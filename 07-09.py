# SESION DE APRENDIZAJE 2025-07-09
# En Python, 'def' se utiliza para definir una función.
# Implementare la funcion bool_to_word
def bool_to_word(boolean):
    # analogia [imaginemos un interruptor de luz]
    # tenemos que expresar que cuando el interruptor estre prendido (osea *postivo*) diga *yes*
    # si el interrupto esta apagado (osea *false*) la funcion diga *no*
    if boolean:
        return "Yes"
    else:
        return "No"

