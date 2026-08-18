from django.db import models
from datetime import datetime

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo = models.EmailField()
    carrera = models.CharField(max_length=100)
    edad = models.IntegerField()
    fecha_ingreso = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
