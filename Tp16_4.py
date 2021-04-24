def encontrar_palindrome(palabra):
    palabra = palabra.replace(" ","")
    verificador = (palabra == palabra[::-1])
    return verificador
