"""
Created on Abril, 2026
@author: arizbesilva0-star
"""

from Cuenta import *
from Cliente import *

class MenuCliente:

    def __init__(self):
        self.__cliente = Cliente("Arizbe")

        # Cuenta inicial
        cuenta1 = Cuenta(300, "debito", "12/02/2019")
        self.__cliente.agregarCuenta(cuenta1)

    def menu(self):

        while True:

            print("\n--- MENU CLIENTE ---")
            print("1. Depositar")
            print("2. Retirar")
            print("3. Mostrar cuentas")
            print("4. Agregar cuenta")
            print("5. Eliminar cuenta")
            print("6. Salir")

            opcion = input("Opcion: ")

            # -------- DEPOSITAR --------
            if opcion == "1":
                self.__cliente.mostrarCuentas()
                try:
                    i = int(input("Seleccione cuenta: "))
                    cuenta = self.__cliente.recuperarCuenta(i)

                    if cuenta:
                        cant = float(input("Cantidad: "))
                        if cuenta.depositar(cant):
                            print("Deposito exitoso")
                        else:
                            print("Cantidad invalida")
                except:
                    print("Error")

            # -------- RETIRAR --------
            elif opcion == "2":
                self.__cliente.mostrarCuentas()
                try:
                    i = int(input("Seleccione cuenta: "))
                    cuenta = self.__cliente.recuperarCuenta(i)

                    if cuenta:
                        cant = float(input("Cantidad: "))
                        if cuenta.retirar(cant):
                            print("Retiro exitoso")
                        else:
                            print("Fondos insuficientes")
                except:
                    print("Error")

            # -------- MOSTRAR --------
            elif opcion == "3":
                self.__cliente.mostrarCuentas()

            # -------- AGREGAR --------
            elif opcion == "4":
                try:
                    saldo = float(input("Saldo inicial: "))
                    tipo = input("Tipo: ")
                    fecha = input("Fecha: ")

                    nueva = Cuenta(saldo, tipo, fecha)
                    self.__cliente.agregarCuenta(nueva)

                    print("Cuenta agregada")
                except:
                    print("Error")

            # -------- ELIMINAR --------
            elif opcion == "5":
                self.__cliente.mostrarCuentas()
                try:
                    i = int(input("Indice: "))
                    self.__cliente.eliminarCuenta(i)
                except:
                    print("Error")

            # -------- SALIR --------
            elif opcion == "6":
                print("Sesion finalizada")
                break

            else:
                print("Opcion invalida")
