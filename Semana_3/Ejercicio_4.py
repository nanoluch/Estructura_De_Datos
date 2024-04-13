'''
### **Ejercicio 4: TDA en dos niveles**

Modelar el TDA "Cronometro", que contiene un tiempo inicial y un tiempo final.

Se deben implementar las siguientes operaciones:

- Constructor: Queremos modelar el tiempo inicial y final con el TDA "Tiempo". Se pueden tener dos variables que se inicializaran
 en otra operación de la interface.
- Comenzar: Debe recibir las hs,min y seg iniciales.
- Finalizar: Debe recibir las hs,min y seg finales.
- TiempoEmpleado: Devuelve una variable de tipo Tiempo con la diferencia entre el tiempo inicial y el final.

'''

import Ejercicio_3#Ejercicio con la clase Tiempo creada

class Cronometro:
    def __init__(self, tiempo1:Ejercicio_3.Tiempo, tiempo2 = Ejercicio_3.Tiempo):
        self.__tiempoInicial = Ejercicio_3.Tiempo.menorDuracion(tiempo1, tiempo2)
        self.__tiempoFinal = Ejercicio_3.Tiempo.mayorDuracion(tiempo1, tiempo2)
    def comenzar(self):
        return self.__tiempoInicial
    def finalizar(self):
        return self.__tiempoFinal
    def tiempoEmpleado(self):
        return self.__tiempoFinal - self.__tiempoInicial
    




