import random

def encontra_el_numero():
    numero = (random.randrange(1, 21))
    while numero < 20:
        numero_a_adivinar = int(input("ingrese el numero: "))
        if numero_a_adivinar < numero:
            print ("el numero es muy bajo")
        elif numero_a_adivinar > numero:
            print ("el numero es muy alto")
        else: 
            return ("adivino el numero, felicidades!!!!")
            
    
            
                




print(encontra_el_numero())
