from django.db import models
from unittest.util import _MAX_LENGTH

#entregable
class Hambuergesa(models.Model):
    nombre = models.CharField(max_length=50)
    contenido = models.CharField(max_length=150)
    precio = models.FloatField()
    

class Pizza(models.Model):
    tipo = models.CharField(max_length=40)
    caracteristicas = models.CharField(max_length=150)
    precio = models.FloatField()

class Postre(models.Model):
    nombre = models.CharField(max_length=40)
    contenido = models.CharField(max_length=150)
    precio = precio = models.FloatField()
