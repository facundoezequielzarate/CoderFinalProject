from django.db import models

# Create your models here.

class Banda(models.Model):
    nombre = models.CharField(max_lengh=40)
    cantidad = models.IntegerField()

class Integrantes(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)

class Empresa(models.Model):
    nombre = models.CharField(max_length=40)
    CEO = models.CharField(max_length=40)


