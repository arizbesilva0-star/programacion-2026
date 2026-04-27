"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from cuenta import *
from cliente import *

print("Desde las pruebas")

cuenta1 = Cuenta(300, "debito")
cuenta1.depositar(400)

cliente1 = Cliente("Virginia", "direccion", 25, cuenta1)
cliente1.mostrarDetalles()
