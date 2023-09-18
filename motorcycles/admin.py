from django.contrib import admin
from .models import Productos, Categorias, Clientes, Motos

class ProductosAdmin(admin.ModelAdmin):
    readonly_fields = ("fecha_registro",)

class ClientesAdmin(admin.ModelAdmin):
    
    pass

class CategoriasAdmin(admin.ModelAdmin):
   
    pass

class MotosAdmin(admin.ModelAdmin):
    
    pass

# Registrar los modelos con sus respectivas clases ModelAdmin
admin.site.register(Productos, ProductosAdmin)
admin.site.register(Clientes, ClientesAdmin)
admin.site.register(Categorias, CategoriasAdmin)
admin.site.register(Motos, MotosAdmin)
