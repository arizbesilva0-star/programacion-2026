"""
Created on March, 2026
@author: arizbesilva-star
"""

from Inversion import Inversion
from Cliente import Cliente
from Menu import Menu

cliente1 = Cliente("Arizbe", "CDMX", 20)
inversion1 = Inversion(1000, 0.10, 2, "Inversion BBVA")

menu = Menu("Sistema de inversiones")

menu.bienvenida()

while True:

    opcion = menu.opciones().strip()  # evita errores por espacios

    if opcion == "1":
        try:
            cantidad = float(input("Cantidad a aumentar: "))
            if inversion1.aumentar(cantidad):
                print("Cantidad aumentada")
        except ValueError:
            print("Ingresa un numero valido")

    elif opcion == "2":
        try:
            cantidad = float(input("Cantidad a disminuir: "))
            if inversion1.disminuir(cantidad):
                print("Cantidad disminuida")
        except ValueError:
            print("Ingresa un numero valido")

    elif opcion == "3":
        resultado = inversion1.calcular()
        print("Monto final de la inversion:", resultado)

    elif opcion == "4":
        nombre, saldo, interes, tiempo = inversion1.mostrar()
        print("Nombre:", nombre)
        print("Saldo:", saldo)
        print("Interes:", interes)
        print("Tiempo:", tiempo, "meses")

    elif opcion == "5":
        print(cliente1)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion no valida")
