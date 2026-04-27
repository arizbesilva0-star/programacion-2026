"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from cuenta import Cuenta
from cliente import Cliente
from menu import Menu

def main():

    menu = Menu("Bienvenido al Banco Pato")

    cuenta1 = Cuenta(300, "debito", "12/02/2019")
    cliente1 = Cliente("Arizbe", cuenta1)

    menu.bienvenida()

    while True:

        opcion = menu.opciones()

        if opcion == "1":

            while True:
                try:
                    cant = float(input("Ingrese la cantidad a depositar: $"))

                    if cuenta1.depositar(cant):
                        print("Deposito realizado con exito")
                        print("Saldo actual: $", cuenta1.saldo)
                        break
                    else:
                        print("La cantidad debe ser mayor a 0")

                except:
                    print("Entrada invalida, intenta de nuevo")

        elif opcion == "2":

            while True:
                try:
                    cant = float(input("Ingrese la cantidad a retirar: $"))

                    if cuenta1.retirar(cant):
                        print("Retiro realizado con exito")
                        print("Saldo actual: $", cuenta1.saldo)
                        break
                    else:
                        print("Fondos insuficientes o cantidad invalida")

                except:
                    print("Entrada invalida, intenta de nuevo")

        elif opcion == "3":
            print("\n--- Informacion de la cuenta ---")
            print(cliente1)

        elif opcion == "4":
            print("Sesion finalizada")
            break

        else:
            print("Opcion invalida")


if __name__ == "__main__":
    main()
