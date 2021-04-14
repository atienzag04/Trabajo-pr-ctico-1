def factorial (n):

    numeros_primos = []
    
    for i in range (2, n + 1):
        
        while n % i == 0:
            numeros_primos.append(i)
            n = n / i
    
    return numeros_primos
