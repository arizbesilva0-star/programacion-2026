"""
Created on Abril, 2026
@author: arizbesilva0-star
"""

class Cliente:

    def __init__(self, nombre):
        self.nombre = nombre
        self.cuentas = []

    def agregarCuenta(self, cuenta):
        self.cuentas.append(cuenta)

    def eliminarCuenta(self, indice):
        if 0 <= indice < len(self.cuentas):
            self.cuentas.pop(indice)
        else:
            print("Indice invalido")

    def recuperarCuenta(self, indice):
        if 0 <= indice < len(self.cuentas):
            return self.cuentas[indice]
        else:
            print("Indice invalido")
            return None

    def mostrarCuentas(self):
        if len(self.cuentas) == 0:
            print("No hay cuentas registradas")
        else:
            for i, cta in enumerate(self.cuentas):
                print(i, "-", cta)

    def __str__(self):
        return "Cliente: " + self.nombre + " | Total cuentas: " + str(len(self.cuentas))
