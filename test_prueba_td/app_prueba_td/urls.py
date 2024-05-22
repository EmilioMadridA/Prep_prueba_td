from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, register, login_view, profile_view, add_product, product_list

urlpatterns = [
    path('', index,name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
]