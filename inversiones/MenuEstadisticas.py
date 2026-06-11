"""
Created on June, 2026
@author: arizbesilva-star
"""
class MenuEstadisticas:

    def mostrar(self):

        print("\n" + "-" * 60)
        print("MENU ESTADISTICAS".center(60))
        print("-" * 60)

        print("1) Estadisticas de cliente")
        print("2) Estadisticas del banco")
        print("3) Grafica")
        print("4) Regresar")

        print("-" * 60)

        return input(
            "Selecciona una opcion: "
        )

    def encabezado(self):

        print("\n" + "=" * 60)

        print(
            "ESTADISTICAS"
            .center(60)
        )

        print("=" * 60)
