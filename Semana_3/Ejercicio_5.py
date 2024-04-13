'''
### **Ejercicio 5: TDA en dos niveles**

Modelar el TDA "Rectangulo" a partir de los dos lados que lo definen.

Se deben implementar las siguientes operaciones:

- Constructor: Recibe las longitudes de ambos lados
- area: calcula y devuelve el area del rectangulo
- perimetro: calcula y devuelve el perimetro
- __repr__ : imprime la longitud de los lados

Luego, modelar el TDA "Cuadrado" teniendo unicamente como variable interna en la estructura una variable de tipo "Rectangulo". El TDA Cuadrado debe 
tener las mismas operaciones que el TDA Rectangulo.

Ayuda:

Área(Rectángulo) = lado1 * lado2

Área(Cuadrado) = lado^2

Perímetro(Rectangulo) = 2 * lado1 + 2 * lado2

Perímetro(Cuadrado) = 4 * lado
'''
import Validadores
class Rectangulo:
    def __init__(self, lado1:float, lado2:float):
        self.__lado1 = Validadores.validarPositivo(lado1,"lado1")
        self.__lado2 = Validadores.validarPositivo(lado2,"lado2")
    
    def __repr__(self) -> str:
        return f"Lado 1 = {self.__lado1}, Lado 2 ={self.__lado2}"
    
    def area(self)-> float:
        return self.__lado1 * self.__lado2
    def perimetro(self) -> float:
        return self.__lado1 * 2 + self.__lado2 * 2
    
class Cuadrado:
    def __init__(self, lados:float) -> None:
        self.__lados = Rectangulo(lados, lados)
    def __repr__(self) -> str:
        return str(self.__lados)
    def area(self):
        return self.__lados.area()
    def perimeto(self):
        return self.__lados.perimetro()
    

cuadradoPrueba1 = Cuadrado(12.5)
print(cuadradoPrueba1)
print(cuadradoPrueba1.area())
