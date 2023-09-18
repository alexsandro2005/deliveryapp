from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User

# En este archivo se crean los modelos

# creamos la clase clientes

class Clientes(models.Model):
    documento = models.CharField(max_length=10, primary_key=True, null=False)
    nombres = models.CharField(max_length=100,null=False)
    telefono = models.CharField(max_length=10, null=False)
    email = models.EmailField(max_length=100, null=False)
    genero = models.CharField(max_length=100, null=False)
    fecha_registro = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.nombres

# creamos la clase motos para llevarnos el documento del usuario dueño de la moto


class Motos(models.Model):
    placa = models.CharField(max_length=6, primary_key=True, null=False, unique=True)
    kilometraje = models.IntegerField(max_length=6,null=False)
    modelo = models.IntegerField(max_length=4,null=False)
    marca = models.CharField(max_length=50,null=False)
    color = models.CharField(max_length=50, null=False)
    carroceria = models.CharField(max_length=50, null=False)
    cilindraje = models.IntegerField(max_length=4, null=False)
    combustible = models.CharField(max_length=50, null=False)
    uso = models.CharField(max_length=50, null=False)
    usuario = models.ForeignKey(Clientes, on_delete=models.CASCADE)



# Creamos la clase Categorias
class Categorias(models.Model):
    nombre = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.nombre

# Luego creamos el modelo de productos
class Productos(models.Model):
    id = models.AutoField(primary_key=True, null=False)
    nombre = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True, null=True)
    cantidad = models.BigIntegerField(null=False)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    fecha_registro = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.nombre + '- by ' + self.user.username