def sacar_la_contraseña():
    contasena = "admin"
    intentos = 5
    while intentos != 0:
        contrasena_de_usuario = (input("ingrese la contraseña: "))
        if contrasena_de_usuario == contasena:
            print ("felicidades, ingreso la conraseña correcta")
        else:
            print ("no esta ingresando la contraseña correcta ")
            intentos = intentos -1
            if intentos == 0:
                print ("No tiene mas intentos")


            
        
print (sacar_la_contraseña())