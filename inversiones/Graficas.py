"""
Created on June, 2026
@author: arizbesilva-star
"""

import matplotlib.pyplot as plt


class Graficas:

    def graficaInversionesClientes(self, banco):

        clientes = banco.recuperarClientes()

        if len(clientes) == 0:
            print("No hay datos para graficar")
            return

        nombres = []
        inversiones = []

        for cliente in clientes:

            nombres.append(cliente.recuperarNombre())
            inversiones.append(cliente.totalInvertido())

        plt.figure(figsize=(8, 5))

        plt.bar(nombres, inversiones)

        plt.title("Inversion total por cliente")

        plt.xlabel("Clientes")

        plt.ylabel("Monto invertido")

        plt.xticks(rotation=45)

        plt.tight_layout()

        plt.show()