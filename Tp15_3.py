"""Decimo quinto punto"""
"""Tercera parte"""
def palabras_con_a():
  """Cada palabra que comience con a se muestra"""
  palabra = str(input("Ingrese un texto: ")).split(' ')
  resultado = ' '
  #Uso el for para que cada palabra que comience con A se muestre 
  for i in range(0, len(palabra)):
    cadena = palabra[i]
    if cadena[0] in ["A", "a"]:
      resultado += palabra[i] + " "
  return resultado
 
