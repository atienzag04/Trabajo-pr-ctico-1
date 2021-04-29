"""Decimo octavo punto"""
"""Segunda parte"""
def devolver_lista_alreves():
    """Se devuelve una lista de elementos dada por el usuario, dada vuelta
    sin el uso de una lista auxiliar"""
    lista = []
    lista_g = int(input("Ingrese numeros de elementos: "))
    for i in range(0, lista_g):
        ele = (input())
        lista.append(ele) 
    #Se utiliza el for para saber cuantos elementos hay en la funcion
    lista.reverse()
    return lista
print(devolver_lista_alreves())
