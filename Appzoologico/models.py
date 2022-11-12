from django.db import models

# Create your models here.
class Animal_GrupoPrincipal (models.Model):

    nombre = models.CharField(max_length = 40)
    extremidades = models.IntegerField()
    AlimentacionElecciones = [
        ('Omnívoro', 'Omnívoro'),
        ('Carnívoro', 'Carnívoro'),
        ('Herbívoro', 'Herbívoro'),
        ('Insectivoros', 'Insectivoros'),
    ]
    alimentacion = models.CharField(max_length = 12, choices = AlimentacionElecciones, default='Omnívoro')
    conducta = models.CharField(max_length = 45)

    class Meta:
        abstract = True

class Animal_GrupoSecundario1 (Animal_GrupoPrincipal):

    Subfilo_Vertebrado = "Vertebrado"
    EspecieElecciones = [
        ('Mamifero', 'Mamifero'),
        ('Aves', 'Aves'),
        ('Reptil', 'Reptil'),
        ('Anfibio', 'Anfibio'),
        ('Pez', 'Pez'),
    ]
    Especie = models.CharField(
        max_length= 8,
        choices= EspecieElecciones,
        default= 'Mamifero',
    )

class Animal_GrupoSecundario2 (Animal_GrupoPrincipal):

    Subfilo_Invertebrado = "Invertebrado"
    EspecieElecciones = [
        ('Insecto', 'Insecto'),
        ('Araña', 'Araña'),
        ('Molusco', 'Molusco'),
        ('Crustaceo', 'Crustaceo'),
        ('Myriapoda', 'Myriapoda'),
    ]
    Especie = models.CharField(
        max_length= 9,
        choices= EspecieElecciones,
        default= 'Insectos',
    )

class Empleado (models.Model):

    nombre = models.CharField(max_length = 50)
    fecha_dEntrada = models.DateField()
    turno = models.TimeField()

    
    
"""
class Guardias (Empleado, models.Model):
    fuerza = 

class Ayudantes (Empleado, models.Model):
"""

