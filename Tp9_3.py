def sacar_la_contraseña():
    contasena = "admin"
    contrasena_de_usuario = (input("ingrese la contraseña: "))
    if contrasena_de_usuario == contasena:
        return "felicidades, ingreso la conraseña correcta"
        correcto = True
    else:
        correcto = False

    if correcto == True:
        return "felicidades, ingreso la conraseña correcta"
    elif correcto == False:
        return "no esta ingresando la contraseña correcta "




print (sacar_la_contraseña())