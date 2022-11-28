from django.shortcuts import render
from datetime import datetime
from .models import Animal_GrupoSecundario1, Animal_GrupoSecundario2, Empleado, Avatar, Posteo
from .forms import  UsuarioFormulario, EditarPerfil, ImagenPerfil, AnimalG1F, AnimalG2F, Postformulario
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth import login, authenticate

# Funciones
def Vista_Base_Index(request, mensaje):

    vertebrados = Animal_GrupoSecundario1.objects.all()
    invertebrados = Animal_GrupoSecundario2.objects.all()
    post = Posteo.objects.all()
    postFooter= post[::-1]

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "indexZoo.html",  {"vertebrados": vertebrados, "invertebrados": invertebrados, "post":post, "recentPost": postFooter[0:2], "mensaje": mensaje})
    
    return render(request, "indexZoo.html",  {"vertebrados": vertebrados, "invertebrados": invertebrados, "imgPerfil": avatar.imagen.url, "post":post, "recentPost": postFooter[0:2], "mensaje": mensaje})

################ Vistas Principales ################
def view_zool(request):

    return Vista_Base_Index(request, "")


def view_posts(request):
    
    post = Posteo.objects.all()
    postFooter= post[::-1]

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "Posts.html", {'post': post, "recentPost": postFooter[0:2]})

    return render(request, "Posts.html", {'post': post, "recentPost": postFooter[0:2], "imgPerfil": avatar.imagen.url})


def view_about(request):

    empleados = Empleado.objects.all()
    post = Posteo.objects.all()
    postFooter= post[::-1]

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "About.html", {"Empleados": empleados, "recentPost": postFooter[0:2]})
    
    return render(request, "About.html", {"Empleados": empleados, "recentPost": postFooter[0:2], "imgPerfil": avatar.imagen.url})


def view_contact(request):

    post = Posteo.objects.all()
    postFooter= post[::-1]

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "Contact.html", {"recentPost": postFooter[0:2]})
    
    return render(request, "Contact.html", {"recentPost": postFooter[0:2], "imgPerfil": avatar.imagen.url})


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
             
                return Vista_Base_Index(request, f"Bienvenido {nombre}")
        
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

            return Vista_Base_Index(request, f'Te has Registrado satisfactoriamente {informacion}')
        
        miFormulario = UsuarioFormulario()
    
        return render(request, "./Cuenta/Registrarse.html", {'form': miFormulario, 'mensaje': f'Error, No pudo Registrarse'})

    else:
        miFormulario = UsuarioFormulario()
    
        return render(request, "./Cuenta/Registrarse.html", {'form': miFormulario})


################ Vistas de Perfil ################
@login_required
def view_Detalles_Perfil(request):
    avatar = Avatar.objects.get(user = request.user)
    
    return render(request, "./Cuenta\DetallesPerfil.html", {"imgPerfil": avatar.imagen.url})

@login_required
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
            
            return Vista_Base_Index(request, f'Modificaste tu perfil satisfactoriamente {usuario.first_name}')
        
        miFormulario = EditarPerfil(instance = request.user)
    
        return render(request, "./Cuenta\ActualizarPerfil.html", {'form': miFormulario, 'mensaje': f'Error, No pudo actualizar su perfil'})

    else:
        miFormulario = EditarPerfil(instance = request.user)
        miFormularioImagen = ImagenPerfil(initial={'imagen': avatar.imagen})
    
        return render(request, "./Cuenta\ActualizarPerfil.html", {'form': miFormulario, 'imgForm': miFormularioImagen})


################ Vistas de Animales ################
@staff_member_required(login_url='/Appzoologico/LogIn')
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

            return Vista_Base_Index(request, f'Agregado {informacion["nombre"]} con exito.')

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


@staff_member_required(login_url='/Appzoologico/LogIn')
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

            return Vista_Base_Index(request, f'Modificado animal con exito.')
        else:    
            return render(request, "Animales/ModificarAnimalG1.html", {"mensaje": f'Error, no se pudo modificar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = AnimalG1F(instance = animalG1)
    
        return render(request, "Animales/ModificarAnimalG1.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})


@staff_member_required(login_url='/Appzoologico/LogIn')
def view_EliminarAnimalG1(request, id):

    if request.method == "POST":
 
        animalG1 = Animal_GrupoSecundario1.objects.get(id = id)
        nombre = animalG1.nombre
        animalG1.imagenAnimal.delete()
        
        animalG1.delete()

        return Vista_Base_Index(request, f'Liberaste a {nombre}.')


@staff_member_required(login_url='/Appzoologico/LogIn')
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

            return Vista_Base_Index(request, f'Agregado {informacion["nombre"]} con exito.')

        else:    

            return render(request, "Animales/AgregarAnimalG1.html", {"mensaje": f'Error, no se pudo agregar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = AnimalG2F()
    
        return render(request, "Animales/AgregarAnimalG1.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})


@staff_member_required(login_url='/Appzoologico/LogIn')
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

            return Vista_Base_Index(request, f'Modificado animal con exito.')
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


@staff_member_required(login_url='/Appzoologico/LogIn')
def view_EliminarAnimalG2(request, id):

    if request.method == "POST":
 
        animalG2 = Animal_GrupoSecundario2.objects.get(id = id)
        nombre = animalG2.nombre
        animalG2.delete()

        return Vista_Base_Index(request, f'Liberaste a {nombre}.')
   

def view_ListasAnimales(request):

    animalG1 = Animal_GrupoSecundario1.objects.all()
    animalG2 = Animal_GrupoSecundario2.objects.all()

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "Animales/ListasAnimales.html",  {'vertebrados': animalG1, 'invertebrados': animalG2})       
    
    return render(request, "Animales/ListasAnimales.html", {'vertebrados': animalG1, 'invertebrados': animalG2, "imgPerfil": avatar.imagen.url})
   

################ Vistas de Posteo ################
@login_required
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


@login_required
def view_EliminarPost(request, id):

    PostEliminar = Posteo.objects.get(id = id)

    if request.method == "POST":
 
        titulo = PostEliminar.titulo
        PostEliminar.imagen.delete()
        PostEliminar.delete()

        todoPost = Posteo.objects.all()

        return render(request, "Posts.html", {"mensaje": f'Eliminaste este articulo {titulo}.', "post": todoPost})


@login_required
def view_ModificarPost(request, id):

    post = Posteo.objects.get(id=id)
    avatar = Avatar.objects.get(user = request.user)

    if request.method == "POST":

        miFormulario = Postformulario(request.POST, request.FILES) # Aqui me llega la informacion del html

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data
            
            post.titulo=informacion["titulo"] 
            post.subtitulo=informacion["subtitulo"] 
            post.posteo=informacion["posteo"] 

            try:
                print(request.FILES['imagen'])
                post.imagen.delete()

            except:
                print("")

            try:
                post.imagen = request.FILES['imagen']
            except: 
                print("")
            
            post.save()

            return render(request, "Posts.html", {"mensaje": f'Modificado el articulo con éxito.', "imgPerfil": avatar.imagen.url})
        else:    
            return render(request, "Posteos/ModificarPost.html", {"mensaje": f'Error, no se pudo modificar.', "imgPerfil": avatar.imagen.url})

    else:
    
        miFormulario = Postformulario(instance = post)
    
        return render(request, "Posteos/ModificarPost.html", {'form': miFormulario, "imgPerfil": avatar.imagen.url})


def view_DetallesPost(request, id):

    Post = Posteo.objects.get(id = id)
    posteos = Posteo.objects.all()
    postFooter= posteos[::-1]

    try:
        avatar = Avatar.objects.get(user = request.user)
    except:
        return render(request, "Posteos/single-post.html", {"post": Post, "recentPost": postFooter[0:2]})
        
    return render(request, "Posteos/single-post.html", {"post": Post, "recentPost": postFooter[0:2], "imgPerfil": avatar.imagen.url})




