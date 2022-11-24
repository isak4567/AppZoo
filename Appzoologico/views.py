from django.shortcuts import render
from datetime import datetime
#from Appzoologico.models import A
from django.http import HttpResponse
from .models import Animal_GrupoSecundario1, Animal_GrupoSecundario2, Empleado, Avatar
from .forms import  UsuarioFormulario, EmpleadoF, EditarPerfil, ImagenPerfil
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def view_zool(request):

    vertebrados = Animal_GrupoSecundario1.objects.all()

    try:
        avatar = Avatar.objects.get(user = request.user)
        print(avatar.imagen)
    except:
        return render(request, "indexZoo.html",  {"vertebrados": vertebrados})
    
    return render(request, "indexZoo.html",  {"vertebrados": vertebrados, "imgPerfil": avatar.imagen.url})

def view_posts(request):
    
    return render(request, "Posts.html")

def view_about(request):

    empleados = Empleado.objects.all()
    
    return render(request, "About.html", {"Empleados": empleados})

def view_contact(request):
    
    return render(request, "Contact.html")

################ Vistas de Usuarios ################
def view_Login(request):
    
    if request.method == "POST":
 
        miFormulario = AuthenticationForm(request, data = request.POST) 
 
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            nombre = informacion["username"]
            contraseña = informacion["password"]

            user = authenticate(username = nombre, password = contraseña)

            if user:

                login(request, user)
                try:
                    avatar = Avatar.objects.get(user = request.user)
                except:
                    return render(request, "indexZoo.html",  {"mensaje": f'Bienvenido {nombre}'})

                return render(request, "IndexZoo.html", {"mensaje": f'Bienvenido {nombre}', "imgPerfil": avatar.imagen.url})
            else:

                return render(request, "IndexZoo.html", {"mensaje": f'No pudo loguerse, usuario inexistente o incorrecto'})
        
        miFormulario = AuthenticationForm()
    
        return render(request, "./Cuenta/LogIn.html", {'form': miFormulario, 'mensaje': f'No pudo loguerse, usuario inexistente o incorrecto'})

    else:
        miFormulario = AuthenticationForm()
    
        return render(request, "./Cuenta/LogIn.html", {'form': miFormulario})

def view_Registrarse(request):
    
    if request.method == "POST":
 
        miFormulario = UsuarioFormulario(request.POST) 
 
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data["username"]
            miFormulario.save()

            usuario = User.objects.get(username = informacion)
            avatar = Avatar(user= usuario, imagen= "avatares/default.png")
            avatar.save()

            return render(request, "IndexZoo.html", {"mensaje": f'Te has Registrado satisfactoriamente {informacion}'})
        
        miFormulario = UsuarioFormulario()
    
        return render(request, "./Cuenta/Registrarse.html", {'form': miFormulario, 'mensaje': f'Error, No pudo Registrarse'})

    else:
        miFormulario = UsuarioFormulario()
    
        return render(request, "./Cuenta/Registrarse.html", {'form': miFormulario})

################ Vistas de Perfil ################
def view_Editar_Perfil(request):
    usuario = request.user
    avatar = Avatar.objects.get(user = request.user)

    if request.method == "POST":
 
        miFormulario = EditarPerfil(request.POST)
        miFormularioImagen = ImagenPerfil(request.POST, request.FILES) 
 
        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            usuario.first_name = informacion["first_name"]
            usuario.last_name = informacion["last_name"]
            usuario.email = informacion["email"]
            usuario.save()
            
            try:
                print(request.FILES['imagen'])
                if avatar.imagen != "avatares/default.png":
                    avatar.imagen.delete()
            except:
                print("")

            try:
                avatar.imagen = request.FILES['imagen']
                avatar.save()
            except: 
                print("")
            
            return render(request, "IndexZoo.html", {"mensaje": f'Modificaste tu perfil satisfactoriamente {usuario.first_name}'})
        
        miFormulario = EditarPerfil(instance = request.user)
    
        return render(request, "./Cuenta\ActualizarPerfil.html", {'form': miFormulario, 'mensaje': f'Error, No pudo actualizar su perfil'})

    else:
        miFormulario = EditarPerfil(instance = request.user)
        miFormularioImagen = ImagenPerfil(initial={'imagen': avatar.imagen})
    
        return render(request, "./Cuenta\ActualizarPerfil.html", {'form': miFormulario, 'imgForm': miFormularioImagen})


def view_Ingresar_F(request):
    """
    if request.method == "POST":
 
        miFormulario = UsuarioF(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")

    else:
    
    miFormulario = UsuarioF()
    
    return render(request, "Ingresar_F.html", {'form': miFormulario})
    """

################ Vistas de Empleados ################

    """
    if request.method == "POST":
 
        miFormulario = UsuarioF(request.POST) # Aqui me llega la informacion del html
        print(miFormulario)
 
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request, "AppCoder/inicio.html")

    else:
    """
    miFormulario = EmpleadoF()
    
    return render(request, "Ingresar_F.html", {'form': miFormulario})


class yyT(CreateView):

    model = Animal_GrupoSecundario1
    template_name = './Ingresar_AF.html'
    success_url = 'Posts/'
    fields = ['nombre','extremidades','alimentacion','conducta','Especie']
