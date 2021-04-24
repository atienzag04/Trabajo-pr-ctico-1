def devolver_lista_con_auxiliar():
    lista = []
    lista_g = int(input("Enter number of elements : "))
    for i in range(0, lista_g):
     ele = (input())
     lista.append(ele)
    lista_auxiliar = tuple(reversed(lista))
    return lista_auxiliar
print(devolver_lista_con_auxiliar())