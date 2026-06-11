"""
Created on June, 2026
@author: arizbesilva-star
"""
class Inversion:

    def __init__(
        self,
        saldo,
        interes,
        tiempo,
        nombre
    ):

        self._saldo = saldo

        self._interes = interes

        self._tiempo = tiempo

        self._nombre = nombre

    def aumentar(
        self,
        cantidad
    ):

        if cantidad > 0:

            self._saldo += cantidad

            return True

        return False

    def disminuir(
        self,
        cantidad
    ):

        if (
            cantidad > 0
            and
            cantidad <= self._saldo
        ):

            self._saldo -= cantidad

            return True

        return False

    def calcular(self):

        return (
            self._saldo
            *
            (
                1
                +
                self._interes
                *
                self._tiempo
            )
        )

    def recuperarNombre(self):

        return self._nombre

    def recuperarSaldo(self):

        return self._saldo

    def recuperarInteres(self):

        return self._interes

    def recuperarTiempo(self):

        return self._tiempo

    def mostrar(self):

        return (

            self._nombre,

            self._saldo,

            self._interes,

            self._tiempo
        )

    def __str__(self):

        cadena = ""

        cadena += (
            "\nNombre: "
            + self._nombre
        )

        cadena += (
            "\nSaldo: "
            + str(
                self._saldo
            )
        )

        cadena += (
            "\nInteres: "
            + str(
                self._interes
            )
        )

        cadena += (
            "\nTiempo: "
            + str(
                self._tiempo
            )
            + " meses"
        )

        return cadena
