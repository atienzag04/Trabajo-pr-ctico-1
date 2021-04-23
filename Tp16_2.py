def removerConsonantes(palabra):
  letras = []
  for caracter in palabra:
    if caracter.lower() not in 'bdfghjklmnñpqrstvxyz':
      letras.append(caracter)
  return ''.join(letras) 

print (removerConsonantes('Diego'))
