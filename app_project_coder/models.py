
from django.db import models

'''Agregando clases:
Estudiante (nombre, apellido, email)
Profesor 
Curso
'''



class Estudiante (models.Model):

    nombre = models.CharField(max_length=130)
    apellido = models.CharField(max_length=130)
    email = models.EmailField()


class Profesor (models.Model):

    nombre = models.CharField()
    apellido = models.CharField()
    email = models.EmailField()
    profesion = models.CharField()


class Curso(models.Model):
    nombre = models.CharField()
    comision = models.IntegerField()