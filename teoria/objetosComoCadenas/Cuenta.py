"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Cuenta:

    def __init__(self, saldo, tipo):
        self.__saldo = saldo
        self.__tipo = tipo

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad

    def getSaldo(self):
        return self.__saldo

    def getTipo(self):
        return self.__tipo

    def __str__(self):
        return "Saldo: " + str(self.__saldo) + ", Tipo: " + self.__tipo
