from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Reserva
from django.contrib import messages
##prueba de envio de email
from django.core.mail import EmailMessage
from django.template.loader import render_to_string

# Create your views here.
def home(request):
    
    return render(request, 'core/home.html')

def home(request):
    reservaListados = Reserva.objects.all()
    messages.success(request, 'reserva listados!')
    return render(request, "core/products.html", {"reservas": reservaListados})


@login_required
def products(request):
    return render(request, 'core/products.html')

def exit(request):
    logout(request)
    return redirect('home')

def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)

        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form

    return render(request, 'registration/register.html', data)


#########################################




def registrarReserva(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    reserva = Reserva.objects.create(
    codigo=codigo, nombre=nombre, creditos=creditos)
    messages.success(request, 'Reserva registrada!')
    return redirect('/')


def editar(request, codigo):
    reserva = Reserva.objects.get(codigo=codigo)
    return render(request, 'core/editar.html', {"reserva": reserva})


def editarReserva(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']

    reserva = Reserva.objects.get(codigo=codigo)
    reserva.nombre = nombre
    reserva.creditos = creditos
    reserva.save()

    messages.success(request, 'Reserva actualizado!')

    return redirect('/')


def eliminarReserva(request, codigo):
    reserva = Reserva.objects.get(codigo=codigo)
    reserva.delete()

    messages.success(request, '¡Reserva eliminada!')

    return redirect('/')


def contact (request):