from django.db import models

class Categoria_Prov(models.Model):
    nombre = models.CharField('nombre', max_length = 50)