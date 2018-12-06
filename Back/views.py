from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.core import serializers
from django.contrib.auth.models import User
from .forms import AgregarUsuario, Login, Tiendas, Productos, listas
from api.models import Usuario, Lista, Tienda, Producto, ListaUsuario, ListaProducto, TiendaProducto
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib import messages
from django.shortcuts import render, redirect
from social_django.models import UserSocialAuth
import json



#defino acciones posibles para establecer permisos
acciones=[
   {'Mostrar':'Home','url':'inicio'}
]
# Create your views here.

def index(request):
    return render(request, "index.html")


def admin(request):
    return render(request, "/admin")



@login_required(login_url='login')
def salir(request):
    logout(request)
    return redirect('/')

#ingreso al sistema
def ingresar(request):
    form=Login(request.POST or None)
    if form.is_valid():
        data=form.cleaned_data
        user=authenticate(username=data.get("username"),password=data.get("password"))
        if user is not None:
            login(request,user)
            return redirect('inicio')

    return render(request,"Login.html",{'form':form,})



#permite al usuario llenar un formulario y registrarse en el sistema
def registro(request):
    actual=request.user
    form=AgregarUsuario(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        regDB=User.objects.create_user(data.get("username"),data.get("correo"), data.get("password"))
        regDB.save()
       # usuario.save()
    usuarios=Usuario.objects.all()
    form=AgregarUsuario()
    contexto={
        'actual':actual, 
        'form':form, 
        'usuarios':Usuario,
        }
    if request.POST:
        return render(request, "registroexitoso.html")
    return render(request, "registrarse.html", contexto)    

#LISTAS




@login_required(login_url='login')
def agregarproductos (request):
    actual=request.user
    form=Productos(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        producto=Producto(Nombreproducto=data.get("Nombreproducto"),costoPresupuesto=data.get("costoPresupuesto"),costoReal=data.get("costoReal") ,descripcionProducto=data.get("descripcionProducto"))
        producto.save()
    producto=Producto.objects.all()
    form=Productos()
    contexto={
        'actual':actual, 
        'form':form, 
        'producto':producto,
        }
    return render(request, "AgregarProducto.html", contexto)    



@login_required(login_url='login')
def agregartiendas(request):
    actual=request.user
    form=Tiendas(request.POST)
    if form.is_valid():
        data=form.cleaned_data
        tienda=Tienda(fotoTienda=data.get("fotoTienda"),nombreTienda=data.get("nombreTienda"),nombreSucursal=data.get("nombreSucursal"),direccion=data.get("direccion"),ciudad=data.get("ciudad")  ,tipoTienda=data.get("tipoTienda"),paginaWeb=data.get("paginaWeb"))
        tienda.save()
    tienda=Tienda.objects.all()
    form=Tiendas()
    contexto={
        'actual':actual, 
        'form':form, 
        'tienda':tienda,
        }
    return render(request, "AgregarTiendas.html", contexto)    


