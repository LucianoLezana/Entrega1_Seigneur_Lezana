from unittest.util import _MAX_LENGTH
from django.db import models

class Estudiante (models.Model):

    nombre = models.CharField(max_length=130)
    edad = models.IntegerField()
