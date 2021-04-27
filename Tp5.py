'''Quinta punto'''
print("Tabla de comparacion farenheit-celsius")
def defahacel():
    #Creo las listas
    farenheit = []
    celsius = []
    i = 0
    #Creo un bucle que va a agregar números de 0 a 120 a farenheit
    while i <= 120:
        farenheit.append(i)
        i = i + 10
    i = 0
    #creo un bucle que usalos numeros en farenheit por órden
    # guardandolos en celsuis en su respectivo lugar
    while i <= 12:
        numcelsius = (farenheit[i] - 32) / (9 / 5)
        celsius.append(numcelsius)
        i = i + 1
    return farenheit, celsius
print (defahacel())
