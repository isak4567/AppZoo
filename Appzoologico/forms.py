from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar, Animal_GrupoSecundario1, Animal_GrupoSecundario2, Posteo


class UsuarioFormulario (UserCreationForm):

    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class EditarPerfil (UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    class Meta:
        model = User
        fields = ['first_name','last_name','email']


class ImagenPerfil (forms.ModelForm):

    class Meta:
        model = Avatar
        fields = ['imagen']


class AnimalG1F (forms.ModelForm):

    class Meta:
        model = Animal_GrupoSecundario1
        fields = ('__all__')

class AnimalG2F (forms.ModelForm):

    class Meta:
        model = Animal_GrupoSecundario2
        fields = ('__all__')


class EmpleadoF (forms.Form):

    nombre = forms.CharField()
    fecha_dEntrada = forms.DateField()
    rol = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))

class Postformulario(forms.ModelForm):

    class Meta:
        model= Posteo
        fields = ['titulo', 'subtitulo', 'posteo', 'imagen']

