#punto 1
def saludar ():
    print("Hola mundo")
saludar()

#punto2
def saludarPersonalizado (nombre):
    print(f"Hola {nombre}!")

saludarPersonalizado(input("Ingrese su nombre"))

#punto3
name = input("Ingrese su nombre")
lastName = input("Ingrese su apellido")
age = int(input("Ingrese su edad"))
place = input("Ingrese su lugar de residencia")

def infoPersonal (nombre,apellido,edad,residencia):
    print(f"Soy {nombre} {apellido},tengo {edad} y vivo en {residencia}")

infoPersonal(name,lastName,age,place)

#punto4
def calcular_area_circulo(radio):
    area = 3.14 * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * 3.14 * radio
    return perimetro

solicitarRadio = int(input("Escribe el radio: "))

area = calcular_area_circulo(solicitarRadio)
perimetro = calcular_perimetro_circulo(solicitarRadio)

print(f"El area del circulo es {area} y el perimetro es {perimetro}")

#punto5

segundosIngresados = int(input("Ingresar segundos"))

def segundos_a_horas(segundos):
    transformacion = (segundos // 3600)
    return transformacion

horas = segundos_a_horas(segundosIngresados)

print(f"La cantidad de horas es {horas}")

#punto6

numeroAMultiplicar = int(input("Escribe un numero"))

def tabla_multiplicar(numero):
    for numeroMulti in range (0,11):
        resultado = (numero * numeroMulti)
        print(f"{numeroAMultiplicar}*{numeroMulti} = {resultado}")


tabla_multiplicar(numeroAMultiplicar)

#PUNTO 7
aA = int(input("Escribe tu peso actual"))
bB = int(input("Escribe tu altura actual"))

def operaciones_basicas(a,b):
    suma = (a + b)
    resta = (a - b)
    division = ( a / b )
    multipli = (a * b)
    print(f"El resultado de la suma entre {a} y {b} es {suma}.El resultado de la resta entre {a} y {b} es {resta}.El resultado de la division entre {a} y {b} es {division}.El resultado de la multiplicacion entre {a} y {b} es {multipli}")

operaciones_basicas(aA,bB)

#PUNTO 8

def calcular_imc(peso, altura):
    return peso / (altura ** 2)

peso_usuario = float(input("Escribe tu peso en kilogramos"))
altura_usuario = float(input("Escribe tu altura en metros"))

imc = calcular_imc(peso_usuario, altura_usuario)
print(f"Tu IMC es {imc}")

#PTUNO 9

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

temp_celsius = float(input("Escribe la temperatura en grados celsius"))

fahrenheit = celsius_a_fahrenheit(temp_celsius)
print(f"La temperatura en fahrenheit es {fahrenheit}")

#PUNTO 10
def calcular_promedio(a, b, c):
    return (a + b + c) / 3

num1 = float(input("Escribe el primer numero"))
num2 = float(input("Escribe el segundo numero"))
num3 = float(input("Escribe el tercer numero"))

promedio = calcular_promedio(num1, num2, num3)
print(f"El promedio es {promedio}")









