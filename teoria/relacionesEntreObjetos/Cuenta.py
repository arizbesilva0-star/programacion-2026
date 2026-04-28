"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Cuenta:

    def __init__(self, cantidad, tipo):
        self.cantidad = cantidad
        self.tipo = tipo

    def depositar(self, valor):
        if valor > 0:
            self.cantidad = self.cantidad + valor
        else:
            print("valor incorrecto")

    def mostrarDetalles(self):
        print("Cantidad::", self.cantidad)
        print("Tipo::", self.tipo)
