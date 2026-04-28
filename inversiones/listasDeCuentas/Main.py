"""
Created on April, 2026
@author: arizbesilva-star
"""

from Inversion import Inversion
from Cliente import Cliente
from Menu import Menu

cliente1 = Cliente("Arizbe", "CDMX", 20)

# ahora las inversiones se agregan al cliente
inversion1 = Inversion(1000, 0.10, 2, "Inversion BBVA")
inversion2 = Inversion(2000, 0.15, 1, "Inversion Banamex")

cliente1.agregarCuenta(inversion1)
cliente1.agregarCuenta(inversion2)

menu = Menu("Sistema de inversiones")

menu.bienvenida()

while True:

    opcion = menu.opciones().strip()

    if opcion == "1":
        nombre = input("Nombre de la cuenta: ")
        cuenta = cliente1.recuperarCuenta(nombre)
        if cuenta:
            try:
                cantidad = float(input("Cantidad a aumentar: "))
                if cuenta.aumentar(cantidad):
                    print("Cantidad aumentada")
            except ValueError:
                print("Ingresa un numero valido")
        else:
            print("Cuenta no encontrada")

    elif opcion == "2":
        nombre = input("Nombre de la cuenta: ")
        cuenta = cliente1.recuperarCuenta(nombre)
        if cuenta:
            try:
                cantidad = float(input("Cantidad a disminuir: "))
                if cuenta.disminuir(cantidad):
                    print("Cantidad disminuida")
            except ValueError:
                print("Ingresa un numero valido")
        else:
            print("Cuenta no encontrada")

    elif opcion == "3":
        nombre = input("Nombre de la cuenta: ")
        cuenta = cliente1.recuperarCuenta(nombre)
        if cuenta:
            resultado = cuenta.calcular()
            print("Monto final de la inversion:", resultado)
        else:
            print("Cuenta no encontrada")

    elif opcion == "4":
        cliente1.mostrarCuentas()

    elif opcion == "5":
        print(cliente1)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opcion no valida")
