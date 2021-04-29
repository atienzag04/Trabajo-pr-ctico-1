'''Undécima Parte'''

def revision_de_examen():
    """Calculo de apobados o desaprobados"""
    valor_centinela = ""
    alumno = 0
    #Pido las variables al usuario
    numero_de_ejercicios = int(input("Ingrese el numero de ejercicios: "))
    porcentaje = int(input("Ingrese el porcentaje por punto: "))
    cantidad_porcentaje = (numero_de_ejercicios * porcentaje)//100
    #Creo el while, para saber si aprobo o no el alumno
    #El sistema no para hasta que se escriba ok
    while valor_centinela != "ok":
        cantidad_ejercicios =  int(input("Ingrese la cantidad de ejercicios "))
        if cantidad_ejercicios >= cantidad_porcentaje:
            resultado = "aprobo"
        else: 
            resultado = "desaprobo"
        alumno += 1
        #Muestro el resultado
        print ("El alumno " + str(alumno) + " " + resultado)
        valor_centinela = str(input("Ingrese ok si desea terminar el proceso "))
    return alumno
print (revision_de_examen())
