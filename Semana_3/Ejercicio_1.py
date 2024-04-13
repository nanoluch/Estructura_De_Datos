'''
**Ejercicio 1**
Implementar el TDA "Propiedad" que modela un inmueble, con una estructura definida por los siguientes componentes:
- Calle
- Número
- Localidad
- Año de construcción
- Cantidad de ambientes

Implementar las siguientes operaciones:
- Constructor: Debe incluir las validaciones necesarias, teniendo en cuenta que solo se almacenan propiedades construidas luego de 1870.
- __repr__: Al usar la función *print* con una variable del tipo propiedad debe mostrar: **'calle' 'numero' ('localidad')**.
- mismaLocalidad: Operación que recibe dos propiedades y retorna *True* si estan en la misma localidad y *False* en caso contrario.
- mayorNumeración: Operación que recibe dos propiedades y si están en la misma calle, retorna la que posee mayor numeración. Si están calles diferentes debe lanzar una excepción.
- calculaImpuestoARBA: Operación que retorna el porcentaje de impuesto inmobiliario de una propiedad, según la siguiente regla:
 - Propiedades entre 1870 y 1949:
   - Entre 1 y 3 ambientes: 5% de impuesto
   - Entre 4 y 6 ambientes: 10% de impuesto
   - Más de 6 ambientes: 25 % de impuesto
 - Propiedades desde 1950 hasta la actualidad:
   - Entre 1 y 5 ambientes: 5% de impuesto
   - Más de 5 ambientes: 35 % de impuesto
'''
import Validadores#Importa validadores generales.
#Validadores generales para los ejercicios.

def validarTipoYAnioConstruccion(anioConstruccion:int):
    if Validadores.validarTipo(anioConstruccion, int, "anioConstruccion"):
        salida = anioConstruccion if anioConstruccion >= 1870 else None
    return salida

class Propiedad:
    def __init__(self, calle:int, numero:int, localidad:str, anioConstruccion:int, cantidadAmbientes:int) -> None:
        self.__calle = Validadores.validarStrVacia(calle, "calle")
        self.__numero = Validadores.validarNatural(numero, "numero")
        self.__localidad = Validadores.validarStrVacia(localidad, "localidad")
        self.__anioConstruccion = validarTipoYAnioConstruccion(anioConstruccion)
        self.__cantidadAmbientes = Validadores.validarNatural(cantidadAmbientes, "cantidadAmbientes")
    
    def __repr__(self) -> str:
        return f"{self.__calle} {self.__numero} ({self.__localidad})"
    
    def mismaCalle(propiedad1, propiedad2)->bool:
        return propiedad1.__calle == propiedad2.__calle
    
    def mayorNumeracion(propiedad1, propiedad2):
        propiedadMayorNumeracion = None
        if Propiedad.mismaCalle(propiedad1,propiedad2):
            propiedadMayorNumeracion = propiedad1
        if propiedad2.__numero > propiedad1.__numero:
            propiedadMayorNumeracion = propiedad2
        return propiedadMayorNumeracion

    def mismaLocalidad(propiedad1, propiedad2) -> bool:
        #Indica si sos propiedades son de la misma localidad
        return propiedad1.__localidad == propiedad2.__localidad
    def impuestoArba(self)->str:
        if self.__anioConstruccion < 1950:
            if self.__cantidadAmbientes > 6:
                salida = f"25% de impuesto"
            elif self.__cantidadAmbientes > 3:
                salida = f"10% de impuesto"
            else:
                salida = f"5% de impuesto"
        else:
            salida = f"35% de impuesto" if self.__cantidadAmbientes > 5 else f"5% de impuesto"
        return salida


