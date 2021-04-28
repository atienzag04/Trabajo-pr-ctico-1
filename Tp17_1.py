def procesamiento_de_telegramas():
    palabra_lista = []
    valor_palabra = 0
    resultado = ' '
    palabra_lista = str(input("Ingrese la palabra: ")).split(' ')
    for i in range(0, len(palabra_lista)):
        if ((len(palabra_lista[i])) > 5):
            palabra_lista[i] = palabra_lista[i][0:5]
            palabra_lista[i] = palabra_lista[i] + "@"
            valor_palabra = valor_palabra + 0.55
            resultado += palabra_lista[i] + " "
        elif ((len(palabra_lista[i])) <= 5):
            valor_palabra = valor_palabra + 0.35 
            resultado += palabra_lista[i] + " "
    return resultado, valor_palabra
print(procesamiento_de_telegramas())