# SEGUNDA SESION DE APRENDIZAJE 2025-07-09
# DNA to RNA Conversion

# Creamos la funcion dna_to_rna
def dna_to_rna(dna): # dna es el punto de partida, el codigo original que transforaemos a rna

    # Usare .replace > .replace('valor original', 'valor por el que sera cambiado')
    # En este ejercicio solo queremos cambiar "GCAT" a "GCAU"
    # rna es el valor igual a
    rna = dna.replace('T', 'U')

    # "python devolveme el valor rna"
    return rna

'''
Deoxyribonucleic acid, DNA is the primary information storage molecule in biological systems. It is composed of four nucleic acid bases Guanine ('G'), Cytosine ('C'), Adenine ('A'), and Thymine ('T').

Ribonucleic acid, RNA, is the primary messenger molecule in cells. RNA differs slightly from DNA its chemical structure and contains no Thymine. In RNA Thymine is replaced by another nucleic acid Uracil ('U').

Create a function which translates a given DNA string into RNA.

For example:

"GCAT"  =>  "GCAU"
The input string can be of arbitrary length - in particular, it may be empty. All input is guaranteed to be valid, i.e. each input string will only ever consist of 'G', 'C', 'A' and/or 'T'.
'''
