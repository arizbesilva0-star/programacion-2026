"""
Created on April, 2026
@author: arizbesilva-star
"""

class Cliente:

    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad
        self.__cuentas = []

    def agregarCuenta(self, cuenta):
        if self.recuperarCuenta(cuenta.mostrar()[0]) is None:
            self.__cuentas.append(cuenta)
            return True
        else:
            print("La cuenta ya existe")
            return False

    def borrarCuenta(self, nombre):
        cuenta = self.recuperarCuenta(nombre)
        if cuenta:
            self.__cuentas.remove(cuenta)
            return True
        else:
            print("Cuenta no encontrada")
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
                print("\n" + "-"*40)
                print("Nombre:", nombre)
                print("Saldo:", saldo)
                print("Interes:", interes)
                print("Tiempo:", tiempo, "meses")
                print("-"*40)

    def ordenarPorSaldo(self):
        self.__cuentas.sort(key=lambda c: c.mostrar()[1])
        print("Cuentas ordenadas por saldo")

    def __str__(self):
        texto = ""
        texto += "Nombre: " + self.__nombre + "\n"
        texto += "Direccion: " + self.__direccion + "\n"
        texto += "Edad: " + str(self.__edad)
        return texto
