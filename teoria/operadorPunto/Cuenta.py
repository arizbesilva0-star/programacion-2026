"""
Created on Febrero, 2019
@author: arizbesilva0-star
"""

class Cuenta:

    # Método constructor
    # Inicializa los atributos de la cuenta
    def __init__(self, saldo, tipo, fechaCreacion):
        self.saldo = saldo
        self.tipo = tipo
        self.fechaCreacion = fechaCreacion

    # Método para depositar dinero
    def depositar(self, cantidad):
        self.saldo = self.saldo + cantidad

    # Método para retirar dinero
    def retirar(self, cantidad):
        self.saldo = self.saldo - cantidad

    # Método para mostrar la información de la cuenta
    def imprimirDetalles(self):
        print("saldo:", self.saldo)
        print("tipo:", self.tipo)
        print("fechaCreacion:", self.fechaCreacion)