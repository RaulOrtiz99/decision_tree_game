from django.db import models

class Decision(models.Model):
    personaje = models.CharField(max_length=50)
    estado = models.JSONField()
    accion = models.CharField(max_length=100)
    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.personaje}: {self.accion} - {self.fecha}"