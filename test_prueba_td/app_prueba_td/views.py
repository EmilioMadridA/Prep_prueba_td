from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from .forms import CustomUserCreationForm, ProductForm, CustomAuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Product, Order, OrderItem
from django.contrib.auth import get_user_model
from django.utils import timezone

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

# FUNCIONA
# @login_required
# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('product_list')  # Redirigir a una lista de productos después de crear uno nuevo
#     else:
#         form = ProductForm()
#     return render(request, 'add_product.html', {'form': form})

# TEST
@login_required
def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            return redirect('product_list')  # Redirigir a una lista de productos después de crear uno nuevo
    else:
        form = ProductForm()
    return render(request, 'add_product.html', {'form': form})

@login_required
def product_list(request):
    products = Product.objects.filter(public=True)
    return render(request, 'product_list.html', {'products': products})

# Añade esta vista para manejar la acción de añadir al carrito

# FUNCIONA
# @login_required
# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart = request.session.get('cart', [])
#     cart.append(product_id)
#     request.session['cart'] = cart
#     return redirect('product_list')

# TEST
@login_required
def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}
    if str(product_id) in cart:
        cart[str(product_id)] += 1
    else:
        cart[str(product_id)] = 1
    request.session['cart'] = cart
    return redirect('product_list')

# FUNCIONA
# @login_required
# def detail_product(request):
#     cart = request.session.get('cart', [])
#     products = Product.objects.filter(id__in=cart)
#     return render(request, 'detail_product.html', {'products': products})

# TEST
@login_required
def detail_product(request):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}
    products = Product.objects.filter(id__in=cart.keys())
    cart_items = []
    for product in products:
        quantity = cart[str(product.id)]
        total_amount = product.price * quantity
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'total_amount': total_amount
        })
    return render(request, 'detail_product.html', {'cart_items': cart_items})

# FUNCIONA
# @login_required
# def remove_from_cart(request, product_id):
#     cart = request.session.get('cart', [])
#     if product_id in cart:
#         cart.remove(product_id)
#     request.session['cart'] = cart
#     return redirect('detail_product')

# TEST
@login_required
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}
    if str(product_id) in cart:
        if cart[str(product_id)] > 1:
            cart[str(product_id)] -= 1
        else:
            del cart[str(product_id)]
    request.session['cart'] = cart
    return redirect('detail_product')

@login_required
def make_purchase(request):
    cart = request.session.get('cart', {})
    if not isinstance(cart, dict):
        cart = {}

    if cart:
        order = Order.objects.create(user=request.user, created_at=timezone.now())
        for product_id, quantity in cart.items():
            product = get_object_or_404(Product, id=product_id)
            OrderItem.objects.create(order=order, product=product, quantity=quantity)
        
        # Vaciar el carrito después de realizar la compra
        request.session['cart'] = {}
        return redirect('order_list')

    return redirect('detail_product')

@login_required
def order_list(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'order_list.html', {'orders': orders})

@login_required
def seller_orders(request):
    if request.user.user_type != 'seller':
        return redirect('home')

    orders = Order.objects.filter(items__product__user=request.user).distinct()
    seller_orders = []

    for order in orders:
        seller_items = order.items.filter(product__user=request.user)
        total_amount = sum(item.product.price * item.quantity for item in seller_items)
        seller_orders.append({
            'order': order,
            'items': seller_items,
            'total_amount': total_amount
        })

    return render(request, 'seller_orders.html', {'seller_orders': seller_orders})