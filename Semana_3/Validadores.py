#Validadores generales para los ejercicios.


def validarStrVacia(stringVar:str, varName:str):
    #Valida que la variable *stringVar* no sea una variable vacia a traves de la función *validarTipo*
    salida = None
    if validarTipo(stringVar, str, varName):
        if stringVar != "":
            salida = stringVar.lower()
        else:
            raise Exception(varName + "No puede estar vacia.")
    return salida

def validarTipo(varTest, tipo:type, varName:str):
    #Valida si la variable varTest es del tipo *tipo*, de lo contrario arroja una excepcion indicando el tipo correcto del nombre de la variable.
    salida = None
    if varTest == 0:
        return int(0)
    elif isinstance(varTest, tipo):
        salida = varTest
    else:
        raise Exception(f"La variable {varName} debe ser un {tipo}")
    return salida

def validarPositivo(numero:int, varName:str)->int:
    salida = None #Se declara esta variable pero si no se llega a asignar un valor para el return, por defecto se devuelve el valor "None"
    if numero == 0:
        return int(0)
    elif numero > 0:
        salida = numero
    else:
        raise Exception(varName + " debe ser un numero entero positivo.")
    return salida

def validarNatural(numero, varName:str):
    #Valida *numero* sea un numero entero positivo.
    salida = None
    if numero == 0:
        return int(0)
    elif validarTipo(numero, int, varName):
        salida = validarPositivo(numero, varName)
    return salida