"""Decimo quinto punto"""
"""Primera parte"""
def primer_letra_por_palabra():
    """Muestra las palaras iniciales de la frase a ingresar"""
    palabras = str(input("Ingrese la frase que desea mostrar las iniciales: "))
    #Separo cada palabra en palabras_separadas
    palabras_separadas = palabras.split(' ')
    caracteres = ""
    #Utilizo el for para que se guarde cada inicial
    for la_palabra in palabras_separadas:
        caracteres += la_palabra[0]
    return caracteres

