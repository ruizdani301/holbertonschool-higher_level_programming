#!/usr/bin/python3
"""Prueba clases"""
class Carro():
    """variable clase"""
    vehiculo = "carro"
    def __init__(self, marca, color, placa, modelo):
    #propiedades
        self.marca = marca
        self.color = color
        self.placa = placa
        self.modelo = modelo
        self.numero_llanta = 4
    #PORQ LA " f "ANTES DEL SOY
    def acelerar(self):
        print(f"soy {self.marca}, estoy acelerado!!")

    def frenar(self):
        print(f"soy {self.marca}, me frene")

    def voltear(self, direccion):
        print(f"Soy {self.marca}, estoy volteando a la {direccion}")

    def __str__(self):
        return self.marca
# Objeto carro, se instancia un nivel de sangría atrás, fuera de la clase.

Obj_mazda = Carro("mazda", "gris", "OST06", "2020")#por q lo defino como string el numero
Obj_audi = Carro("audi", "rojo", "PGY01", "2021")

print(Obj_mazda)
print(Obj_audi)

Obj_mazda.voltear("izquierda")#Cuando se llama el metodo no se usa el self
Obj_audi.voltear("derecha")
Obj_mazda.acelerar()
Obj_audi.frenar()


