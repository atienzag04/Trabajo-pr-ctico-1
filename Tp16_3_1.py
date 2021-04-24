def remplazar_vocal_por_la_siguiente():

    frase = str(input("Ingrese la palabra que desea reemplazar las vocales por la siguiente vocal: "))
    frase = frase.replace("u","a")
    frase = frase.replace("o","u")
    frase = frase.replace("i","o")
    frase = frase.replace("e","i")
    frase = frase.replace("a","e") 
 
    return frase
 
print(remplazar_vocal_por_la_siguiente())
