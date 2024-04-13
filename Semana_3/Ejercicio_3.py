'''
### **Ejercicio 3**

Implementar el TDA "Tiempo" que modela una duracion en horas, minutos y segundos.

Se deben implementar las siguientes operaciones:
- Constructor: Debe incluir las validaciones necesarias, la hora debe ser un número positivo y los minutos y segundos deben ser números positivos entre 0 y 59.
- __repr__: Al usar la función *print* con una variable del tipo tiempo debe mostrar: **'horas':'minutos':'segundos'**.
- tiempoASegundos: Operación que toma una variable de tipo tiempo y retorna la cantidad en segundos.
- tiemposDesdeSegundos: Operación que recibe un tiempo en segundos como parámetro y retorna una variable de tipo tiempo, en horas minutos y segundos.
- mayorDuracion: Operación que recibe dos variables de tipo tiempo y retorna la de mayor duración.
'''
import Validadores

class Tiempo:
    def __init__(self, horas:int = 0, minutos:int = 0, segundos:int = 0) -> None:
        self.__horas = Validadores.validarNatural(horas, "horas")
        self.__minutos = self.validarEnterosHasta(minutos, "minutos", 60)
        self.__segundos = self.validarEnterosHasta(segundos, "segundos", 60)
    def validarEnterosHasta(varTest:int,varName:str, max:int):
        if(varTest < max):
            return Validadores.validarNatural(varTest, varName)
    def __repr__(self) -> str:
        return f"{self.__horas} : {self.__minutos} : {self.__segundos}"
    
    def tiempoASegundos(self):
        return self.__segundos + self.__minutos * 60 + self.__horas * 3600

    def tiempoDesdeSegundos(cantidadSegundos:int):
        if(Validadores.validarNatural(cantidadSegundos, "cantidadSegundos")):
            horas = cantidadSegundos // 3600
            segundosRestantes = cantidadSegundos % 3600
            minutos = segundosRestantes // 60
            segundosRestantes = segundosRestantes % 60
            segundos = segundosRestantes
        return(Tiempo(horas, minutos, segundos))
    
    def mayorDuracion(tiempo1, tiempo2):
        return tiempo1 if tiempo1.tiempoASegundos() > tiempo2.tiempoASegundos() else tiempo2
    def menorDuracion(tiempo1, tiempo2):
        return tiempo1 if tiempo1.tiempoASegundos() < tiempo2.tiempoASegundos() else tiempo2
    def __sub__(valor1, valor2):
        #Retorna una variable de timpo Tiempo con la diferencia de tiempos
        diferenciaSegundos = abs(valor1.tiempoASegundos() - valor2.tiempoASegundos())
        return Tiempo.tiempoDesdeSegundos(diferenciaSegundos)