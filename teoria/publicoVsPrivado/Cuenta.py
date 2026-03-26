"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Cuenta:

    def __init__(self, saldo, tipo, fechaCreacion):
        # ATRIBUTOS PRIVADOS (no se pueden acceder directamente desde fuera)
        self.__saldo = saldo
        self.__tipo = tipo
        self.__fechaCreacion = fechaCreacion

    def depositar(self, cantidad):
        # MÉTODO PÚBLICO
        if cantidad <= 0:
            return False
        self.__saldo += cantidad
        return True

    def retirar(self, cantidad):
        # MÉTODO PÚBLICO
        if cantidad > self.__saldo:
            return False
        self.__saldo -= cantidad
        return True

    # GETTERS (métodos públicos para acceder a atributos privados)
    def getSaldo(self):
        return self.__saldo

    def getTipo(self):
        return self.__tipo

    def __str__(self):
        # MÉTODO PÚBLICO
        return "Saldo: " + str(self.__saldo) + ", Tipo: " + self.__tipo