import math
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 
1450}

#PUNTO 1
precios_frutas["naranja"] = 1200
precios_frutas["manzana"] = 1500
precios_frutas["pera"] = 2300


#PUNTO 2
precios_frutas["Banana"] = 1330
precios_frutas["manzana"] = 1700
precios_frutas["Melón"] = 2800

#PUNTO 3
print(precios_frutas.keys())
frutas = (['Banana', 'Ananá', 'Melón', 'Uva', 'naranja', 'manzana', 'pera'])

#PUNTO 4
class Persona:
    def __init__(self,nombre,pais,edad):
        self.nombre = nombre
        self.pais = pais
        self.edad = edad

    def saludar(self):
        print(f"Hola soy {self.nombre},vivo en {self.pais} y tengo {self.edad} años.")

#PUNTO 5

import math 

class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * (self.radio ** 2)

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio

mi_circulo = Circulo(5)

print(f"El area del circulo es {mi_circulo.calcular_area()}. El perimetro del circulo es {mi_circulo.calcular_perimetro()}")

#PUNTO 7

class Banco:
    def __init__(self):
        self.cola = []

    def encolar(self, cliente):
        self.cola.append(cliente)
        print(f"clente {cliente} agregado a la cola")

    def desencolar(self):
        if len(self.cola) == 0:
            print("No hay clientes en la cola")
        else:
            cliente = self.cola.pop(0)
            print(f"cliente {cliente} atendido")

    def siguiente(self):
        if len(self.cola) == 0:
            print("no hay clientes en la cola")
        else:
            print(f"El siguiente cliente en la fila es: {self.cola[0]}")

#PUNTO 8
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

#PUNTO 9
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def insertar_inicio(self, valor):
        nuevo_nodo = Nodo(valor)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo

    def recorrer(self):
        actual = self.cabeza
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")
    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente 
            actual.siguiente = anterior
            anterior = actual
            actual = siguiente   
        self.cabeza = anterior  






