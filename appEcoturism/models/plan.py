from django.db import models
from .user import User

class Plan(models.Model):
    valor = models.DecimalField(max_digits=20, decimal_places=4)
    f_inicio = models.DateTimeField()
    f_fin = models.DateTimeField()
    activo = models.BooleanField(default=False)
    user = models.ForeignKey(User, related_name='plan', on_delete=models.CASCADE)