from django.db import models


# Create your models here.

# Cargo
# Salário
# Carga Horária
# Folha de Ponto
# Setor


class RecursosH(models.Model):
    cargo  = models.CharField(max_length=50, unique=True)
    nome  = models.CharField(max_length=50)
    salario = models.DecimalField(max_digits=8, decimal_places=2)
    cargaHoraria = models.DecimalField(max_digits=8, decimal_places=2)
    folhaPonto = models.DecimalField(max_digits=8, decimal_places=2)
    setor = models.CharField(max_length=50)