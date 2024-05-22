from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, ProductForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'index.html', {})

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')  # Redirige a la página de perfil después del registro
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=username_or_email, password=password)
            if user is None:
                # Si la autenticación con el correo electrónico falla, intentar con el nombre de usuario
                user = authenticate(request, username=username_or_email, password=password)
                
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirige a la página de inicio después del inicio de sesión
    else:
        form = CustomAuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def profile_view(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('product_list')  # Redirigir a una lista de productos después de crear uno nuevo
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.filter(public=True)
    return render(request, 'product_list.html', {'products': products})