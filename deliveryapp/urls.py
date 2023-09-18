"""
URL configuration for deliveryapp project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from motorcycles import views

urlpatterns = [

    # url que mostrara la interfaz del admin de django
    path("admin/", admin.site.urls),
    # url que mostrara la interfaz principal de la aplicacion
    path('',views.home, name='home'),
    # url que mostrara el formuario de registro
    path('signup/',views.signup, name='signup'),
    # url que mostrara la lista de productos
    path('productos/', views.productos, name="productos"),
    # url para cerrar la sesion del usuario en la aplicacion  
    path('logout/',views.cerrar_sesion, name="loguout"),
    # url para iniciar la sesion del usuario
    path('signin/',views.iniciar_sesion, name="signin"),
    # url para registrar un nuevo producto
    path('create_product/', views.crear_producto, name="crear_producto"),
    # url para mostrar las categorias que estan registradas
    path('categorias/', views.categorias, name="categorias"),
    # url para crear una nueva categoria
    path('create_category/', views.crear_categoria, name="create_category"),
    # url para mostrar el listado de clientes registrados
    path('clientes/', views.cliente, name="cliente"),
    # url para crear nuevos clientes
    path('create_client/', views.create_client, name="create_client"),
    # url para mostrar las motos registradas
    path('motos/', views.motos, name="motos"),
    # url para registrar un nueva moto 
    path('create_motorcycle/', views.crear_moto, name="crear_moto"),
    # url para actualizar los datos de un producto
    path('productos/<int:producto_id>/', views.update_producto, name="update_producto"),
    # url para actualizar los datos de un cliente
    path('clientes/<int:cliente_documento>/', views.update_client, name="update_client"),
    # url para actualizar los datos de la moto seleccionada
    path('motos/<str:moto_placa>/', views.update_moto, name="update_moto"),
    # url para eliminar un poducto
    path('productos/<int:producto_id>/delete', views.delete_product, name="delete_product"),
    # url para eliminar un cliente registrado
    path('clientes/<int:cliente_documento>/delete', views.delete_client, name="delete_client"),
    # url para eliminar una moto registrada
    path('motos/<str:moto_placa>/delete', views.delete_moto, name="delete_moto"),
]
