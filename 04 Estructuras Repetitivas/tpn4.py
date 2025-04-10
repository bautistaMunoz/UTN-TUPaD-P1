import random

#PUNTO 1
for x in range (0,101):
    print(x)

#PUNTO 2
numeroEntero = int(input("Coloque un numero entero"))

numeroEntero = abs(numeroEntero)

cantidadDeDigitos = len(str(numeroEntero))

print("Tiene",cantidadDeDigitos)

#PUNTO 3
valor1 = int(print("Escribe el primer valor"))
valor2 = int(print("Escrbie el segundo valor"))

suma = 0
for num in range(valor1 + 1,valor2):
    suma += num

print("La suma es igual a", suma)

#PUNTO 4
resultado = 0

numeEnt1 = int(input("Ingrese un numero entero: "))
numeEnt2 = int(input("Ingrese otro numero entero: "))

while numeEnt1 > 0 or numeEnt2 > 0:
    resultado += numeEnt1 + numeEnt2
    
    numeEnt1 = int(input("Ingrese un numero entero: "))
    numeEnt2 = int(input("Ingrese otro numero entero: "))

print("El resultado es", resultado)

#PUNTO 5
numero = random.randint(0,9)
numeroDeseado = int(input("Coloque un numero entre 0 y 9"))

while numero != numeroDeseado:
    print("Numero incorrecto intente nuevamente")
    numeroDeseado = int(input("Coloque un numero entre 0 y 9"))

print("Numero correcto! El numero era",numero)

#PUNTO 6
for i in range(100, -1, -1):  
    if i % 2 == 0:
        print(i)

#PUNTO 7

limite = int(input("Ingrese un numero entero positivo: "))
suma = 0

for i in range(0, limite + 1):
    suma += i

print("La suma de los numero de 0 hasta", limite, "es:", suma)

#PUNTO 8
cantidad = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    num = int(input(f"ingrese el numero {i+1}: "))
    
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print("Cantidad de numeros pares:", pares)
print("Cantidad de numeros impares:", impares)
print("Cantidad de numeros positivos:", positivos)

#PUNTO 9

cantidad = 100
suma = 0

for i in range(cantidad):
    num = int(input(f"Ingrese el numero {i+1}: "))
    suma += num

media = suma / cantidad
print("La media de los numeros ingresados es:", media)

#SUMA 10
numero = int(input("Ingrese un numero: "))
numero_invertido = numero[::-1] 

print("umero invertido:", numero_invertido)
