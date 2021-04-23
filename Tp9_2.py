import time

def sacar_la_contraseña():
    contasena = "admin"
    intentos = 1
    while intentos != 6:
        contrasena_de_usuario = (input("ingrese la contraseña: "))
        if contrasena_de_usuario == contasena:
            print ("felicidades, ingreso la conraseña correcta")
        else:
            print ("no esta ingresando la contraseña correcta ")
            intentos = intentos + 1
            time.sleep (1 * intentos)
            if intentos == 6:
                print ("No tiene mas intentos")


            
        
print (sacar_la_contraseña())