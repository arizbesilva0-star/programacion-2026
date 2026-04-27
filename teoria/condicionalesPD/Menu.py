"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Menu:

    def __init__(self, mensaje):
        # ATRIBUTO PRIVADO (no debe modificarse desde fuera)
        self.__mensaje = mensaje

    def bienvenida(self):
        # MÉTODO PÚBLICO
        print(self.__mensaje)

    def opciones(self):
        # MÉTODO PÚBLICO
        print("\n1. Depositar")
        print("2. Retirar")
        print("3. Mostrar cuenta")
        print("4. Salir")
        return input("Opcion: ")