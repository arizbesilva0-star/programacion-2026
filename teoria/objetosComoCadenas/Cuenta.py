"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Cuenta:

    def __init__(self, saldo, tipo):
        self.saldo = saldo
        self.tipo = tipo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.saldo += cantidad

    def __str__(self):
        return "Saldo: " + str(self.saldo) + ", Tipo: " + self.tipo
