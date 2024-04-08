'''
Escribir un programa que pida números positivos
(Debe dejar de pedir números cuando se ingrese uno negativo). 
Mostrar el número cuya sumatoria de dígitos fue mayor 
y la cantidad de números cuya sumatoria de dígitos fue menor que 10.
Utilizar una o más funciones, según sea necesario.
'''
#Funciones aux
def boolToInt(valorBooleano:bool)->int:
  return 1 if valorBooleano else 0
def maximoEntre(numero1:int, numero2:int)->int:
  return numero1 if numero1 > numero2 else numero2
def sumarDigitos(num:int)->int:
  #Describe la suma de los digitos de un numero.
    sumaDeDigitos = 0
    while num > 0:
        #Sumar el numero despues de la coma(variable % 10)
        sumaDeDigitos += num % 10
        #Reasignar el valor de la variable a el numero sin la coma(division entera de la variable)
        num = num // 10
    return sumaDeDigitos
#Fin funciones aux  

#Ingresar el primer valor
ingreso = int(input("Ingrese un número: "))
#Guardar el número como mayor sumatoria
maxSumatoriaDeDigitos = sumarDigitos(ingreso)
numeroMaximoSumado = ingreso;
sumatoriasMenoresQue10 = 0;
#Entrar al bucle si no es negativo
while (ingreso >= 0):
  if(maxSumatoriaDeDigitos < sumarDigitos(ingreso)):
    #Actualizar maximo
    maxSumatoriaDeDigitos = sumarDigitos(ingreso)
    numeroMaximoSumado = ingreso
  #Contar si suma menos que 10
  sumatoriasMenoresQue10 += boolToInt(sumarDigitos(ingreso) < 10)
  #Volver a pedir ingreso
  ingreso = int(input("Ingrese un número: "))

print(f"El numero cuya sumatoria de digitos fué mas alta fué: {numeroMaximoSumado}")
print(f"La cantidad de ingresos cuya suma de digitos es menor a 10 es: {sumatoriasMenoresQue10}")