"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Cliente:

    def __init__(self, nombre, direccion, edad, cuenta):
        self.nombre = nombre
        self.direccion = direccion
        self.edad = edad
        self.cuenta = cuenta

    def mostrarDetalles(self):
        print("Nombre:", self.nombre)
        print("Direccion:", self.direccion)
        print("Edad:", self.edad)
        print("Tipo de cuenta:", self.cuenta.getTipo())
        print("Saldo:", self.cuenta.getSaldo())
