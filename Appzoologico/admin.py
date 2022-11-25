from django.contrib import admin

# Register your models here.
from .models import Animal_GrupoSecundario1, Animal_GrupoSecundario2, Empleado, Avatar, Posteo


# Register your models here.
admin.site.register(Animal_GrupoSecundario1)
admin.site.register(Animal_GrupoSecundario2)
admin.site.register(Empleado)
admin.site.register(Avatar)
admin.site.register(Posteo)