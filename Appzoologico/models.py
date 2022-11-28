from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from ckeditor.fields import RichTextField

# Create your models here.
class Animal_GrupoPrincipal (models.Model):

    nombre = models.CharField(max_length = 40)
    extremidades = models.IntegerField(
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
    )
    AlimentacionElecciones = [
        ('Omnívoro', 'Omnívoro'),
        ('Carnívoro', 'Carnívoro'),
        ('Herbívoro', 'Herbívoro'),
        ('Insectivoros', 'Insectivoros'),
    ]
    alimentacion = models.CharField(max_length = 12, choices = AlimentacionElecciones, default='Omnívoro')
    conducta = models.CharField(max_length = 150)
    imagenAnimal = models.ImageField(upload_to='animalesImg', null=True, blank = True)

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

    def __str__(self):
        return f"{self.id} {self.nombre} - {self.Subfilo_Vertebrado} - {self.Especie}"


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

    def __str__(self):
        return f"{self.id} {self.nombre} - {self.Subfilo_Invertebrado} - {self.Especie}"


class Empleado (models.Model):

    nombre = models.CharField(max_length = 30)
    fecha_dEntrada = models.DateField()
    rol = models.CharField(max_length = 30, default='')
    descripcion = models.TextField(max_length = 300, default='')
    imagenEmpleado = models.ImageField(upload_to='empleadosImg', null=True, blank = True)

    def __str__(self):
        return f"{self.nombre} - {self.rol}"


class Avatar (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)
 
    def __str__(self):
        return f"{self.user} - {self.imagen}"

class Posteo(models.Model):

    titulo = models.CharField(max_length=80)
    subtitulo = models.TextField(max_length=400)
    posteo = RichTextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_post = models.DateTimeField(auto_now=False, auto_now_add=False)
    animal = models.CharField(default='',max_length=80)
    imagen = models.ImageField(upload_to='posts', null=True, blank = True)
    avatar_url = models.CharField(default='',max_length=100)

    def __str__(self):
        return f"Posteo {self.id} - {self.titulo}"


