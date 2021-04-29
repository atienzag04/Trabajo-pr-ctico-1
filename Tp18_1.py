"""Decimo octavo punto"""
"""Primera parte"""
def devolver_lista_con_auxiliar():
    """Se devuelve una lista de elementos dada por el usuario, dada vuelta"""
    #Se utiliza una lista auxiliar, para guardar la nueva lista con los 
    # elementosdados vuelta
    lista = []
    lista_g = int(input("Ingrese el numero de elementos : "))
    #Se utiliza el for para saber cuantos elementos hay en la funcion
    for i in range(0, lista_g):
     ele = (input())
     lista.append(ele)
    lista_auxiliar = tuple(reversed(lista))
    return lista_auxiliar
