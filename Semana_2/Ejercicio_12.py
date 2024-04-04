'''
Escribir una función que tome por parámetro un numero entero
y retorne la suma de sus dígitos.
Para obtener los digitos deben ir dividiendo (division entera)
por 10 sucesivamente y tomando el resto 
(digito que esta mas a la derecha).
'''
#Pedir numero
variableString = (input("Ingrese un numero: "))
#Funcion auxiliar
def sumarDigitos(num):
  #Describe la suma de los digitos de un numero.
    sumaDeDigitos = 0
    while num > 0:
        #Sumar el numero despues de la coma(variable % 10)
        sumaDeDigitos += num % 10
        #Reasignar el valor de la variable a el numero sin la coma(division entera de la variable)
        num = num // 10
    return sumaDeDigitos
print(sumarDigitos(variableString))