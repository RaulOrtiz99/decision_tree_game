class EstadoMaquina:
    def __init__(self):
        self.estado_actual = "inactivo"

    def actualizar_estado(self, accion):
        if self.estado_actual == "inactivo" and accion == "detectar_jugador":
            self.estado_actual = "alerta"
        elif self.estado_actual == "alerta" and accion == "atacar":
            self.estado_actual = "atacando"
        elif self.estado_actual == "alerta" and accion == "huir":
            self.estado_actual = "huyendo"
        elif self.estado_actual in ["atacando", "huyendo"] and accion == "reset":
            self.estado_actual = "inactivo"

    def get_accion(self):
        if self.estado_actual == "inactivo":
            return "Descansando"
        elif self.estado_actual == "alerta":
            return "Alerta - vigilando"
        elif self.estado_actual == "atacando":
            return "Atacando"
        elif self.estado_actual == "huyendo":
            return "Huyendo"