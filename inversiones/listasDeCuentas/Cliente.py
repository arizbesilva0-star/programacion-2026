"""
Created on March, 2026
@author: arizbesilva-star
"""

class Cliente:

    def __init__(self, nombre, direccion, edad):
        self.__nombre = nombre
        self.__direccion = direccion
        self.__edad = edad

    def __str__(self):
        texto = ""
        texto += "Nombre: " + self.__nombre + "\n"
        texto += "Direccion: " + self.__direccion + "\n"
        texto += "Edad: " + str(self.__edad)
        return texto