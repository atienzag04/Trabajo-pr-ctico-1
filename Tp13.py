"""Decimo tercer punto"""

def iguales_pero_mayusculas ():
    primera_palabra = str(input("Ingrese la primera palabra a comparar: "))
    segunda_palabra = str(input("Ingrese la segunda palabra a comparar: "))
    Resultado= bool
    #Se compara la primera palabra con la segunda
    if primera_palabra == segunda_palabra.upper():
        Resultado = True
    else:
        Resultado = False
    return Resultado 
print (iguales_pero_mayusculas())
