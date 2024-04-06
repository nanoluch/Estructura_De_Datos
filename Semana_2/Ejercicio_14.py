"""
Escribir un programa que solicita el ingreso de números primos. 
 La lectura finalizará cuando ingrese un número que no sea primo. 
 Por cada número, mostrar la suma de sus dígitos. 
 Al finalizar el programa, mostrar el factorial del mayor número ingresado.
 Utilizar una o más funciones, según sea necesario.
"""
#Funciones auxiliares.
def esNumPrimo(numero:int)->bool:
    if numero > 1:
        esPrimo = True
        divisor = 2
        while divisor < numero and esPrimo:
            if numero % divisor == 0:
                esPrimo = False
            divisor += 1
    else:
        esPrimo = False
    return esPrimo

def sumarDigitos(num:int)->int:
  #Describe la suma de los digitos de un numero.
    sumaDeDigitos = 0
    while num > 0:
        #Sumar el numero despues de la coma(variable % 10)
        sumaDeDigitos += num % 10
        #Reasignar el valor de la variable a el numero sin la coma(division entera de la variable)
        num = num // 10
    return sumaDeDigitos

def factorialDe_(unNumero:int)->int:
  respuesta = 1
  while unNumero > 0:
    respuesta *= unNumero
    unNumero -= 1
  return respuesta

def maximoEntre(numero1:int, numero2:int)->int:
  return numero1 if numero1 > numero2 else numero2

#Inicio programa
ingreso = int(input("Ingrese un número: "))
print(f"La suma de los digitos de {ingreso} es {sumarDigitos(ingreso)}")
numeroMaximo = ingreso

while not(esNumPrimo(ingreso)):
    ingreso = int(input("Ingrese otro número:"))
    print(f"La suma de los digitos de {ingreso} es {sumarDigitos(ingreso)}")
    numeroMaximo = maximoEntre(ingreso, numeroMaximo)


print("FIN PROGRAMA")
print(f"El mayor número ingresado fué {numeroMaximo} y su factorial es : {factorialDe_(numeroMaximo)}")