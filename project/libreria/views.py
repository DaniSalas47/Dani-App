from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from .models import Libro
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm, CustomUserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.

def inicio(request):
    return render(request, 'paginas/inicio.html')

def nosotros(request):
    return render(request, 'paginas/nosotros.html')

@login_required
def libros(request):
    libros = Libro.objects.all()
    return render(request, 'libros/index.html', {'libros': libros})

@login_required
def crear(request):
    return render(request, 'libros/crear.html')

@login_required
def editar(request):
    return render(request, 'libros/editar.html')

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
    template_name = "libros/login.html"
    next_page = "template/base.html"

def register(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('libreria:inicio') 
    else:
        form = CustomUserCreationForm()
    return render(request, "libros/register.html", {"form": form})