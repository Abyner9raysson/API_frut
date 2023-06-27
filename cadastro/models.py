from django.db import models

# Create your models here.

class Usuarios(models.Model):
    username  = models.CharField(max_length=50, unique=True)
    senha = models.CharField(max_length=50)