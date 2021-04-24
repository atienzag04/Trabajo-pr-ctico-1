

def mostrar_palabras_comienzen_con_a(palabras):
  palabras_separadas = palabras.split(' ')
  la_a = "a"
  for i in palabras_separadas:
    if str(palabras_separadas) in la_a:
      ases = palabras_separadas[i]
    else:
      ases = ""
  return ases
print(mostrar_palabras_comienzen_con_a("aloja soy"))