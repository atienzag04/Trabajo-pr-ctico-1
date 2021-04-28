'''Noveno punto'''
'''Tercera parte'''

def sacar_la_contraseña():
    #Ingreso cual es la contraseña
    contasena = "admin"
    contrasena_de_usuario = (input("ingrese la contraseña: "))
    #Utilizo el if, y la varieble bool para mostrar cual es la respuesta
    if contrasena_de_usuario == contasena:
        return "felicidades, ingreso la conraseña correcta"
        correcto = True
    else:
        correcto = False

    if correcto == True:
        return "felicidades, ingreso la conraseña correcta"
    elif correcto == False:
        return "no esta ingresando la contraseña correcta "
