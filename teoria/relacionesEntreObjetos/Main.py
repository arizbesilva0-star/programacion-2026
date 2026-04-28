"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from cuenta import *
from cliente import *

print("Desde las pruebas")

cuenta1 = Cuenta(300, "debito")
cuenta1.mostrarDetalles()

cuenta1.depositar(400)
cuenta1.mostrarDetalles()

cliente1 = Cliente("Arizbe", "direccion", 25, cuenta1)
cliente1.mostrarDetalles()
