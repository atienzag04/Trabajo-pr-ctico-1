def mayor_producto_de_cuatro (n1, n2, n3, n4):
    m1 = n1 * n2
    m2 = n1 * n3
    m3 = n1 * n4
    m4 = n2 * n3 
    m5 = n2 * n4
    m6 = n3 * n4
    
    mayor = m1
    for i in (m2, m3, m4, m5, m6):
        if i > mayor:
            mayor = i
    return mayor
print (mayor_producto_de_cuatro (1, 5, -2, 4))
