"""
Created on April, 2026
@author: arizbesilva0-star
"""

class Menu:

    def __init__(self, titulo):
        self.__titulo = titulo

    def bienvenida(self):
        print("=" * 50)
        print("BIENVENIDO AL SISTEMA DE INVERSIONES".center(50))
        print("=" * 50)
        print("Cliente: Acceso autorizado")
        print("Cargando sistema...\n")
        print(self.__titulo.center(50))
        print("=" * 50)

    def opciones(self):
        print("\n" + "-" * 50)
        print("MENU PRINCIPAL".center(50))
        print("-" * 50)
        print("1) Crear nueva cuenta de inversion")
        print("2) Eliminar cuenta")
        print("3) Depositar dinero")
        print("4) Retirar dinero")
        print("5) Calcular rendimiento")
        print("6) Mostrar todas las cuentas")
        print("7) Ordenar cuentas por saldo")
        print("8) Ver datos del cliente")
        print("9) Salir del sistema")
        print("-" * 50)
        return input("Selecciona una opcion: ")
