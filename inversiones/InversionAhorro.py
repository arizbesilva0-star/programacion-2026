"""
Created on June, 2026
@author: arizbesilva-star
"""

from Inversion import Inversion


class InversionAhorro(Inversion):

    def __init__(
        self,
        saldo,
        interes,
        tiempo,
        nombre
    ):

        super().__init__(
            saldo,
            interes,
            tiempo,
            nombre
        )

    def calcular(self):

        rendimiento = super().calcular()

        bono = (
            self._saldo * 0.02
        )

        return (
            rendimiento
            + bono
        )

    def __str__(self):

        cadena = ""

        cadena += (
            "\nTipo: Inversion de Ahorro"
        )

        cadena += (
            super().__str__()
        )

        return cadena