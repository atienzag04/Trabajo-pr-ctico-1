'''Tercer punto'''
def factorial (n):
    """Calcular el factorial de un numero"""
    #Creo la lista a usar
    numeros_primos = []  
    #Creo un loop, para que divida por todos los numeros hasta llegar a n
    for i in range (2, n + 1):
        #Esto es, para que al encontrar el divisor, se agregue el numero a 
        #mi lista, y a n lo divide por i para que ahora empieze a factoriza 
        # al número resultante
        while n % i == 0:
            numeros_primos.append(i)
            n = n / i
    #Devuelvo el resultado
    return numeros_primos
print (factorial(8))
