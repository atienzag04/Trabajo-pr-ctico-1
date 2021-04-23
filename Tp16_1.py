def removerVocales(palabra):
  letras = []
  for caracter in palabra:
    if caracter.lower() not in 'aeiou':
      letras.append(caracter)
  return ''.join(letras) 

print (removerVocales('Diego'))
