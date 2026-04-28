"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Menu:

    def __init__(self, titulo):
        self.__titulo = titulo

    def bienvenida(self):
        print(self.__titulo)

    def opciones(self):
        print("\n1. Aumentar dinero")
        print("2. Disminuir dinero")
        print("3. Calcular inversion")
        print("4. Mostrar inversion")
        print("5. Mostrar cliente")
        print("6. Salir")
        return input("Elige una opcion: ")
        return opcion
