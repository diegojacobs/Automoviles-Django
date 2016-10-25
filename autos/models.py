from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Marca(models.Model):
    nombre = models.CharField(max_length=30)

class Automovil(models.Model):
    linea = models.CharField(max_length=30)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    color = models.CharField(max_length=30)
    modelo = models.IntegerField()
