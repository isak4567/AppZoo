from django.urls import path

from Appzoologico.views import (
    view_zool, view_posts, view_about, view_contact,
    view_Login, view_Registrarse, view_Editar_Perfil,
    view_AgregarAnimalG1, view_DetallesAnimalG1, view_ModificarAnimalG1, view_EliminarAnimalG1, 
    view_AgregarAnimalG2, view_DetallesAnimalG2, view_ModificarAnimalG2, view_EliminarAnimalG2,
    view_ListasAnimales,
    agregarpost
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
    path('AgregarAnimalG1/', view_AgregarAnimalG1, name="AgregarAnimalG1"),
    path('DetallesAnimalG1/<int:id>', view_DetallesAnimalG1, name="DetallesAnimalG1"),
    path('ModificarAnimalG1/<int:id>', view_ModificarAnimalG1, name="ModificarAnimalG1"),
    path('EliminarAnimalG1/<int:id>', view_EliminarAnimalG1, name="EliminarAnimalG1"),
    path('AgregarAnimalG2/', view_AgregarAnimalG2, name="AgregarAnimalG2"),
    path('DetallesAnimalG2/<int:id>', view_DetallesAnimalG2, name="DetallesAnimalG2"),
    path('ModificarAnimalG2/<int:id>', view_ModificarAnimalG2, name="ModificarAnimalG2"),
    path('EliminarAnimalG2/<int:id>', view_EliminarAnimalG2, name="EliminarAnimalG2"),
    path('ListasAnimales/', view_ListasAnimales, name="ListasAnimales"),
    path('AgregarPost/<nombre>', agregarpost, name="AgregarPost"),
]