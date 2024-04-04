'''
Escribir un programa que pida dos años y escriba cuántos años bisiestos
hay entre esas dos fechas(incluidos los dos años)
'''


print("Ingrese un periodo de años:")
#Pedir los valores
valorA = int(input("Entre: "))
valorB = int(input("Y: "))
#funciones Aux
def minimoEntre(numero1, numero2):
  return numero1 if numero1 < numero2 else numero2
def valor_MultiploDe_(valor, divisor):
  return valor % divisor == 0
def boolToInt(valorBooleano):
  return 1 if valorBooleano else 0
def maximoEntre(numero1, numero2):
  return numero1 if numero1 > numero2 else numero2
def _EsBisiesto(anio):
  return((not(valor_MultiploDe_(anio, 100)) and (valor_MultiploDe_(anio, 4)) or valor_MultiploDe_(anio, 400)))
#Ordenar los valores
max = maximoEntre(valorA, valorB)
min = minimoEntre(valorA, valorB)
#Iniciar contador
cantidadBisiestos = 0;
for i in range(min, max + 1):
  #Sumar al contador si es bisiesto el año indicado por el valor de i
  cantidadBisiestos += boolToInt(_EsBisiesto(i))

print(f"La cantidad de años bisiestos entre {min} y {max} es de : {cantidadBisiestos}")