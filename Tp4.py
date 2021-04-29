'''Cuarta punto'''
def fahrenheit_a_celsius():
    """Pasar grados de celsius a fahrenheit"""
    #Pido los grados en fahrenheit
    grados_fahrenheit = int(input("Ingrese los grados en Fahrenheit: "))
    #Calculo el valor en Celsius
    celsius = (grados_fahrenheit - 32) * (5/9)
    #Muestro el resultado
    return celsius
print (fahrenheit_a_celsius())
