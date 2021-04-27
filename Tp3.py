'''Tercer punto'''
print ("Calcular el factorial de un numero")
def factorial (n):
    #Creo la lista a usar
    numeros_primos = []    
    for i in range (2, n + 1):
        while n % i == 0:
            numeros_primos.append(i)
            n = n / i
    return numeros_primos
print (factorial(8))
