from django import forms

from .models import Productos, Categorias, Clientes, Motos


#  creamos la clase que tendra el formulario para registrar productos

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'description', 'cantidad', 'categoria']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'description': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'cantidad': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'categoria': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }
        categoria = forms.ModelChoiceField(
            queryset=Categorias.objects.all(), empty_label=None)


# creamos la clase que tendra el formulario de categorias

class CategoriasForm(forms.ModelForm):

    class Meta:
        model = Categorias
        fields = ['nombre']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }

# creamos la clase que tendra el formulario de clientes
class ClientesForm(forms.ModelForm):

    class Meta:
        model = Clientes
        fields = ['documento', 'nombres', 'telefono', 'email', 'genero']
        widgets = {
            'documento': forms.NumberInput(attrs={'class': 'form-control form-control-user', 'onkeypress': 'return(multiplenumber(event));', 'maxlength': '10', 'oninput': 'maxlengthNumber(this);'}),
            'nombres': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'telefono': forms.NumberInput(attrs={'class': 'form-control form-control-user', 'onkeypress': 'return(multiplenumber(event));', 'maxlength': '10', 'oninput': 'maxlengthNumber(this);'}),
            'email': forms.EmailInput(attrs={'class': 'form-control form-control-user'}),
            'genero': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
        }

# creamos la clase que tendra el formulario de motos

class MotosForm(forms.ModelForm):
    class Meta:
        model = Motos
        fields = ['placa', 'kilometraje', 'modelo', 'marca', 'color',
                  'carroceria', 'cilindraje', 'combustible', 'uso', 'usuario']
        widgets = {
            'placa': forms.TextInput(attrs={'class': 'form-control form-control-user', 'oninput': 'mayusculas();', 'id': 'placa'}),
            'kilometraje': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'modelo': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'marca': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'color': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'carroceria': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'cilindraje': forms.NumberInput(attrs={'class': 'form-control form-control-user'}),
            'combustible': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'uso': forms.TextInput(attrs={'class': 'form-control form-control-user'}),
            'usuario': forms.Select(attrs={'class': 'form-control form-control-user'}),
        }

        usuario = forms.ModelChoiceField(
            queryset=Clientes.objects.all(), empty_label=None
        )
