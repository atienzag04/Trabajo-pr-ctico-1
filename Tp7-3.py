bisiesto = bool
bisiesto = False

def fecha_erronea (dia, mes, anio):
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
        
    if mes.lower() in ("enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"):
        return "31"
    elif mes.lower() == "febrero":
        return "28/29"
    elif mes.lower() in ("abril", "junio", "septiembre", "noviembre"):
        return "30"
    else:
        return "No ingreso un mes"
    