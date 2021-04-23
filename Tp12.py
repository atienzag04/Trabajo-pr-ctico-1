def contar_vocales(palabra):
    contador_a = 0
    contador_e = 0
    contador_i = 0
    contador_o = 0
    contador_u = 0
    total=0
    for letra in palabra:
        if letra.lower() in "a":
            contador_a += 1
        if letra.lower() in "e":
            contador_e += 1
        if letra.lower() in "i":
            contador_i += 1
        if letra.lower() in "o":
            contador_o += 1
        if letra.lower() in "u":
            contador_u += 1
            
    return contador_a, contador_e, contador_i, contador_o, contador_u


print (contar_vocales("holla"))