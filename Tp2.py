from math import pi
from math import sqrt

def perimetro_rectangulo ():
    #Pido las medidas del rectangulo
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingresa la altura: "))
    #Calculo el perimetro
    calculo_perimetro = ((base * 2)+(altura * 2))
    return  calculo_perimetro

def area_rectangulo ():
    #Pido las medidas del rectangulo
    base = int(input("Ingrese la base: "))
    altura = int(input("Ingresa la altura: "))
    #Calculo el area
    calculo_area = (base * altura)
    return calculo_area

def area_rectangulo_en_cordenadas ():
    #Pido las medidas del rectangulo
    x1 = int(input("Ingrese la primera cordenada en x: ")) 
    x2 = int(input("Ingrese la segunda cordenada en x: "))
    y1 = int(input("Ingrese la primera cordenada en y: "))
    y2 = int(input("Ingrese la segunda cordenada en y: "))
    #Calculo el area 
    #El uso de abs, es para permitir el uso de cordenadas negativas
    calculo_area_cordenadas = ((abs(x2) - abs(x1)) * (abs(y2) - abs(y1)))
    return calculo_area_cordenadas

def perimetro_circulo ():
    #Pido el radio del circulo
    radio = int(input("Ingrese el radio del circulo: "))
    #Calculo el perimetro del circulo
    calculo_perimetro_circulo = (2 * pi * radio)
    return calculo_perimetro_circulo

def area_circulo ():
    #Pido el radio del circulo
    radio = int(input("Ingrese el radio del circulo: "))
    calculo_area_circulo = (pi * radio **2) 
    #tambien se podria, multiplicar al radio por si mismo 
    return calculo_area_circulo

def volumen_esfera ():
    #Pido el radio de la esfera
    radio = int(input("Ingrese el radio de la esfera: "))
    calculo_volumen_esfera = ((4/3) * pi * radio **3)
    return calculo_volumen_esfera

def hipotenusa_de_triangulo_rectangulo ():
    #Pido los catetos
    cateto1 = int(input("Ingrese el primer cateto: "))
    cateto2 = int(input("Ingrese el segundo cateto: "))
    calculo_hipotenusa = sqrt ((cateto1 **2)+(cateto2 **2))
    return calculo_hipotenusa
