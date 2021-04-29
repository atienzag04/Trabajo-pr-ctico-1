"""Decimo septimo punto"""
"""Primera parte"""
def procesamiento_de_telegramas():
    """Se acortan las palabras de 5 letras, ademas de agregarles
    el @ al final. A todas las palabras ingresadas se les cuenta
    el precio"""
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
