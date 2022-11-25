from django.shortcuts import render
from datetime import datetime
#from Appzoologico.models import A
from django.http import HttpResponse
from .models import Animal_GrupoSecundario1, Animal_GrupoSecundario2, Empleado, Avatar, Posteo
from .forms import  UsuarioFormulario, EmpleadoF, EditarPerfil, ImagenPerfil, AnimalG1F, AnimalG2F, Postformulario
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
def view_AgregarAnimalG1(request):

    avatar = Avatar.objects.get(user = request.user)

    if request.method == "POST":

        miFormulario = AnimalG1F(request.POST, request.FILES) # Aqui me llega la informacion del html

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            animalGrupo1 = Animal_GrupoSecundario1(
                nombre=informacion["nombre"], extremidades=informacion["extremidades"], 
                alimentacion=informacion["alimentacion"], conducta=informacion["conducta"], 
                Especie=informacion["Especie"], imagenAnimal=request.FILES['imagenAnimal']
                )
            animalGrupo1.save()
            return render(request, "indexZoo.html", {"mensaje": f'Agregado {informacion["nombre"]} con exito.', "imgPerfil": avatar.imagen.url})
        else:    
            return render(request, "Animales/AgregarAnimalG1.html", {"mensaje": f'Error, no se pudo agregar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = AnimalG1F()
    
        return render(request, "Animales/AgregarAnimalG1.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})


def view_DetallesAnimalG1(request, id):
 
    animalG1 = Animal_GrupoSecundario1.objects.get(id = id)
    
    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "./Animales/DetallesAnimal.html", {"animal": animalG1})

    return render(request, "./Animales/DetallesAnimal.html", {"animal": animalG1, "imgPerfil": avatar.imagen.url})


def view_ModificarAnimalG1(request, id):

    animalG1 = Animal_GrupoSecundario1.objects.get(id=id)
    avatar = Avatar.objects.get(user = request.user)

    if request.method == "POST":

        miFormulario = AnimalG1F(request.POST, request.FILES) # Aqui me llega la informacion del html

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            animalG1.nombre=informacion["nombre"] 
            animalG1.extremidades=informacion["extremidades"] 
            animalG1.alimentacion=informacion["alimentacion"] 
            animalG1.conducta=informacion["conducta"] 
            animalG1.Especie=informacion["Especie"]
            
            try:
                print(request.FILES['imagenAnimal'])
                animalG1.imagenAnimal.delete()
            except:
                print("")

            try:
                animalG1.imagenAnimal = request.FILES['imagenAnimal']
            except: 
                print("")
            
            animalG1.save()

            return render(request, "indexZoo.html", {"mensaje": f'Modificado animal con exito.', "imgPerfil": avatar.imagen.url})
        else:    
            return render(request, "Animales/ModificarAnimalG1.html", {"mensaje": f'Error, no se pudo modificar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = AnimalG1F(instance = animalG1)
    
        return render(request, "Animales/ModificarAnimalG1.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})
 

def view_EliminarAnimalG1(request, id):

    if request.method == "POST":
 
        animalG1 = Animal_GrupoSecundario1.objects.get(id = id)
        nombre = animalG1.nombre
        animalG1.imagenAnimal.delete()
        
        animalG1.delete()

        vertebrados = Animal_GrupoSecundario1.objects.all()
        invertebrados = Animal_GrupoSecundario2.objects.all()
        avatar = Avatar.objects.get(user = request.user)

        return render(request, "indexZoo.html", {"mensaje": f'Liberaste a {nombre}.', "vertebrados": vertebrados, "invertebrados": invertebrados, "imgPerfil": avatar.imagen.url})
    

def view_AgregarAnimalG2(request):

    avatar = Avatar.objects.get(user = request.user)

    if request.method == "POST":

        miFormulario = AnimalG2F(request.POST, request.FILES) # Aqui me llega la informacion del html

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            animalGrupo2 = Animal_GrupoSecundario2(
                nombre=informacion["nombre"], extremidades=informacion["extremidades"], 
                alimentacion=informacion["alimentacion"], conducta=informacion["conducta"], 
                Especie=informacion["Especie"], imagenAnimal=request.FILES['imagenAnimal']
                )
            animalGrupo2.save()
            return render(request, "indexZoo.html", {"mensaje": f'Agregado {informacion["nombre"]} con exito.', "imgPerfil": avatar.imagen.url})
        else:    
            return render(request, "Animales/AgregarAnimalG1.html", {"mensaje": f'Error, no se pudo agregar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = AnimalG2F()
    
        return render(request, "Animales/AgregarAnimalG1.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})


def view_ModificarAnimalG2(request, id):

    animalG2 = Animal_GrupoSecundario2.objects.get(id=id)
    avatar = Avatar.objects.get(user = request.user)

    if request.method == "POST":

        miFormulario = AnimalG2F(request.POST, request.FILES) # Aqui me llega la informacion del html

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            animalG2.nombre=informacion["nombre"] 
            animalG2.extremidades=informacion["extremidades"] 
            animalG2.alimentacion=informacion["alimentacion"] 
            animalG2.conducta=informacion["conducta"] 
            animalG2.Especie=informacion["Especie"]
            
            try:
                print(request.FILES['imagenAnimal'])
                animalG2.imagenAnimal.delete()
            except:
                print("")

            try:
                animalG2.imagenAnimal = request.FILES['imagenAnimal']
            except: 
                print("")
            
            animalG2.save()

            return render(request, "indexZoo.html", {"mensaje": f'Modificado animal con exito.', "imgPerfil": avatar.imagen.url})
        else:    
            return render(request, "Animales/ModificarAnimalG1.html", {"mensaje": f'Error, no se pudo modificar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = AnimalG2F(instance = animalG2)
    
        return render(request, "Animales/ModificarAnimalG1.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})


def view_DetallesAnimalG2(request, id):
 
    animalG2 = Animal_GrupoSecundario2.objects.get(id = id)
    
    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "./Animales/DetallesAnimal.html", {"animal": animalG2})

    return render(request, "./Animales/DetallesAnimal.html", {"animal": animalG2, "imgPerfil": avatar.imagen.url})


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

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "Animales/ListasAnimales.html",  {'vertebrados': animalG1, 'invertebrados': animalG2})       
    
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