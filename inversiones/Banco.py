"""
Created on June, 2026
@author: arizbesilva-star
"""

import csv

from Cliente import Cliente


class Banco:

    def __init__(self):

        self.__clientes = []

    def agregarCliente(self, cliente):

        if self.recuperarCliente(
            cliente.recuperarNombre()
        ) is None:

            self.__clientes.append(
                cliente
            )

            return True

        return False

    def borrarCliente(self, nombre):

        cliente = self.recuperarCliente(
            nombre
        )

        if cliente:

            self.__clientes.remove(
                cliente
            )

            return True

        return False

    def recuperarCliente(
        self,
        nombre
    ):

        for cliente in self.__clientes:

            if (
                cliente.recuperarNombre()
                == nombre
            ):

                return cliente

        return None

    def recuperarClientes(self):

        return self.__clientes

    def mostrarClientes(self):

        if len(
            self.__clientes
        ) == 0:

            print(
                "No hay clientes registrados"
            )

        else:

            for cliente in self.__clientes:

                print(cliente)

                print(
                    "-" * 50
                )

    def cantidadClientes(self):

        return len(
            self.__clientes
        )

    def totalInvertidoBanco(self):

        suma = 0

        for cliente in self.__clientes:

            suma += (
                cliente.totalInvertido()
            )

        return suma

    def promedioBanco(self):

        if (
            len(self.__clientes)
            == 0
        ):

            return 0

        return (
            self.totalInvertidoBanco()
            /
            len(self.__clientes)
        )

    def clienteMayorInversion(self):

        if (
            len(self.__clientes)
            == 0
        ):

            return None

        mayor = self.__clientes[0]

        for cliente in self.__clientes:

            if (
                cliente.totalInvertido()
                >
                mayor.totalInvertido()
            ):

                mayor = cliente

        return mayor

    def guardarClientes(self):

        archivo = open(
            "clientes.csv",
            "w",
            newline="",
            encoding="utf-8"
        )

        salida = csv.writer(
            archivo
        )

        salida.writerow(
            [
                "nombre",
                "direccion",
                "edad"
            ]
        )

        for cliente in self.__clientes:

            salida.writerow(
                [
                    cliente.recuperarNombre(),
                    cliente.recuperarDireccion(),
                    cliente.recuperarEdad()
                ]
            )

        archivo.close()

    def cargarClientes(self):

        try:

            archivo = open(
                "clientes.csv",
                "r",
                encoding="utf-8"
            )

            entrada = csv.reader(
                archivo
            )

            next(
                entrada,
                None
            )

            for fila in entrada:

                nombre = fila[0]

                direccion = fila[1]

                edad = int(
                    fila[2]
                )

                cliente = Cliente(
                    nombre,
                    direccion,
                    edad
                )

                self.agregarCliente(
                    cliente
                )

            archivo.close()

        except:

            pass

    def guardarInversiones(self):

        archivo = open(
            "inversiones.csv",
            "w",
            newline="",
            encoding="utf-8"
        )

        salida = csv.writer(
            archivo
        )

        salida.writerow(
            [
                "cliente",
                "nombre",
                "saldo",
                "interes",
                "tiempo"
            ]
        )

        for cliente in self.__clientes:

            for cuenta in (
                cliente.recuperarCuentas()
            ):

                salida.writerow(
                    [
                        cliente.recuperarNombre(),
                        cuenta.recuperarNombre(),
                        cuenta.recuperarSaldo(),
                        cuenta.recuperarInteres(),
                        cuenta.recuperarTiempo()
                    ]
                )

        archivo.close()

    def __str__(self):

        cadena = ""

        cadena += (
            "\nClientes registrados: "
            + str(
                self.cantidadClientes()
            )
        )

        cadena += (
            "\nCapital total invertido: "
            + str(
                self.totalInvertidoBanco()
            )
        )

        cadena += (
            "\nPromedio por cliente: "
            + str(
                self.promedioBanco()
            )
        )

        return cadena