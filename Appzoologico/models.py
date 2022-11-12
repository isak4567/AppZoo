from django.db import models

# Create your models here.
class Animal_GrupoPrincipal (models.Model):

    nombre = models.CharField(max_length = 40)
    extremidades = models.IntegerField()
    tipo = models.CharField(max_length = 15)
    alimentacion = models.CharField(max_length = 15)
    conducta = models.CharField(max_length = 150)

    class Meta:
        abstract = True

class Animal_GrupoSecundario1 (Animal_GrupoPrincipal):

    Subfilo_Vertebrado = "Vertebrado"

class Animal_GrupoSecundario2 (Animal_GrupoPrincipal):

    Subfilo_Invertebrado = "Invertebrado"

class Empleado (models.Model):

    nombre = models.CharField(max_length = 50)
    fecha_dEntrada = models.DateField()
    turno = models.TimeField()

    
    
"""
class Guardias (Empleado, models.Model):
    fuerza = 

class Ayudantes (Empleado, models.Model):
"""

