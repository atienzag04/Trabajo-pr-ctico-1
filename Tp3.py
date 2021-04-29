'''Tercer punto'''
def factorial ():
    """Calcular el factorial de un numero"""
    #Creo la lista a usar
    numeros_primos = []  
    numero = int(input("Ingrese el numero del que desea los factoriales: "))
    #Creo un loop, para que divida por todos los numeros hasta llegar a n
    for i in range (2, numero + 1):
        #Esto es, para que al encontrar el divisor, se agregue el numero a 
        #mi lista, y a numero lo divide por i para que ahora empieze a 
        # factoriza al número resultante
        while numero % i == 0:
            numeros_primos.append(i)
            numero = numero / i
    #Devuelvo el resultado
    return numeros_primos
