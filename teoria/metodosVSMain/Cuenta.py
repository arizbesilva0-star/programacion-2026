"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Cuenta:

    def __init__(self, saldo, tipo, fechaCreacion):
        self.saldo = saldo
        self.tipo = tipo
        self.fechaCreacion = fechaCreacion

    def depositar(self, cantidad):
        if cantidad <= 0:
            return False
        self.saldo += cantidad
        return True

    def retirar(self, cantidad):
        if cantidad > self.saldo:
            return False
        self.saldo -= cantidad
        return True

    def __str__(self):
        return "Saldo: " + str(self.saldo) + ", Tipo: " + self.tipo
