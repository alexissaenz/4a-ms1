from django.db import models
from .tipo_servicio import Tipo_Servicio
from .proveedor import Proveedor
from .plan import Plan

class Servicio(models.Model):
    nombre = models.CharField('nombre', max_length = 100)
    activo = models.BooleanField(default=False)
    imagen = models.CharField('imagen', max_length = 250)
    precio = models.DecimalField(max_digits=20, decimal_places=4)
    proveedor = models.ForeignKey(Proveedor, related_name='servicio', on_delete=models.CASCADE)
    tipo_serv = models.ForeignKey(Tipo_Servicio, related_name='servicio', on_delete=models.CASCADE)
    plan = models.ManyToManyField(Plan, related_name='servicio', blank=True)