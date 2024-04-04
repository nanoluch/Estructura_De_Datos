'''
Escribir una función que calcule el área de un circulo y otra que
calcule el volumen de un cilindro usando la primera función
'''
#Para calcular el area de un circulo es A= Pi * radio**2
#Para calcular el volumen de un cilindro es V = Area(circulo) * Altura(cilindro)

def areaDeCirculoRadio_(radio):
  return 3.14 * radio**2
def volumenDeCilindroRadio_Altura_(radio, altura):
  return areaDeCirculoRadio_(radio) * altura

radio = 4
altura = 4
print(f"El area de un circulo de radio 4 es: {areaDeCirculoRadio_(radio)}" )
print(f"El volumen de un cilindro de radio 4 y altura 2 es: {volumenDeCilindroRadio_Altura_(radio, altura)}")