"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from cuenta import *
from cliente import *

print("Desde las pruebas")

cuenta1 = Cuenta(300, "debito")
print(cuenta1)

cuenta1.depositar(400)
print(cuenta1)

cliente1 = Cliente("Virginia", "direccion", 25, cuenta1)
print(cliente1)
