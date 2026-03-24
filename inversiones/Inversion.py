"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Inversion:

    def __init__(self, saldo, interes, tiempo, nombre):
        self.__saldo = saldo
        self.__interes = interes
        self.__tiempo = tiempo
        self.__nombre = nombre

    def aumentar(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            return True
        else:
            print("Error")
            return False

    def disminuir(self, cantidad):
        if cantidad > 0 and cantidad <= self.__saldo:
            self.__saldo -= cantidad
            return True
        else:
            print("Error")
            return False

    def calcular(self):
        return self.__saldo * (1 + self.__interes * self.__tiempo)

    def mostrar(self):
        return self.__nombre, self.__saldo, self.__interes, self.__tiempo
