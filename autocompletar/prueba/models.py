from django.db import models
from month.models import MonthField

class Concepto(models.Model):
    descripcion = models.CharField('Descripción', max_length=100, unique=True)

class Movimiento(models.Model):
    concepto = models.ForeignKey('prueba.Concepto', on_delete=models.PROTECT)

class Bug_Movimiento(models.Model):
    concepto = models.ForeignKey('prueba.Concepto', on_delete=models.PROTECT)
    mes_inicio = MonthField()