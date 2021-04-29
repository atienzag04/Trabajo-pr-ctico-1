"""Decimo sexto punto"""
"""Cuarta parte"""
def encontrar_palindrome():
    """Se verifica si una palabra es palindrome"""
    palabra = str(input("Ingrese la palabra para averiguar si una palabra es palindrome: "))
    #Utilizo el lower y el replace para que las palabras 
    #se sepan mejor y sin complicaciones
    palabra = palabra.lower()
    palabra = palabra.replace(" ","")
    verificador = (palabra == palabra[::-1])
    return verificador
