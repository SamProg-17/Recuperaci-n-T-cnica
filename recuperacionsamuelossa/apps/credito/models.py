from django.db import models

# Create your models here.
class Credito(models.Model):
    banco = models.TextField('banco')
    valor_agregado = models.IntegerField('valor_agredado')