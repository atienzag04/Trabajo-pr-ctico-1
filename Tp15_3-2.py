def mostrar_palabras_comienzen_con_a(palabras):
  palabras_separadas = palabras.split(' ')
  la_a = "a"
  ases = ' '
  for i in palabras_separadas:
    if palabras_separadas[i].startswith("a") == True:
      ases = palabras_separadas[i]
    return ases

  return 
print(mostrar_palabras_comienzen_con_a("aloja e a"))