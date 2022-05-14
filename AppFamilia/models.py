from django.db import models

class Familiar(models.Model):
    nombre=models.CharField(max_length=40)
    apellido=models.CharField(max_length=40)
    relacion=models.CharField(max_length=20)
    edad=models.IntegerField()
    fechaNacimiento=models.DateField()
