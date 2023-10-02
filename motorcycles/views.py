from .models import Clientes
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import ProductosForm, CategoriasForm, ClientesForm, MotosForm
from .models import Productos, Categorias, Clientes, Motos
from django.contrib.auth.decorators import login_required


# Create your views here.

# Creamos el metodo para mostrar la interfaz inicial o principal
def home(request):
    return render(request, 'home.html')


#  creamos el metodo para registrar un nuevo usuario
def signup(request):

    if request.method == 'GET':
        return render(request, 'signup.html', {
            'form': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            # registro de usuario

            try:
                user = User.objects.create_user(
                    username=request.POST['document'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('productos')
            except IntegrityError:

                return render(request, 'signup.html', {
                    'form': UserCreationForm,
                    'error_register': 'El numero de documento ya esta registrado'
                })

        return render(request, 'signup.html', {
            'form': UserCreationForm,
            'error_register': 'Las contraseñas deben ser iguales'
        })


# creamos una nueva funcion para validar el logueo del usuario

def iniciar_sesion(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['document'], password=request.POST['password'])

        if user is None:
            return render(request, 'signin.html', {
                'form': AuthenticationForm,
                'error_login': 'El numero de documento o contraseña son incorrectos'
            })
        else:
            login(request, user)
            return redirect(productos)


# creamos un metodo para borrar la sesion del usuario que esta logueado

def cerrar_sesion(request):
    logout(request)
    return redirect('home')

# creamos una funcion para mostrar los productos que estan registrados


@login_required
def productos(request):
    productos = Productos.objects.all()
    categorias = Categorias.objects.all()
    return render(request, 'productos.html', {'producto': productos, 'categoria': categorias})

# creamos una funcion para crear nuevos productos


@login_required
def crear_producto(request):
    if request.method == 'GET':
        return render(request, 'create_product.html', {
            'form': ProductosForm
        })

    else:
        try:
            form = ProductosForm(request.POST)
            new_Product = form.save(commit=False)
            new_Product.user = request.user
            new_Product.save()
            return redirect('/productos', {
                'confirmacion': 'El producto ha sido registrado exitosamente'
            })
        except ValueError:
            return render(request, 'create_product.html', {
                'form': ProductosForm,
                'error': 'Error al momento de registrar los productos'
            })


@login_required
# creamos un metodo para actualizar los datos del producto seleccionado
def update_producto(request, producto_id):
    if request.method == 'GET':
        producto = get_object_or_404(Productos, pk=producto_id)
        form = ProductosForm(instance=producto)
        return render(request, 'update_product.html', {
            'producto': producto,
            'form': form
        })
    else:
        try:
            producto = get_object_or_404(Productos, pk=producto_id)
            formProductos = ProductosForm(request.POST, instance=producto)
            formProductos.save()
            return redirect('productos')
        except ValueError:
            return render(request, 'update_producto.html', {
                'producto': producto,
                'form': form,
                'error': 'Error al momento de actualizar el producto'
            })


@login_required
# creamos un nuevo metodo para borrar el producto seleccionado
def delete_product(request, producto_id):
    producto = get_object_or_404(Productos, pk=producto_id)
    if request.method == 'POST':
        producto.delete()
        return redirect('productos')


@login_required
# creamos un metodo para mostrar todas las categorias de productos registrados
def categorias(request):
    categorias = Categorias.objects.all()
    return render(request, 'category.html', {'categoria': categorias})


@login_required
# creamos una nueva funcion para mostrar el formulario dependiendo el metodo que se este implementando
def crear_categoria(request):
    if request.method == 'GET':
        return render(request, 'create_category.html', {
            'form': CategoriasForm,
        })

    # si se esta implementando el metodo POST se realizara el registro de dicha categoria
    else:
        try:
            formCategoria = CategoriasForm(request.POST)
            new_Category = formCategoria.save(commit=False)
            new_Category.save()
            return redirect('/categorias', {
                'confirmacion': 'La categoria ha sido creada exitosamente'
            })

        except ValueError:
            return render(request, 'create_category.html', {
                'form': CategoriasForm,
                'error': 'Error al momento de registrar la nueva categoria de lo productos'
            })


@login_required
# creamos una nueva funcion para mostrar todos los clientes que esten registrados
def cliente(request):
    clientes = Clientes.objects.all()
    return render(request, 'clientes.html', {
        'clientes': clientes
    })


@login_required
# creamos una nueva funcion para mostrar el formulario y registrar mediante la clase ClientesForm
def create_client(request):
    if request.method == 'GET':
        return render(request, 'create_client.html', {
            'form': ClientesForm
        })
    else:
        try:
            formCliente = ClientesForm(request.POST)

            # Verificamos si el formulario es válido

            if formCliente.is_valid():
                # Capturamos el número de documento del formulario
                documento = formCliente.cleaned_data['documento']

                # Verificamos si ya existe un cliente con el mismo número de documento

                if Clientes.objects.filter(documento=documento).exists():
                    return render(request, 'create_client.html', {
                        'form': ClientesForm,
                        'error': 'El número de documento ya está registrado.'
                    })

                # Si no existe, guardamos el nuevo cliente
                newClient = formCliente.save(commit=False)
                newClient.save()

                return redirect('/clientes', {
                    'confirmacion': 'El nuevo Cliente se registró correctamente.'
                })
            else:
                return render(request, 'create_client.html', {
                    # Pasa el formulario con errores para que los errores se muestren en la plantilla
                    'form': formCliente,
                    'error': 'El formulario contiene errores. Por favor, corrígelos e inténtalo de nuevo.'
                })

        except ValueError:
            return render(request, 'create_client.html', {
                'form': ClientesForm,
                'error': 'Error al momento de registrar un nuevo cliente.'
            })


@login_required
def update_client(request, cliente_documento):
    cliente = get_object_or_404(Clientes, pk=cliente_documento)

    if request.method == 'GET':
        form = ClientesForm(instance=cliente)
        # Agregar el atributo readonly al campo "documento"
        form.fields['documento'].widget.attrs['readonly'] = True

        return render(request, 'update_client.html', {
            'cliente': cliente,
            'form': form,
        })
    else:
        try:
            clienteActualizado = get_object_or_404(
                Clientes, pk=cliente_documento)
            formClient = ClientesForm(
                request.POST, instance=clienteActualizado)
            formClient.save()
            return redirect('/clientes')
        except ValueError:
            return render(request, 'update_client.html', {
                'cliente': cliente,
                'form': form,
                'error': 'Error al momento de actualizar el cliente'
            })


@login_required
# creamos una nueva funcion para eliminar el cliente seleccionado
def delete_client(request, cliente_documento):
    cliente = get_object_or_404(Clientes, pk=cliente_documento)
    if request.method == 'POST':
        cliente.delete()
        return redirect('/clientes')


@login_required
# creamos una nueva funcion para mostrar el listado de motos que esta registrado
def motos(request):
    motos = Motos.objects.all()
    clientes = Clientes.objects.all()
    return render(request, 'motos.html', {
        'motos': motos,
        'clientes': clientes
    })


@login_required
# creamos una nueva funcion para mostrar el formulario de registro de motos o registrar la moto mediante el metodo POST
def crear_moto(request):
    if request.method == 'GET':
        return render(request, 'create_motorcycle.html', {
            'form': MotosForm
        })

    else:
        try:
            formMotos = MotosForm(request.POST)
            newMotorcycle = formMotos.save(commit=False)
            newMotorcycle.save()
            return redirect('/motos', {
                'confirmacion': 'La nueva moto fue creada con exito!'
            })

        except ValueError:
            return render(request, "create_motorcycle.html", {
                'form': MotosForm,
                'error': 'Error al momento de registrar la moto'
            })


# creamos una funcion para actualizar los datos de la moto
@login_required
def update_moto(request, moto_placa):
    moto = get_object_or_404(Motos, pk=moto_placa)
    if request.method == 'GET':
        form = MotosForm(instance=moto)
        form.fields['placa'].widget.attrs['readonly'] = True
        return render(request, 'update_moto.html', {
            'moto': moto,
            'form': form
        })
    elif request.method == 'POST':
        try:
            moto = get_object_or_404(Motos, pk=moto_placa)
            formMotos = MotosForm(request.POST, instance=moto)
            formMotos.save()
            return redirect('motos')
        except ValueError:
            return render(request, 'update_moto.html', {
                'moto': moto,
                'form': form,
                'error': 'Error al momento de actualizar los datos de la moto'
            })


@login_required
# creamos una nueva funcion para borrar la moto seleccionada
def delete_moto(request, moto_placa):
    moto = get_object_or_404(Motos, pk=moto_placa)
    if request.method == 'POST':
        moto.delete()
        return redirect('motos')
