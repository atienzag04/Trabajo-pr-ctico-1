def cuantos_dias_tiene_el_mes (mes):
    if mes.lower() in ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"):
        return "31"
    elif mes.lower() == "febrero":
        return "28/29"
    elif mes.lower() in ("abril", "junio", "septiembre", "noviembre"):
        return "30"
    else:
        return "No ingreso un mes"
