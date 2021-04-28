'''Decimo segundo punto'''

def contar_vocales():
    #Creo las variables para contar las variables
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    total=0
    palabra = str(input("Ingrese la palabra a la que desea contar las vocales: "))
    for letra in palabra:
        #Busco las letras en las palabras, y las sumo en su contador
        if letra.lower() in "a":
            contador_a += 1
        if letra.lower() in "e":
            contador_e += 1
        if letra.lower() in "i":
            contador_i += 1
        if letra.lower() in "o":
            contador_o += 1
        if letra.lower() in "u":
            contador_u += 1

    return contador_a, contador_e, contador_i, contador_o, contador_u
