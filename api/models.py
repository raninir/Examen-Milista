from django.db import models
from django.contrib.auth.models import User



# Create your models here.
#manejo de usuarios perzonalizados
class Usuario(models.Model):
    codigoUsuario=models.AutoField(primary_key=True)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

#modelo de la mascota
class Lista(models.Model):
    codigoLista=models.AutoField(primary_key=True)
    nombreLista=models.CharField(max_length=20,verbose_name="Nombre Lista")
   

class Tienda(models.Model):
    codigoTienda=models.AutoField(primary_key=True)
    fotoTienda = models.ImageField(upload_to="fotos/")
    nombreTienda=models.CharField(max_length=20,verbose_name="Nombre Tienda")
    nombreSucursal=models.CharField(max_length=20,default="",verbose_name="Nombre Sucursal")
    direccion=models.CharField(max_length=50,default="",verbose_name="Direccion")
    ciudad=models.CharField(max_length=30,default="",verbose_name="Ciudad")
    tipoTienda=models.CharField(max_length=30,default="Fisica",verbose_name="Tipo Tienda")
    paginaWeb=models.CharField(max_length=50,default="",verbose_name="Pagina Web")
    estadoTienda=models.CharField(max_length=30,default="Pendiente",verbose_name="Estado Tienda")

class Producto(models.Model):
    codigoProducto=models.AutoField(primary_key=True)
    Nombreproducto=models.CharField(max_length=50,default="",verbose_name="Nombre Producto")
    costoPresupuesto=models.PositiveIntegerField(default="0",verbose_name="Costo Presupuestado")
    costoReal=models.PositiveIntegerField(default="0",verbose_name="Costo Real")
    descripcionProducto=models.CharField(max_length=50,default="",verbose_name="Descripcion")


class ListaUsuario(models.Model):
    codigoLista=models.ForeignKey(Lista,on_delete=models.CASCADE)
    codigoUsuario=models.ForeignKey(Usuario,on_delete=models.CASCADE)


class ListaProducto(models.Model):
    codigoLista=models.ForeignKey(Lista,on_delete=models.CASCADE)
    codigoProducto=models.ForeignKey(Producto,on_delete=models.CASCADE) 


class TiendaProducto(models.Model):
    codigoTienda=models.ForeignKey(Tienda,on_delete=models.CASCADE)
    codigoProducto=models.ForeignKey(Producto,on_delete=models.CASCADE)      




class ListaCompras(models.Model):
    idLista=models.AutoField(primary_key=True)
    nombreproducto=models.CharField(max_length=20)
    precio=models.CharField(max_length=100)
    precioreal=models.CharField(max_length=100)
    tienda=models.CharField(max_length=100)
    notas=models.CharField(max_length=100)
