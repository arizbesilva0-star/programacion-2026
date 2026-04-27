"""
Created on Marzo, 2026
@author: arizbesilva0-star
"""

class Cliente:

    def __init__(self, nombre, cuenta):
        # ATRIBUTOS PÚBLICOS
        self.nombre = nombre
        self.cuenta = cuenta

    def __str__(self):
        # MÉTODO PÚBLICO (usa getters porque Cuenta es privada internamente)
        return "Cliente: " + self.nombre + " | " + self.cuenta.getTipo() + " | Saldo: " + str(self.cuenta.getSaldo())