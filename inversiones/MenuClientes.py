"""
Created on June, 2026
@author: arizbesilva-star
"""
class MenuClientes:

    def mostrar(self):

        print("\n" + "-" * 60)
        print("MENU CLIENTES".center(60))
        print("-" * 60)

        print("1) Registrar cliente")
        print("2) Eliminar cliente")
        print("3) Mostrar clientes")
        print("4) Regresar")

        print("-" * 60)

        return input(
            "Selecciona una opcion: "
        )

    def solicitarDatosCliente(self):

        nombre = input("Nombre: ")

        direccion = input("Direccion: ")

        edad = int(
            input("Edad: ")
        )

        return (
            nombre,
            direccion,
            edad
        )

    def solicitarNombreCliente(self):

        return input(
            "Nombre del cliente: "
        )
