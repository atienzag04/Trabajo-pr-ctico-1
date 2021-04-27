'''Sexto punto'''
print ("Calculo el maximo producto")
def mayor_producto_de_cuatro (n1, n2, n3, n4):
    #Creo las variables a utilizar
    m1 = n1 * n2
    m2 = n1 * n3
    m3 = n1 * n4
    m4 = n2 * n3 
    m5 = n2 * n4
    m6 = n3 * n4
    #Considero a m1 como el mayor, para que luego pueda descubrir 
    # cual es el mayor en el for
    mayor = m1
    for i in (m2, m3, m4, m5, m6):
        #Comparo a todos las multiplicaciones, hasta encontrar la mayor
        if i > mayor:
            mayor = i
    return mayor
print (mayor_producto_de_cuatro (1, 5, -2, 4))
