from django.shortcuts import render
from datetime import datetime
#from Appzoologico.models import A
from django.http import HttpResponse
from .models import Animal_GrupoSecundario1, Animal_GrupoSecundario2, Empleado, Avatar, Posteo
from .forms import  UsuarioFormulario, EmpleadoF, EditarPerfil, ImagenPerfil, AnimalG1F, Postformulario
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def view_zool(request):

    vertebrados = Animal_GrupoSecundario1.objects.all()
    invertebrados = Animal_GrupoSecundario2.objects.all()
    post = Posteo.objects.all()

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "indexZoo.html",  {"vertebrados": vertebrados, "invertebrados": invertebrados, "post":post})
    
    return render(request, "indexZoo.html",  {"vertebrados": vertebrados, "invertebrados": invertebrados, "imgPerfil": avatar.imagen.url, "post":post})

def view_posts(request):
    
    post = Posteo.objects.all()

    return render(request, "Posts.html", {'post': post})

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

################ Vistas de Animales ################
def view_EliminarAnimalG1(request, id):

    if request.method == "POST":
 
        animalG1 = Animal_GrupoSecundario1.objects.get(id = id)
        nombre = animalG1.nombre
        animalG1.delete()

        vertebrados = Animal_GrupoSecundario1.objects.all()
        invertebrados = Animal_GrupoSecundario2.objects.all()
        avatar = Avatar.objects.get(user = request.user)

        return render(request, "indexZoo.html", {"mensaje": f'Liberaste a {nombre}.', "vertebrados": vertebrados, "invertebrados": invertebrados, "imgPerfil": avatar.imagen.url})
    
def view_AgregarAnimalG1(request):

    if request.method == "POST":

        miFormulario = AnimalG1F(request.POST, request.FILES) # Aqui me llega la informacion del html

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            avatar = Avatar.objects.get(user = request.user)
            animalGrupo1 = Animal_GrupoSecundario1(
                nombre=informacion["nombre"], extremidades=informacion["extremidades"], 
                alimentacion=informacion["alimentacion"], conducta=informacion["conducta"], 
                Especie=informacion["Especie"], imagenAnimal=request.FILES['imagenAnimal'],
                avatar_url=avatar.imagen.url
                )
            animalGrupo1.save()
            return render(request, "indexZoo.html", {"mensaje": f'Agregado {informacion["nombre"]} con exito.', "imgPerfil": avatar.imagen.url})
        else:    
            return render(request, "Animales/AgregarAnimalG1.html", {"mensaje": f'Error, no se pudo agregar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = AnimalG1F()
    
        return render(request, "Animales/AgregarAnimalG1.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})
   
def view_EliminarAnimalG2(request, id):

    if request.method == "POST":
 
        animalG2 = Animal_GrupoSecundario2.objects.get(id = id)
        nombre = animalG2.nombre
        animalG2.delete()

        vertebrados = Animal_GrupoSecundario1.objects.all()
        invertebrados = Animal_GrupoSecundario2.objects.all()
        avatar = Avatar.objects.get(user = request.user)

        return render(request, "indexZoo.html", {"mensaje": f'Liberaste a {nombre}.', "vertebrados": vertebrados, "invertebrados": invertebrados, "imgPerfil": avatar.imagen.url})
   


def view_ListasAnimales(request):

    animalG1 = Animal_GrupoSecundario1.objects.all()
    animalG2 = Animal_GrupoSecundario2.objects.all()
    avatar = Avatar.objects.get(user = request.user)        
    
    return render(request, "Animales/ListasAnimales.html", {'vertebrados': animalG1, 'invertebrados': animalG2, "imgPerfil": avatar.imagen.url})
   

################ Vistas de Empleados ################

################ Vistas de Posteo ################

def agregarpost(request, nombre):

    print(f'Datos ------------------ {request.method}')

    if request.method == "POST":

        miFormulario = Postformulario(request.POST, request.FILES)
        print(f'Datos ------------------ {miFormulario.is_valid()}')

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            avatar = Avatar.objects.get(user = request.user)
            posteo = Posteo(
                titulo=informacion["titulo"], subtitulo=informacion["subtitulo"], 
                posteo=informacion["posteo"], fecha_post=datetime.now(), user=request.user, 
                imagen=request.FILES['imagen'], animal=nombre, avatar_url=avatar.imagen.url
                )
            posteo.save()
            return render(request, "Posts.html", {"mensaje": f'Posteo agregado con exito.'})
        else:    
            return render(request, "Posteos/Agregarpost.html", {"mensaje": f'Error, no se pudo agregar.'})

    else:
    
        miFormulario = Postformulario()
    
        return render(request, "Posteos/Agregarpost.html", {'form': miFormulario})