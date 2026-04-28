"""
Created on April, 2026
@author: arizbesilva-star
"""

class Cliente:

    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuentas = []  # lista de cuentas (Inversion)

    def agregarCuenta(self, cuenta):
        self.__cuentas.append(cuenta)

    def borrarCuenta(self, nombre):
        for cuenta in self.__cuentas:
            if cuenta.mostrar()[0] == nombre:
                self.__cuentas.remove(cuenta)
                return True
        return False

    def recuperarCuenta(self, nombre):
        for cuenta in self.__cuentas:
            if cuenta.mostrar()[0] == nombre:
                return cuenta
        return None

    def mostrarCuentas(self):
        if len(self.__cuentas) == 0:
            print("No hay cuentas registradas")
        else:
            for cuenta in self.__cuentas:
                nombre, saldo, interes, tiempo = cuenta.mostrar()
                print("\nNombre:", nombre)
                print("Saldo:", saldo)
                print("Interes:", interes)
                print("Tiempo:", tiempo, "meses")

    def __str__(self):
        texto = ""
        texto += "Nombre: " + self.__nombre + "\n"
        texto += "Direccion: " + self.__direccion + "\n"
        texto += "Edad: " + str(self.__edad)
        return texto
