"""Decimo sexto punto"""
"""Tercera parte"""
def remplazar_vocal_por_la_siguiente():
    """Se cambian las vocales, por la siguiente
    Ej: vacunas pasa a ser vecanes"""
    cadena = input("Ingese una cadena: ")       
    largo = len(cadena)                                    
    inicio = 0                                                   
    cadena_final = ""                                                    
    caracter = ""                                              
    while inicio < largo:                               
        if cadena[inicio] in "a":                     
            caracter="e"                                
        elif cadena[inicio] in "e":                    
            caracter="i"     
        elif cadena[inicio] in "i":                    
            caracter="o"
        elif cadena[inicio] in "o":                    
            caracter="u"
        elif cadena[inicio] in "u":                   
            caracter="a"                              
        else:                                              
            caracter=cadena[inicio]                  
        cadena_final+= caracter                                 
        inicio+=1                                       
    return cadena_final                                      
