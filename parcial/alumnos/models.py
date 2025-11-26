from django.db import models
from django.contrib.auth.models import User

class Alumno(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    curso = models.CharField(max_length=100)
    email = models.EmailField()  # ✅ nuevo campo para envío de PDF

    def __str__(self):
        return f"{self.nombre} ({self.curso})"
