from django.db import models

# Create your models here.
#compra
#venda
#fiscal
#relatorioCompra
#relatorioVenda

class Financeiro(models.Model):
    compra  = models.CharField(max_length=50)
    venda = models.CharField(max_length=50)
    fiscal = models.CharField(max_length=50)
    relatorioCompra = models.CharField(max_length=50)
    relatorioVenda = models.CharField(max_length=50)