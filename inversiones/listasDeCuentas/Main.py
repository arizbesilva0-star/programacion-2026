"""
Created on April, 2026
@author: arizbesilva-star
"""

from Cliente import Cliente
from Inversion import Inversion
from Menu import Menu

cliente1 = Cliente("Arizbe", "CDMX", 20)

menu = Menu("Sistema de Inversiones")
menu.bienvenida()

while True:

    opcion = menu.opciones().strip()

    if opcion == "1":
        nombre = input("Nombre de la cuenta: ")
        saldo = float(input("Saldo inicial: "))
        interes = float(input("Interes (ej. 0.10): "))
        tiempo = int(input("Tiempo (meses): "))

        nueva = Inversion(saldo, interes, tiempo, nombre)
        if cliente1.agregarCuenta(nueva):
            print("Cuenta creada exitosamente")

    elif opcion == "2":
        nombre = input("Nombre de la cuenta a eliminar: ")
        if cliente1.borrarCuenta(nombre):
            print("Cuenta eliminada correctamente")

    elif opcion == "3":
        nombre = input("Nombre de la cuenta: ")
        cuenta = cliente1.recuperarCuenta(nombre)
        if cuenta:
            cantidad = float(input("Cantidad a depositar: "))
            if cuenta.aumentar(cantidad):
                print("Deposito realizado con exito")
        else:
            print("Cuenta no encontrada")

    elif opcion == "4":
        nombre = input("Nombre de la cuenta: ")
        cuenta = cliente1.recuperarCuenta(nombre)
        if cuenta:
            cantidad = float(input("Cantidad a retirar: "))
            if cuenta.disminuir(cantidad):
                print("Retiro realizado con exito")
        else:
            print("Cuenta no encontrada")

    elif opcion == "5":
        nombre = input("Nombre de la cuenta: ")
        cuenta = cliente1.recuperarCuenta(nombre)
        if cuenta:
            print("El monto final de la inversion es:", cuenta.calcular())
        else:
            print("Cuenta no encontrada")

    elif opcion == "6":
        cliente1.mostrarCuentas()

    elif opcion == "7":
        cliente1.ordenarPorSaldo()

    elif opcion == "8":
        print("\n" + "-"*50)
        print(cliente1)
        print("-"*50)

    elif opcion == "9":
        print("\nGuardando informacion...")
        print("Cerrando sesion...")
        print("Gracias por usar el sistema de inversiones")
        print("=" * 50)
        break

    else:
        print("Opcion no valida")
