"""Septimo punto"""
"""Septima parte"""
def diferencia_en_fechas():
    """Se muestra cuantos dias pasan entre 2 fechas dadas"""
    anio_1 = int(input ("Ingrese el primer año a utilizar: "))
    anio_2 = int(input ("Ingrese el segundo año a utilizar: "))
    mes_1 = input ("Ingrese el primer mes: ")
    mes_2 = input ("Ingrese el segundo mes: ")
    dia_1 = int(input ("Ingrese el primer día: "))
    dia_2 = int(input ("Ingrese el segundo día: "))
    if anio_1 % 4 == 0:
        if anio_1 % 100 == 0:
            if anio_1 % 400 == 0:
                bisiesto = True
            else:
                bisiesto = False
        else:
            bisiesto = True
    else:
        bisiesto = False
    if mes_1.lower() == "enero":
        dias_total_del_anio_1 = 0 
    elif mes_1.lower() == "febrero":
        dias_total_del_anio_1 = 31
    elif mes_1.lower() == "marzo":
        dias_total_del_anio_1 = 59
        if bisiesto == True:
            dias_total_del_anio_1 = dias_total_del_anio_1 + 1
    elif mes_1.lower() == "abril":
        dias_total_del_anio_1 = 90
    elif mes_1.lower() == "mayo":
        dias_total_del_anio_1 = 120
    elif mes_1.lower() == "junio":
        dias_total_del_anio_1 = 151
    elif mes_1.lower() == "julio":
        dias_total_del_anio_1 = 181
    elif mes_1.lower() == "agosto":
        dias_total_del_anio_1 = 212
    elif mes_1.lower() == "septiembre":
        dias_total_del_anio_1 = 243
    elif mes_1.lower() == "octubre":
        dias_total_del_anio_1 = 273
    elif mes_1.lower() == "noviembre":
        dias_total_del_anio_1 = 304
    elif mes_1.lower() == "diciembre":
        dias_total_del_anio_1 = 334

    todos_los_dias_1 = dias_total_del_anio_1 + dia_1

    if anio_2 % 4 == 0:
        if anio_2 % 100 == 0:
            if anio_2 % 400 == 0:
                bisiesto = True
            else:
                bisiesto = False
        else:
            bisiesto = True
    else:
        bisiesto = False
    if mes_2.lower() == "enero":
        dias_total_del_anio_2 = 0 
    elif mes_2.lower() == "febrero":
        dias_total_del_anio_2 = 31
    elif mes_2.lower() == "marzo":
        dias_total_del_anio_2 = 59
        if bisiesto == True:
            dias_total_del_anio_2 = dias_total_del_anio_2 + 1
    elif mes_2.lower() == "abril":
        dias_total_del_anio_2 = 90
    elif mes_2.lower() == "mayo":
        dias_total_del_anio_2 = 120
    elif mes_2.lower() == "junio":
        dias_total_del_anio_2 = 151
    elif mes_2.lower() == "julio":
        dias_total_del_anio_2 = 181
    elif mes_2.lower() == "agosto":
        dias_total_del_anio_2 = 212
    elif mes_2.lower() == "septiembre":
        dias_total_del_anio_2 = 243
    elif mes_2.lower() == "octubre":
        dias_total_del_anio_2 = 273
    elif mes_2.lower() == "noviembre":
        dias_total_del_anio_2 = 304
    elif mes_2.lower() == "diciembre":
        dias_total_del_anio_2 = 334

    todos_los_dias_2 = dias_total_del_anio_2 + dia_2

    dias_del_anio_1 = anio_1 * 365
    if bisiesto == True:
        dias_del_anio_1 = dias_del_anio_1 + 1

    dias_del_anio_2 = anio_2 * 365
    if bisiesto == True:
        dias_del_anio_2 = dias_del_anio_2 + 1
    
    fecha_1 = todos_los_dias_1 + dias_total_del_anio_1 
    fecha_2 = todos_los_dias_2 + dias_total_del_anio_2

    if (fecha_1 - fecha_2) > 0:
        fecha_total = fecha_1 - fecha_2
    elif (fecha_2 - fecha_1) > 0:
        fecha_total = fecha_2 - fecha_1
    
    return "Entre ambas fechas, hay ", fecha_total, " dias, ", fecha_total/30, " meses, y ", (fecha_total/360), " años."