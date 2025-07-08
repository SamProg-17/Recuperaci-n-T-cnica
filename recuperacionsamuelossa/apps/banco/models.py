from django.db import models

# Create your models here.

class Banco(models.Model):
    codigo = models.IntegerField('codigo')
    nombre = models.TextField('nombre')