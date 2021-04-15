bisiesto = bool
bisiesto = False

def funcion_anos_bisiesto (anio):
    
    if anio % 4 == 0:

        if anio % 100 == 0:

            if anio % 400 == 0:
                bisiesto = True
            else:
                bisiesto = False
        else:
            bisiesto = True
    else:
        bisiesto = False
    return bisiesto 
print (funcion_anos_bisiesto(2018))