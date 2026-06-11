"""
Created on June, 2026
@author: arizbesilva-star
"""
class MenuPrincipal:

    def mostrar(self):

        print("\n" + "-" * 60)
        print("MENU PRINCIPAL".center(60))
        print("-" * 60)

        print("1) Gestion de clientes")
        print("2) Gestion de inversiones")
        print("3) Estadisticas")
        print("4) Salir")

        print("-" * 60)

        return input(
            "Selecciona una opcion: "
        )
