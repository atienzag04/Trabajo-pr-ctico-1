def revision_de_examen(numero_de_ejercicios, porcentaje):
    valor_centinela = ""
    alumno = 0
    cantidad_porcentaje = (numero_de_ejercicios * porcentaje)//100
    while valor_centinela != "ok":
        cantidad_ejercicios =  int(input("Ingrese la cantidad de ejercicios "))
        if cantidad_ejercicios >= cantidad_porcentaje:
            resultado = "aprobo"
        else: 
            resultado = "desaprobo"
        alumno += 1
        print ("El alumno " + str(alumno) + " " + resultado)
        valor_centinela = str(input("Ingrese ok si desea terminar el proceso "))
    return alumno
