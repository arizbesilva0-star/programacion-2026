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

    def __str__(self):
        tmp = "Cliente: " + self.nombre + "\n"
        tmp += "Direccion: " + self.direccion + "\n"
        tmp += "Edad: " + str(self.edad) + "\n"
        tmp += "Tipo de cuenta: " + self.cuenta.getTipo() + "\n"
        tmp += "Saldo: " + str(self.cuenta.getSaldo())
        return tmp
