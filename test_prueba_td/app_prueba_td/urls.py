from django.urls import path
from django.contrib.auth import views as auth_views
from .views import index, register, login_view, profile_view, add_product, product_list, add_to_cart, detail_product, remove_from_cart, make_purchase, order_list, seller_orders

urlpatterns = [
    path('', index,name='home'),
    path('register/', register, name='register'),
    path('login/', login_view, name='login'),
    path('profile/', profile_view, name='profile'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('add_product/', add_product, name='add_product'),
    path('product_list/', product_list, name='product_list'),
    ######
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('detail_product/', detail_product, name='detail_product'),
    path('remove_from_cart/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('make_purchase/', make_purchase, name='make_purchase'),
    path('orders/', order_list, name='order_list'),
    path('seller_orders/', seller_orders, name='seller_orders'),
]