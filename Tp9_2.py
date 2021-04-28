'''Noveno punto'''
'''Segunda parte'''

import time

def sacar_la_contraseña():
    #Ingreso cual es la contraseña
    contasena = "admin"
    intentos = 1
    #Creo el while para asegurar que el numero de intenos que le quedan 
    #no es 6
    while intentos != 6:
        contrasena_de_usuario = (input("ingrese la contraseña: "))
        if contrasena_de_usuario == contasena:
            print ("felicidades, ingreso la conraseña correcta")
        else:
            print ("no esta ingresando la contraseña correcta ")
            #uso el time.sleep para hacer que cada vez pase mas tiempo entre
            #cada intento
            intentos = intentos + 1
            (time.sleep (1 * intentos))
            if intentos == 6:
                return ("No tiene mas intentos")
