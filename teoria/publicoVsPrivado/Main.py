"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from Cuenta import *
from Cliente import *
from Menu import *

menu = Menu("Bienvenido al Banco Pato")

cuenta1 = Cuenta(300, "debito", "12/02/2019")
cliente1 = Cliente("Arizbe", cuenta1)

menu.bienvenida()

while True:

    opcion = menu.opciones()

    if opcion == "1":
        try:
            cant = float(input("Ingrese la cantidad a depositar: $"))
            if cuenta1.depositar(cant):
                print("Deposito realizado con exito")
                print("Saldo actual: $", cuenta1.getSaldo())
            else:
                print("Operacion no valida. El monto debe ser mayor a cero")
        except:
            print("Entrada invalida. Ingrese un numero")

    elif opcion == "2":
        try:
            cant = float(input("Ingrese la cantidad a retirar: $"))
            if cuenta1.retirar(cant):
                print("Retiro realizado con exito")
                print("Saldo actual: $", cuenta1.getSaldo())
            else:
                print("Fondos insuficientes o monto invalido")
        except:
            print("Entrada invalida. Ingrese un numero")

    elif opcion == "3":
        print("\n--- Informacion de la cuenta ---")
        print(cliente1)

    elif opcion == "4":
        print("\nGracias por confiar en nuestro banco")
        print("Sesion finalizada correctamente")
        break

    else:
        print("Opcion invalida. Seleccione una opcion del menu")
