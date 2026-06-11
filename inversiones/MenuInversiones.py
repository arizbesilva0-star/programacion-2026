"""
Created on June, 2026
@author: arizbesilva-star
"""

class MenuInversiones:

    def mostrar(self):

        print("\n" + "-" * 60)
        print("MENU INVERSIONES".center(60))
        print("-" * 60)

        print("1) Crear inversion")
        print("2) Depositar dinero")
        print("3) Retirar dinero")
        print("4) Calcular rendimiento")
        print("5) Mostrar inversiones")
        print("6) Ordenar inversiones")
        print("7) Regresar")

        print("-" * 60)

        return input(
            "Selecciona una opcion: "
        )

    def solicitarDatosInversion(self):

        nombre = input(
            "Nombre de la inversion: "
        )

        saldo = float(
            input(
                "Saldo inicial: "
            )
        )

        interes = float(
            input(
                "Interes (0.10): "
            )
        )

        tiempo = int(
            input(
                "Tiempo en meses: "
            )
        )

        return (
            nombre,
            saldo,
            interes,
            tiempo
        )

    def solicitarTipoInversion(self):

        print("\nTipos de inversion")

        print("1) Inversion Ahorro")

        print("2) Inversion Plazo Fijo")

        return input(
            "Selecciona una opcion: "
        )

    def solicitarCantidad(self):

        return float(
            input(
                "Cantidad: "
            )
        )