from django.db import models
from django.contrib.auth.models import User

carreras = [
    ('ING', 'Ingeniería'),
    ('MED', 'Medicina'),
    ('ARQ', 'Arquitectura'),
    ('DER', 'Derecho'),
    ('ECO', 'Economía'),
]

class AlumnoUTT(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    carrera = models.CharField(max_length=100, choices=carreras)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
