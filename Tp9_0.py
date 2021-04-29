'''Noveno punto'''
'''Parte 0'''

def sacar_la_contraseña():
    """Programa para descubrir la contraseña"""
    #Ingreso cual es la contraseña
    contasena = "admin"
    contrasena_de_usuario = (input("ingrese la contraseña: "))
    #Creo un if para saber si la contraseña es correcta
    if contrasena_de_usuario == contasena:
        return "felicidades, ingreso la conraseña correcta"
    else:
        return "no esta ingresando la contraseña correcta "
