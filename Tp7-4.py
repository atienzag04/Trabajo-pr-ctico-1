"""Septimo punto"""
"""Cuarta parte"""
def cuantos_faltan_hasta_final_mes (dias_que_pasaron, mes):
    """Se devuelve cuanto falta hasta el fin de mes"""
    if mes.lower() in ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"):
        dias_del_mes = 31
        dias_que_pasaron = dias_del_mes - dias_que_pasaron 
        return dias_que_pasaron
    elif mes.lower() == "febrero":
        dias_del_mes = 28
        dias_que_pasaron = dias_del_mes - dias_que_pasaron 
        return dias_que_pasaron
    elif mes.lower() in ("abril", "junio", "septiembre", "noviembre"):
        dias_del_mes = 30
        dias_que_pasaron = dias_del_mes - dias_que_pasaron 
        return dias_que_pasaron
    else:
        return "No ingreso un mes"
