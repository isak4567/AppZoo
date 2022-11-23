from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth.models import User
from .models import Avatar


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


class EmpleadoF (forms.Form):

    nombre = forms.CharField()
    fecha_dEntrada = forms.DateField()
    rol = forms.CharField()
    descripcion = forms.CharField(widget=forms.Textarea(attrs={"rows":5}))

