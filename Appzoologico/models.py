from django.db import models
from django.contrib.auth.models import User

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

    nombre = models.CharField(max_length = 30)
    fecha_dEntrada = models.DateField()
    rol = models.CharField(max_length = 30, default='')
    descripcion = models.TextField(max_length = 80, default='')

"""
class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"
"""  
