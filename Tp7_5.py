def tiempo_entre_años (dia, mes, anio):



    if mes.lower() == "enero":
        dias_total_del_mes = 31
        dias_total_del_anio = 0 

    elif mes.lower() == "febrero":
        dias_total_del_mes = 28
        dias_total_del_anio = 31

    elif mes.lower() == "marzo":
        dias_total_del_mes = 31
        dias_total_del_anio = 59

    elif mes.lower() == "abril":
        dias_total_del_mes = 30
        dias_total_del_anio = 90

    elif mes.lower() == "mayo":
        dias_total_del_mes = 31
        dias_total_del_anio = 120

    elif mes.lower() == "junio":
        dias_total_del_mes = 30
        dias_total_del_anio = 151

    elif mes.lower() == "julio":
        dias_total_del_mes = 31
        dias_total_del_anio = 181

    elif mes.lower() == "agosto":
        dias_total_del_mes = 31
        dias_total_del_anio = 212

    elif mes.lower() == "septiembre":
        dias_total_del_mes = 30
        dias_total_del_anio = 243

    elif mes.lower() == "octubre":
        dias_total_del_mes = 31
        dias_total_del_anio = 273

    elif mes.lower() == "noviembre":
        dias_total_del_mes = 30
        dias_total_del_anio = 304

    elif mes.lower() == "diciembre":
        dias_total_del_mes = 31
        dias_total_del_anio = 334

    else:
        return "No ingreso un mes"
    
    dias_que_faltan = 365 - dia - dias_total_del_anio
    return dias_que_faltan
print (tiempo_entre_años (11, "diciembre", 2003) )

