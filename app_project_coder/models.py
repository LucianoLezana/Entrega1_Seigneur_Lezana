
from django.db import models

'''
        Agregando clases:
-Estudiante (nombre, apellido, email)
-Profesor (nombre, apellido, email, profesion)
-Curso (nombre, comision)

'''



class Estudiante (models.Model):

    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    email = models.EmailField()


class Profesor (models.Model):

    nombre = models.CharField(max_length=120)
    apellido = models.CharField(max_length=120)
    email = models.EmailField()
    profesion = models.CharField(max_length=100)


class Curso(models.Model):
    nombre = models.CharField(max_length=120)
    comision = models.IntegerField()