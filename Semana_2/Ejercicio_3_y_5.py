'''
Ejercicio 3
Escribir una función que calcule
y retorne el factorial de un número natural.
'''
def factorialDe_(unNumero):
  respuesta = 1
  while unNumero > 0:
    respuesta *= unNumero
    unNumero -= 1
  return respuesta

        
'''
Ejercicio 5
Escribir la función máximo, que recibe 2 números por parámetro
 y retorna el mayor.
Luego, usando esta función, escriba un programa que pida 
10 números al usuario por teclado y al finalizar 
informe el mayor por pantalla.
'''
def maximoEntre(numero1, numero2):
  return numero1 if numero1 > numero2 else numero2

for i in range (10):
  numeroIngresado = int(input(f"Ingrese el numero para la posición {i + 1}:"))
  if i > 0:
    numeroMaximo = maximoEntre(numeroMaximo, numeroIngresado)
  else:
    numeroMaximo = numeroIngresado
print(f"El numero mas alto de los ingresados es {numeroMaximo}")