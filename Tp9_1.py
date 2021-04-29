'''Noveno punto'''
'''Primera parte'''

def sacar_la_contraseña():
    """Programa para descubrir la contraseña, utilizando 5 intentos
    para limitar las veces que el usario puede usar el programa"""
    #Ingreso cual es la contraseña
    contasena = "admin"
    intentos = 5
    #Creo el while para asegurar que el numero de intenos que le quedan 
    #no es 0
    while intentos != 0:
        contrasena_de_usuario = (input("ingrese la contraseña: "))
        if contrasena_de_usuario == contasena:
            print ("felicidades, ingreso la conraseña correcta")
        else:
            print ("no esta ingresando la contraseña correcta ")
            intentos = intentos -1
            if intentos == 0:
                return ("No tiene mas intentos")
