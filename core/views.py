from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate, login
from .models import Reserva,Room, Message
from django.contrib import messages
from django.http import HttpResponse, JsonResponse


##prueba de envio de email


# Create your views here.
def home(request):
    
    return render(request,'core/home.html')

def nosotros(request):
    return render(request,'core/nosotros.html')

@login_required
###############
def products(request):
    reservaListados = Reserva.objects.all()
    messages.success(request, 'reserva listados!')
    return render(request, "core/products.html", {"reservas": reservaListados})
#############
def exit(request):
    logout(request)
    return redirect('home')
################
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
    email = request.POST['txtEmail']
    servicio =request.POST['txtServicio']
    fecha_hora= request.POST['txtFechaReserva']


    reserva = Reserva.objects.create(
    codigo=codigo, nombre=nombre, creditos=creditos, email=email, servicio=servicio , fecha_hora=fecha_hora)
    messages.success(request, 'Reserva registrada!')
    return redirect('products')

############
def editar(request, codigo):
    reserva = Reserva.objects.get(codigo=codigo)
    return render(request, 'core/editar.html', {"reserva": reserva})

###################
def editarReserva(request):
    codigo = request.POST['txtCodigo']
    nombre = request.POST['txtNombre']
    creditos = request.POST['numCreditos']
    servicio =request.POST['txtServicio']
   
    

    reserva = Reserva.objects.get(codigo=codigo)
    reserva.nombre = nombre
    reserva.creditos = creditos
    reserva.servicio = servicio
    
    reserva.save()

    messages.success(request, 'Reserva actualizado!')

    return redirect('products')

##########################
def eliminarReserva(request, codigo):
    reserva = Reserva.objects.get(codigo=codigo)
    reserva.delete()

    messages.success(request, '¡Reserva eliminada!')

    return redirect('products')


###############################################

# Create your views here.


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'core/room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})