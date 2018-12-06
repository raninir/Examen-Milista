from django import forms
from api.models import Lista , Usuario, ListaUsuario, Tienda, Producto , ListaProducto, TiendaProducto


#ESTADO DE LA MASCOTA
estadoLista=(
    ('Proceso', 'Proceso'),
    ('Completada', 'Completada'),

)

estadoTienda=(
    ('Pendiente', 'Pendiente'),
    ('Aprobada', 'Aprobada'),
)


tipoTienda=(
    ('Fisica', 'Fisica'),
    ('Online', 'Online'),
)


#AGREGAR USUARIOS
class AgregarUsuario(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    correo=forms.EmailField(widget=forms.EmailInput(),label="Correo")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")
    

#INGRESAR AL SISTEMA
class Login(forms.Form):
    username=forms.CharField(widget=forms.TextInput(),label="Nombre Usuario")
    password=forms.CharField(widget=forms.PasswordInput(),label="contraseña")

class listas(forms.Form):
    nombreLista=forms.CharField(widget=forms.TextInput(),label="Nombre Lista")
   

class Productos(forms.Form):
    Nombreproducto=forms.CharField(widget=forms.TextInput(),label="Nombre Producto")
    costoPresupuesto=forms.IntegerField(widget=forms.TextInput(),label="Costo Presupuestado")
    costoReal=forms.IntegerField(widget=forms.TextInput(),label="Costo Real")
    descripcionProducto=forms.CharField(widget=forms.TextInput(),label="Descripcion")

#CLASE DE LA TIENDA
class Tiendas(forms.Form):
    fotoTienda=forms.ImageField()
    nombreTienda=forms.CharField(widget=forms.TextInput(),label="Nombre Tienda")
    nombreSucursal=forms.CharField(widget=forms.TextInput(),label="Nombre Sucursal")
    direccion=forms.CharField(widget=forms.TextInput(),label="Dirección")
    ciudad=forms.CharField(widget=forms.TextInput(),label="Ciudad")
    tipoTienda=forms.ChoiceField(choices=tipoTienda, initial='Fisica',label="Tipo Tienda")
    paginaWeb=forms.CharField(widget=forms.TextInput(),label="Pagina Web")


