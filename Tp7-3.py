'''Séptima parte'''
'''Tercera actividad'''
def validar_fecha():
    """Se verifica si una fecha puede ser valida"""
    anio = int(input ("Ingrese el año a utilizar: "))
    mes = input ("Ingrese el mes: ")
    dia = int(input ("Ingrese el día: "))
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
    if mes.lower() in ("enero","marzo","mayo","julio","agosto","octubre","diciembre") and dia <= 31 and dia > 0:
        fecha_correcta = True
    elif mes.lower() in ("abril","junio","septiembre","noviembre") and dia <= 30 and dia > 0:
        fecha_correcta = True
    elif bisiesto == False and mes.lower() in ("febrero") and dia <= 28 and dia > 0:
        fecha_correcta = True
    elif bisiesto == True and mes.lower() in ("febrero") and dia <= 29 and dia > 0:
        fecha_correcta = True
    else:
        fecha_correcta = False
    return fecha_correcta
