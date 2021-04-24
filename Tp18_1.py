def devolver_lista_alreves():
    lista = []
    lista_g = int(input("Enter number of elements : "))
    for i in range(0, lista_g):
     ele = int(input())
     lista.append(ele) # adding the element
    lista.reverse()

    return lista
print(devolver_lista_alreves())