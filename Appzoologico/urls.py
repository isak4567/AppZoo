from django.urls import path

from Appzoologico.views import (
    view_zool, view_posts, view_about, view_contact,
    view_Login, view_Registrarse, view_Detalles_Perfil, view_Editar_Perfil,
    view_AgregarAnimalG1, view_DetallesAnimalG1, view_ModificarAnimalG1, view_EliminarAnimalG1, 
    view_AgregarAnimalG2, view_DetallesAnimalG2, view_ModificarAnimalG2, view_EliminarAnimalG2,
    view_ListasAnimales,
    agregarpost, view_EliminarPost, view_ModificarPost, view_DetallesPost
    )

from django.contrib.auth.views import LogoutView


urlpatterns = [
    # ---------------------------- Urls Principales ----------------------------
    path('', view_zool, name="Home"),
    path('Posts/', view_posts, name="posts"),
    path('About/', view_about, name="about"),
    path('Contact/', view_contact, name="contact"),
    # ---------------------------- Urls Usuario ----------------------------
    path('Registrarse/', view_Registrarse, name="RegistrarCuenta"),
    path('LogIn/', view_Login, name="LogIn"),
    path('logout/', LogoutView.as_view(template_name='IndexZoo.html'), name='LogOut'),
    path('DetallesPerfil/', view_Detalles_Perfil, name="DetallesPerfil"),
    path('ActualizarPerfil/', view_Editar_Perfil, name="ActualizarPerfil"),
    # ---------------------------- Urls AnimalG1 ----------------------------
    path('AgregarAnimalG1/', view_AgregarAnimalG1, name="AgregarAnimalG1"),
    path('DetallesAnimalG1/<int:id>', view_DetallesAnimalG1, name="DetallesAnimalG1"),
    path('ModificarAnimalG1/<int:id>', view_ModificarAnimalG1, name="ModificarAnimalG1"),
    path('EliminarAnimalG1/<int:id>', view_EliminarAnimalG1, name="EliminarAnimalG1"),
    # ---------------------------- Urls AnimalG2 ----------------------------
    path('AgregarAnimalG2/', view_AgregarAnimalG2, name="AgregarAnimalG2"),
    path('DetallesAnimalG2/<int:id>', view_DetallesAnimalG2, name="DetallesAnimalG2"),
    path('ModificarAnimalG2/<int:id>', view_ModificarAnimalG2, name="ModificarAnimalG2"),
    path('EliminarAnimalG2/<int:id>', view_EliminarAnimalG2, name="EliminarAnimalG2"),
    # ---------------------------- Urls Lista Animales ----------------------------
    path('ListasAnimales/', view_ListasAnimales, name="ListasAnimales"),
    # ---------------------------- Urls Post ----------------------------
    path('AgregarPost/<nombre>', agregarpost, name="AgregarPost"),
    path('PostEliminar/<int:id>', view_EliminarPost, name="PostEliminar"),
    path('PostModificar/<int:id>', view_ModificarPost, name="PostModificar"),
    path('PostDetalles/<int:id>', view_DetallesPost, name="PostDetalles")
]