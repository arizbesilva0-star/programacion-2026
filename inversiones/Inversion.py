"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Inversion:

    def __init__(self, capital, interes, tiempo, nombre):
        self.capital = capital
        self.interes = interes
        self.tiempo = tiempo
        self.nombre = nombre

    # Aumentar capital
    def aumentar(self, cantidad):
        if cantidad <= 0:
            return False
        self.capital = self.capital + cantidad
        return True

    # Disminuir capital
    def disminuir(self, cantidad):
        if cantidad <= 0 or cantidad > self.capital:
            return False
        self.capital = self.capital - cantidad
        return True

    # Calcular monto final
    def calcular(self):
        monto = self.capital * (1 + self.interes * self.tiempo)
        return monto

    # Mostrar datos (sin print)
    def mostrar(self):
        return self.nombre, self.capital, self.interes, self.tiempo
