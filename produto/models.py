from django.db import models

# Create your models here.

class Produtos(models.Model):
    nome  = models.CharField(max_length=50, unique=True)
    quantidade = models.IntegerField()
    descricao = models.CharField(max_length=500)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    tipo = models.CharField(max_length=500)
    categoria = models.CharField(max_length=500)

