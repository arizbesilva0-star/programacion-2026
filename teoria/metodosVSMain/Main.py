"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

from cuenta import *

class Main:
    pass


print("Desde las pruebas")

cuenta1 = Cuenta(300, "debito")

print("Cantidad inicial::", cuenta1.cantidad)
print("Tipo de cuenta::", cuenta1.tipo)

cuenta1.depositar(200)

cuenta1.mostrarDetalles()
