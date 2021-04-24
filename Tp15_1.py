def primer_letra_por_palabra(palabras):
    palabras_separadas = palabras.split(' ')
    caracteres = ""
    for la_palabra in palabras_separadas:
        caracteres += la_palabra[0]
    return caracteres

print(primer_letra_por_palabra("viva peron"))