from django.shortcuts import render, redirect
from gestion_inmuebles.forms import UsuarioForm, ProfileForm, InmuebleForm,FotoForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from gestion_inmuebles.models import Inmueble, Usuario,Comuna,Region,Foto

# Create your views here.

def registro(request):
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
            print('form  valid')
            form.save()
            return redirect('login')
        else:
            print('form  not valid')
            messages.error(request, "Por favor, corrige los errores en el formulario.")
            context = {'form':form}
            #return render(request, 'register.html', context)
    else:
        form = UsuarioForm()
    return render(request, 'register.html', {'form':form})

@login_required(login_url='/login/')
def pagina_principal(request):
    context  = {}
    return render(request,'index.html',context)

@login_required
def profile(request):
    user = request.user
    inmuebles = Inmueble.objects.filter(dueño=user)
    if request.method == 'POST':
        form = ProfileForm(request.POST,instance=user)
        if form.is_valid():
            form.save()  # Guarda los cambios
            return redirect('profile')  # Redirige a alguna página, como el perfil
    else:
        form = ProfileForm(instance=user)
    context={'form':form,'inmuebles':inmuebles}
    return render(request,'profile.html',context)

def inmuebles(request):
    regiones = Region.objects.all()
    inmuebles =Inmueble.objects.all()
    comunas = {}
    comuna = request.GET.get('comuna')
    region = request.GET.get('region')
    print('comuna:', comuna)
    print('region:', region)
   
    if region:
        inmuebles = inmuebles.filter(comuna__region__nombre=region)
        comunas = Comuna.objects.filter(region__nombre=region)
    if comuna:
        print('comuna:', comuna)
        inmuebles = inmuebles.filter(comuna__nombre=comuna)
        #inmuebles = inmuebles.filter(comuna__region__nombre='Valparaíso')
        pass
    context = {'inmuebles':inmuebles,
               'regiones':regiones,
               'comunas' : comunas,
               }
    return render(request,'inmuebles.html',context)

def inmuebles_detalle(request, id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    context={'inmueble':inmueble}
    return render(request, 'inmuebles_detalle.html',context )

@permission_required('gestion_inmuebles.add_inmueble',login_url='/')
def inmuebles_agregar(request):
    if request.method == 'POST':
        form = InmuebleForm(request.POST)
        if form.is_valid():
            user=Usuario.objects.get(username=request.user.username)
            inmueble = form.save(commit=False)  # Evitar guardar aún
            inmueble.dueño = user       # Asignar el dueño
            inmueble.save()                     # Ahora guardar el objeto
            return redirect('profile')  # Redirige después de guardar
    else:
        form = InmuebleForm()
    context={'form':form}
    return render(request, 'inmuebles_agregar.html',context)

#AGREGAR AUTORIZACION POR PERMISOS
def inmuebles_actualizar(request,id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    if request.method=='POST':
        form = InmuebleForm(request.POST,instance=inmueble)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = InmuebleForm(instance=inmueble)
    context={'form':form,'inmueble':inmueble}
    return render(request,'inmuebles_actualizar.html',context)

#AGREGAR AUTORIZACION POR PERMISOS
def inmuebles_eliminar(request, id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    print('eliminar',inmueble,inmueble.dueño,type(inmueble))
    user = Usuario.objects.get(id=request.user.id)
    print('eliminar',user)
    if inmueble.dueño == user:
        print('bandera')
        inmueble.delete()
    return redirect('profile')

def agregar_foto_a_inmueble(request,id_inmueble):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    if request.method=='POST':
        form = FotoForm(request.POST,request.FILES)
        if form.is_valid():
            foto = form.save(commit=False)
            foto.save()
            foto.inmueble.add(inmueble)
            #return redirect('profile')
            return redirect(request.META['HTTP_REFERER'])
    else:
        form = FotoForm()
    context = {
        'form':form,
        'inmueble':inmueble
               }
    return render(request,'agregar_foto.html',context)
#agregar verificacion de auth
#AGREGAR AUTORIZACION POR PERMISOS
def inmuebles_foto_eliminar(request, id_inmueble,id_foto):
    inmueble = Inmueble.objects.get(id=id_inmueble)
    foto = Foto.objects.get(pk=id_foto)
    user = Usuario.objects.get(id=request.user.id)
    print('eliminar foto:',foto.foto.url)
    if inmueble.dueño == user:
        inmueble.fotos.remove(foto)
        print('remove')
    return redirect('agregar_foto')