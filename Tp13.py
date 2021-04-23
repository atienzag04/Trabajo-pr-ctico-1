def iguales_pero_mayusculas (primerapalabra, segundapalabra):
    Resultado= bool
    if primerapalabra == segundapalabra.upper():
        Resultado = True
    else:
        Resultado = False
    return Resultado 
print (iguales_pero_mayusculas("HOLA", "hola"))
