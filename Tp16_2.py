"""Decimo sexto punto"""
"""Segunda parte"""
def remover_consonantes():
  """Se retiran las consonantes de la palabra"""
  palabra = str(input("Ingrese una palabra para retirarle las consonantes: "))
  letras = []
  for caracter in palabra:
    if caracter.lower() in 'aeiou':
      letras.append(caracter)
  return ''.join(letras) 
