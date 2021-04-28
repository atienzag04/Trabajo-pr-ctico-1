'''Octavo punto'''
print ("Pasar numeros enteros a romanos")
def conversion_entero_romano():
    #Creo las listas para almacenar los numeros
    numeros = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerales = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    numeral = ''
    i = 0
    entero = int(input("Ingrese el año a pasar a romanos: "))
    #Calculo un while para calcular los numeros en romano
    while entero > 0:
        for fechas in range(entero // numeros[i]):
            numeral += numerales[i]
            entero -= numeros[i]
        i += 1
    return numeral
print(conversion_entero_romano()) 
