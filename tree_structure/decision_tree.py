import random

class DecisionNode:
    def __init__(self, condicion=None, si=None, no=None, resultado=None):
        self.condicion = condicion  # Puede ser una función lambda o nombre de clave
        self.si = si                # Subárbol si es verdadero
        self.no = no                # Subárbol si es falso
        self.resultado = resultado  # Acción final si es hoja

    def tomar_decision(self, estado_juego):
        if self.resultado is not None:
            return self.resultado

        if callable(self.condicion):
            if self.condicion(estado_juego):
                return self.si.tomar_decision(estado_juego)
            else:
                return self.no.tomar_decision(estado_juego)
        else:
            valor = estado_juego.get(self.condicion, False)
            if valor:
                return self.si.tomar_decision(estado_juego)
            else:
                return self.no.tomar_decision(estado_juego)