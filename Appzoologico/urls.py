from django.urls import path

from Appzoologico.views import (
    view_zool, view_posts, view_about, view_contact,
    view_Login, view_Registrarse, view_Editar_Perfil
    )

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', view_zool, name="Home"),
    path('Posts/', view_posts, name="posts"),
    path('About/', view_about, name="about"),
    path('Contact/', view_contact, name="contact"),
    path('Registrarse/', view_Registrarse, name="RegistrarCuenta"),
    path('LogIn/', view_Login, name="LogIn"),
    path('ActualizarPerfil/', view_Editar_Perfil, name="ActualizarPerfil"),
    path('logout/', LogoutView.as_view(template_name='IndexZoo.html'), name='LogOut'),
]