"""
Created on June, 2026
@author: arizbesilva-star
"""

class Cliente:

    def __init__(self, nombre, direccion, edad):

        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad

        self.__cuentas = []

    def agregarCuenta(self, cuenta):

        if self.recuperarCuenta(
            cuenta.recuperarNombre()
        ) is None:

            self.__cuentas.append(cuenta)

            return True

        return False

    def borrarCuenta(self, nombre):

        cuenta = self.recuperarCuenta(nombre)

        if cuenta:

            self.__cuentas.remove(cuenta)

            return True

        return False

    def recuperarCuenta(self, nombre):

        for cuenta in self.__cuentas:

            if (
                cuenta.recuperarNombre()
                == nombre
            ):

                return cuenta

        return None

    def mostrarCuentas(self):

        if len(self.__cuentas) == 0:

            print(
                "No hay inversiones registradas"
            )

        else:

            for cuenta in self.__cuentas:

                print(cuenta)

                print(
                    "-" * 50
                )

    def ordenarPorSaldo(self):

        self.__cuentas.sort(
            key=lambda cuenta:
            cuenta.recuperarSaldo()
        )

    def recuperarNombre(self):

        return self.__nombre

    def recuperarDireccion(self):

        return self.__direccion

    def recuperarEdad(self):

        return self.__edad

    def recuperarCuentas(self):

        return self.__cuentas

    def cantidadInversiones(self):

        return len(
            self.__cuentas
        )

    def totalInvertido(self):

        suma = 0

        for cuenta in self.__cuentas:

            suma += (
                cuenta.recuperarSaldo()
            )

        return suma

    def promedioInvertido(self):

        if (
            len(self.__cuentas)
            == 0
        ):

            return 0

        return (
            self.totalInvertido()
            /
            len(self.__cuentas)
        )

    def __str__(self):

        cadena = ""

        cadena += (
            "\nNombre: "
            + self.__nombre
        )

        cadena += (
            "\nDireccion: "
            + self.__direccion
        )

        cadena += (
            "\nEdad: "
            + str(self.__edad)
        )

        cadena += (
            "\nCantidad de inversiones: "
            + str(
                self.cantidadInversiones()
            )
        )

        return cadena