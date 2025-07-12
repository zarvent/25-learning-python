'''
SESION 2025-07-12
Complete the solution so that it reverses the string passed into it.
'world'  =>  'dlrow'
'word'   =>  'drow'
'''

# ---- FUNCIONES ----
def invertir_cadenas(string):
        textoinvertido = string[::-1]
        return textoinvertido

'''
Creamos esta funcion llamada invertir_cadenas
La variable texto invertido sera igua que la creada string, y con el slicing le daremos vuelta a las palabras
El ::-1 significa que estamos invirtiendo el string
'''


# ---- PROGRAMA ----
print(" Hola, bienvenido al invertidor de palabras 🤓 \n")
textoinvertido = input("introduce la palabra que quieres invertir: \n")

print("\n✨ ¡Listo! ✨")
print(invertir_cadenas(textoinvertido))
