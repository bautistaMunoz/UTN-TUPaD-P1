import random
from statistics import mean, median, mode

# PUNTO 1
edad = input("Ingrese su edad")
if edad > 18:
    print("Es mayor de edad")

# PUNTO 2
nota = input("Ingrese su nota")
if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

# PUNTO 3
numero = int(input("Ingrese un numero par"))
if numero % 2 == 0:
    print("Ha ingresado un numero par")
else:
    print("Por favor,ingrese un numero par")

# PUNTO 4
edad2 = input("Ingrese su edad")
if edad2 < 12:
    print("Niño/a")
elif edad2 >= 12 and edad2 < 18:
    print("Adolescente")
elif edad2 >= 18 and  edad2 < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# PUNTO 5 
password = input("Escribir una contraseña entre 8 y 14 caracteres")

if len(password) >= 8 and len(password) <= 14:
    print("Ha ingresado una contraseña correcta")

else:
    print("Porfavor, ingrese una contraseña de entre 8 y 14 caracteres")

# PUNTO 6

numeroAleatorios = [random.randint(1, 100) for i in range(50)]

media = mean(numeroAleatorios)
mediana = median(numeroAleatorios)
moda = mode(numeroAleatorios)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
elif media == mediana == moda:
    print("No hay sesgo")
else:
    print("No se pudo determinar")

# PUNTO 7

texto = input("Ingrese una palabra")
if texto[-1] in "aeiou":
    texto += "!"
print(texto)

# PUNTO 8 

userNombre = input("Ingrese su nombre")
userNumName = int(input("Ingrese 1 si quiere su nombre en mayusuclas, ingrese 2 si quiere su nombre en minusculas,ingrese 3 si quiere su nombre con la primera letra mayuscula"))

if userNumName == 1:
    print (userNombre.upper())
elif userNumName == 2:
    print (userNombre.lower())
else:
    print (userNombre.title())

# PUNTO 9

magnitudTerre = int(input("Ingrese la magnitud de su terreno"))

if magnitudTerre < 3:
    print("Muy leve")
elif magnitudTerre >= 3 and magnitudTerre < 4:
    print("Leve")
elif magnitudTerre >= 4 and magnitudTerre < 5:
    print("Moderado")
elif magnitudTerre >= 5 and magnitudTerre < 6:
    print("Fuerte")
elif magnitudTerre >= 6 and magnitudTerre < 7:
    print("Muy fuerte")
else:
    print("Extremo")

# PUNTO 10
hemisferio = input("¿En que hemisferio estas? (N/S): ").strip().upper()
mes = int(input("¿Que mes es?"))
dia = int(input("¿Que dia es?"))

if hemisferio == "N":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Primavera"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Verano"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Otoño"
    else:
        estacion = "Fecha invlida"

elif hemisferio == "S":
    if (mes == 12 and dia >= 21) or (mes in [1, 2]) or (mes == 3 and dia <= 20):
        estacion = "Verano"
    elif (mes == 3 and dia >= 21) or (mes in [4, 5]) or (mes == 6 and dia <= 20):
        estacion = "Otoño"
    elif (mes == 6 and dia >= 21) or (mes in [7, 8]) or (mes == 9 and dia <= 20):
        estacion = "Invierno"
    elif (mes == 9 and dia >= 21) or (mes in [10, 11]) or (mes == 12 and dia <= 20):
        estacion = "Primavera"
    else:
        estacion = "Fecha invalida"

else:
    estacion = "Hemisferio no valido"

print("Estacin del año:", estacion)

