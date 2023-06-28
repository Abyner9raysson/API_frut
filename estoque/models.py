from django.db import models

class Estoque(models.Model):
    setor = models.CharField(max_length=50)
    corredor = models.CharField(max_length=50)
    prateleira = models.CharField(max_length=50)
    produto = models.CharField(max_length=50)
