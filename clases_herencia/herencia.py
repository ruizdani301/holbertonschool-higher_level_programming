#!/usr/bin/python3
"""Prueba clases"""
class Vehiculo():
    """variable clase"""
    def __init__(self, marca, color, placa, modelo):
    #propiedades
        self.marca = marca
        self.color = color
        self.placa = placa
        self.modelo = modelo

    def acelerar(self):
        print(f"soy {self.marca}, estoy acelerado!!")

    def frenar(self):
        print(f"soy {self.marca}, me frene")

    def voltear(self, direccion):
        print(f"Soy {self.marca}, estoy volteando a la {direccion}")

    def __str__(self):
        return self.marca

#Vamos a crear clases hijas heredando de vehiculo
class Carro (Vehiculo):
	numero_llantas = 4

	def tocar_claxon(self):
		print(f"soy {self.marca}, y estoy claxiando")

class Motocicleta (Vehiculo):
	numero_llantas = 2

	def de_patada(self):
		print(f"soy {self.marca}, y soy de patada")

class Avion (Vehiculo):
	numero_llantas = 32

	def sacar_llantas(self):
		print(f"soy {self.marca}, y me saco las llantas")
	def aterrizaje(self):
		print(f"soy {self.marca}, y aterrizo")


#Vamos a instanciar y a hacer pruebas...
# Crear objetos ....

obj_mazda = Carro("mazda", "gris", "OST06", "2020")#por q lo defino como string el numero
obj_audi = Carro("audi", "rojo", "PGY01", "2021")

# Creamos Objetos Motocicleta...
obj_honda = Motocicleta("honda cb", "negro", "ost06", "2018")
obj_suzuki = Motocicleta("Yamaha", "azul", "pgy01c", "2019")

# Creamos objeto Avion...
obj_jet = Avion("jet privado", "blanco", "PQR", "2017")
#*******************************************************
# zona de impresion.
# Llamemos algunos metodos
print(obj_mazda)
print(obj_audi)
obj_mazda.voltear("izquierda")#Cuando se llama el metodo no se usa el self
obj_audi.voltear("derecha")
obj_mazda.acelerar()
obj_audi.frenar()

# Honda va a encender con patada...
obj_honda.de_patada()

# suzuki gira a la derecha
obj_suzuki.voltear("derecha")

# el jet va a terrizar...
obj_jet.aterrizaje()