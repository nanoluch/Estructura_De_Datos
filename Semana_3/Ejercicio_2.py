'''
### **Ejercicio 2**

Implementar el TDA "Cuenta" que modela una cuenta bancaria, la estructura de datos esta compuesta por los siguientes componentes:
- Número de cuenta
- DNI del titular
- Saldo de cuenta actual
- Interés anual

Implementar las siguientes operaciones:
- Constructor: Debe incluir las validaciones necesarias.
- __repr__: Al usar la función *print* con una variable del tipo cuenta debe mostrar: **Cuenta Nro: 'numero' - Titular: 'dni' ($'saldo')**.
- actualizarSaldo: Operación que actualiza el saldo de la cuenta aplicándole el interés diario (interés anual dividido entre 365).
- ingresarDinero: Operación que recibe un número e ingresa esa cantidad en la cuenta.
- retirarDinero: Operación que recibe un número y extrae esa cantidad de la cuenta (si hay saldo disponible), sino debe lanzar una excepción.
'''
import Validadores
class Cuenta:
    def __init__(self,nroCuenta:str, dni:int, saldoActual:float, interesAnual:float) -> None:
        #nroCuenta es un string, ya que una cuenta puede iniciar con 0
        self.__nroCuenta = Validadores.validarTipo(nroCuenta, str, "nroCuenta")
        self.__dni = Validadores.validarPositivo(dni, "dni")
        self.__saldoActual = Validadores.validarTipo(saldoActual, float, "saldoActual")
        self.__interesAnual= Validadores.validarTipo(interesAnual, float, "interesAnual")
    
    def __repr__(self) -> str:
        return f"Cuenta Nro: '{self.__nroCuenta}' - Titular: '{self.__dni}' (${self.__saldoActual})"
    
    def actualizarSaldo(self):
        self.__saldoActual += (self.__saldoActual * (self.__interesAnual / 365))
    
    def ingresarDinero(self, monto:float):
        self.__saldoActual += monto
    
    def retirarDinero(self, monto:float):
        if monto < self.__saldoActual:
            self.__saldoActual -= monto
        else:
            raise Exception("El monto a retirar es mayor al disponible en la cuenta")    

