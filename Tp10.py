'''Decimo punto'''

import random

def encontra_el_numero():
    """Funcion para averiguar el numero, entre 1 y 20, mostrando si el 
    intento es mayor o menor"""
    #Calculo el numero random
    numero = (random.randrange(1, 21))
    #Utilizo el while, para saber si el numero es mayor o menor 
    #al numero correcto
    while numero < 20:
        numero_a_adivinar = int(input("ingrese el numero: "))
        if numero_a_adivinar < numero:
            print ("el numero es muy bajo")
        elif numero_a_adivinar > numero:
            print ("el numero es muy alto")
        else: 
            return ("adivino el numero, felicidades!!!!")
