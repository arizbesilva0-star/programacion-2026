"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from Inversion import *
from Menu import *

menu = Menu("Bienvenido al Sistema de Inversiones")

inversion1 = Inversion(1000, 0.05, 12, "Inversion Banco BBVA")

menu.bienvenida()

while True:

    opcion = menu.opciones()

    if opcion == "1":
        try:
            cantidad = float(input("Cantidad a aumentar: "))
        except:
            print("Error: ingresa un numero valido")
            continue

        if inversion1.aumentar(cantidad):
            print("Capital actualizado:", inversion1.capital)
        else:
            print("Error en la cantidad")

    elif opcion == "2":
        try:
            cantidad = float(input("Cantidad a disminuir: "))
        except:
            print("Error: ingresa un numero valido")
            continue

        if inversion1.disminuir(cantidad):
            print("Capital actualizado:", inversion1.capital)
        else:
            print("Error: saldo insuficiente o cantidad invalida")

    elif opcion == "3":
        resultado = inversion1.calcular()
        print("Monto final de la inversion:", resultado)

    elif opcion == "4":
        nombre, capital, interes, tiempo = inversion1.mostrar()
        print("Nombre:", nombre)
        print("Capital:", capital)
        print("Interes:", interes)
        print("Tiempo:", tiempo, "meses")

    elif opcion == "5":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion no valida")
