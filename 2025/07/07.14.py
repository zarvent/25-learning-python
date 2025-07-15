'''
Escriba una función que acepte una matriz de 10 números enteros (entre 0 y 9), que devuelva una cadena de esos números en forma de número de teléfono.

    Ejemplo
    create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
    El formato devuelto debe ser correcto para poder completar este desafío.

    ¡No olvides el espacio después de los paréntesis de cierre!
----
def create_phone_number(n):
Validacion de entrada, el input tiene que ser 10 numeros enteros entre 0 y 9

Guardar los primeros tres numeros como prefijo [PARTE 1]
Guardar la segunda parte -> numero 456-
Guardar la tercera y ultima parte -> numero 7890
Meter todo en una misma caja llamada numero-final

----
Con 'len' se puede verificar los caracteres introducidos
Con 'isdigit' se puede verificar que los caracteres introducidos son digitos
----
'''

def create_phone_number(n):
    # Validación de tipo
    if not isinstance(n, list):
        raise TypeError("Input invalido")
    # Validación de longitud
    if len(n) != 10:
        raise ValueError("La lista debe tener exactamente 10 dígitos")
    # Validación de cada dígito
    for digit in n:
        if not isinstance(digit, int) or not (0 <= digit <= 9):
            raise ValueError("Debe ser entero entre 0 y 9")

    # Guardamos las 3 "cajas"
    p1 = ''.join(str(d) for d in n[0:3])
    p2 = ''.join(str(d) for d in n[3:6])
    p3 = ''.join(str(d) for d in n[6:])  # Tomar los últimos 4 dígitos
    return f"({p1}) {p2}-{p3}"

'''
    numero_final = "("primera_parte")" segunda_parte"-"tercera_parte
'''
