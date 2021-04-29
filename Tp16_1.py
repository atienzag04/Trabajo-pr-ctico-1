"""Decimo sexto punto"""
"""Primera parte"""
def remover_vocales():
  """Se retiran las vocales de la palabra"""
  palabra = str(input("Ingrese una palabra para retirarle las vocales: "))
  letras = []
  for caracter in palabra:
    if caracter.lower() not in 'aeiou':
      letras.append(caracter)
  return ''.join(letras) 
