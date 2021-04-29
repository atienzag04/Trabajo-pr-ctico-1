'''Décimo Cuarto Ejercicio'''
import random
def juego_de_4_digitos():
    """Adivine los cuatro digitos de una funcion"""
    #Se crean las variables a utilizar
    aciertos = 0
    coincidencias = 0
    numero_random = [0, 0, 0, 0, 0]
    lista_usuario = []
    numero_usuario = str(input ("Ingrese el numero secreto: "))
    #Creo cada numero random separado, para asegurarme
    #  de que cada uno es distinto al anterior
    for i in range (0, 4):
        numero_random[i] = random.randrange(1,10)
    while numero_random[0] in [numero_random[1], numero_random[2],
     numero_random[3]]:
        numero_random[0] = random.randrange(1, 10)
    while numero_random[1] in [numero_random[2], numero_random[3]]:
        numero_random[1] = random.randrange(1,10)
    while numero_random[2] == numero_random[3]:
        numero_random[2] = random.randrange(1,10)
    #Junto cada uno de los numeros randoms
    numero_random[4] = str(str(numero_random[0]) + str(numero_random[1]) 
    + str(numero_random[2]) + str(numero_random[3]))
    while numero_usuario != numero_random[4]:
        for i in range (0,4) :
            if numero_usuario[i] == str(numero_random[i]) :
                aciertos += 1
            else :
                if numero_usuario[i] in [str(numero_random[0]), str(numero_random[1]),
                 str(numero_random[2]), str(numero_random[3])] :
                    coincidencias += 1
        print("Tiene ", aciertos, " aciertos y ", coincidencias, 
        " coincidencias.")
        numero_usuario = str(input ("Ingrese el número secreto: "))
        aciertos = 0
        coincidencias = 0
    return "Ganaste, felicidades!!!"
