def dias_para_terminar_mes (mes, dias):
    
    if mes.lower() in ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"):
        dias_total = 31
    elif mes.lower() == "febrero":
        dias_total = 28/29
    elif mes.lower() in ("abril", "junio", "septiembre", "noviembre"):
        dias_total = 30
    else:
        return "No ingreso una fecha valida"

    if dias <= dias_total:
        dias_que_faltan = dias_total - dias
        return dias_que_faltan
    else: 
        return "No ingreso una fecha valida"

print (dias_para_terminar_mes("junio", 12))
