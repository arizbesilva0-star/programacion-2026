"""
Created on June, 2026
@author: arizbesilva-star
"""

from Banco import Banco
from Cliente import Cliente

from InversionAhorro import InversionAhorro
from InversionPlazoFijo import InversionPlazoFijo

from MenuPrincipal import MenuPrincipal
from MenuClientes import MenuClientes
from MenuInversiones import MenuInversiones
from MenuEstadisticas import MenuEstadisticas

from Graficas import Graficas


class Principal:
    pass

banco = Banco()
banco.cargarClientes()

menuPrincipal = MenuPrincipal()
menuClientes = MenuClientes()
menuInversiones = MenuInversiones()
menuEstadisticas = MenuEstadisticas()

graficas = Graficas()

print("=" * 60)
print("SISTEMA DE INVERSIONES".center(60))
print("=" * 60)

while True:

    opcionPrincipal = menuPrincipal.mostrar()

    if opcionPrincipal == "1":

        while True:

            opcionCliente = menuClientes.mostrar()

            if opcionCliente == "1":

                nombre, direccion, edad = menuClientes.solicitarDatosCliente()

                cliente = Cliente(nombre, direccion, edad)

                if banco.agregarCliente(cliente):
                    print("Cliente registrado correctamente")
                else:
                    print("El cliente ya existe")

            elif opcionCliente == "2":

                nombre = menuClientes.solicitarNombreCliente()

                if banco.borrarCliente(nombre):
                    print("Cliente eliminado correctamente")
                else:
                    print("Cliente no encontrado")

            elif opcionCliente == "3":

                banco.mostrarClientes()

            elif opcionCliente == "4":

                break

            else:

                print("Opcion no valida")

    elif opcionPrincipal == "2":

        while True:

            opcionInversion = menuInversiones.mostrar()

            if opcionInversion == "1":

                nombreCliente = input("Nombre del cliente: ")

                cliente = banco.recuperarCliente(nombreCliente)

                if cliente:

                    nombre, saldo, interes, tiempo = menuInversiones.solicitarDatosInversion()
                    tipo = menuInversiones.solicitarTipoInversion()

                    if tipo == "1":
                        cuenta = InversionAhorro(saldo, interes, tiempo, nombre)
                    else:
                        cuenta = InversionPlazoFijo(saldo, interes, tiempo, nombre)

                    cliente.agregarCuenta(cuenta)

                    print("Inversion registrada")

                else:

                    print("Cliente no encontrado")

            elif opcionInversion == "2":

                nombreCliente = input("Nombre del cliente: ")

                cliente = banco.recuperarCliente(nombreCliente)

                if cliente:

                    nombreCuenta = input("Nombre de la inversion: ")

                    cuenta = cliente.recuperarCuenta(nombreCuenta)

                    if cuenta:

                        cantidad = menuInversiones.solicitarCantidad()

                        if cuenta.aumentar(cantidad):
                            print("Deposito realizado")

                    else:

                        print("Inversion no encontrada")

                else:

                    print("Cliente no encontrado")

            elif opcionInversion == "3":

                nombreCliente = input("Nombre del cliente: ")

                cliente = banco.recuperarCliente(nombreCliente)

                if cliente:

                    nombreCuenta = input("Nombre de la inversion: ")

                    cuenta = cliente.recuperarCuenta(nombreCuenta)

                    if cuenta:

                        cantidad = menuInversiones.solicitarCantidad()

                        if cuenta.disminuir(cantidad):
                            print("Retiro realizado")

                    else:

                        print("Inversion no encontrada")

                else:

                    print("Cliente no encontrado")

            elif opcionInversion == "4":

                nombreCliente = input("Nombre del cliente: ")

                cliente = banco.recuperarCliente(nombreCliente)

                if cliente:

                    nombreCuenta = input("Nombre de la inversion: ")

                    cuenta = cliente.recuperarCuenta(nombreCuenta)

                    if cuenta:
                        print("Monto final:", cuenta.calcular())

                    else:
                        print("Inversion no encontrada")

                else:

                    print("Cliente no encontrado")

            elif opcionInversion == "5":

                nombreCliente = input("Nombre del cliente: ")

                cliente = banco.recuperarCliente(nombreCliente)

                if cliente:
                    cliente.mostrarCuentas()

                else:
                    print("Cliente no encontrado")

            elif opcionInversion == "6":

                nombreCliente = input("Nombre del cliente: ")

                cliente = banco.recuperarCliente(nombreCliente)

                if cliente:
                    cliente.ordenarPorSaldo()
                    print("Inversiones ordenadas")

                else:
                    print("Cliente no encontrado")

            elif opcionInversion == "7":

                break

            else:

                print("Opcion no valida")

    elif opcionPrincipal == "3":

        while True:

            opcionEstadistica = menuEstadisticas.mostrar()

            if opcionEstadistica == "1":

                nombre = input("Nombre del cliente: ")

                cliente = banco.recuperarCliente(nombre)

                if cliente:

                    print(cliente)
                    print("Total invertido:", cliente.totalInvertido())
                    print("Promedio invertido:", cliente.promedioInvertido())

                else:

                    print("Cliente no encontrado")

            elif opcionEstadistica == "2":

                print(banco)

                mayor = banco.clienteMayorInversion()

                if mayor:
                    print("\nCliente con mayor inversion:")
                    print(mayor.recuperarNombre())

            elif opcionEstadistica == "3":

                graficas.graficaInversionesClientes(banco)

            elif opcionEstadistica == "4":

                break

            else:

                print("Opcion no valida")

    elif opcionPrincipal == "4":

        banco.guardarClientes()
        banco.guardarInversiones()

        print("\nGuardando informacion...")
        print("Gracias por usar el sistema de inversiones")

        break

    else:

        print("Opcion no valida")
