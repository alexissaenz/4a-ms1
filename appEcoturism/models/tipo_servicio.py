from django.db import models

class Tipo_Servicio(models.Model):
    nombre = models.CharField('nombre', max_length = 50)
    