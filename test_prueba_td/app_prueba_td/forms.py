from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import CustomUser, Product

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'address', 'phone', 'user_type')

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'address', 'phone', 'user_type')
        
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['image', 'name', 'description', 'price', 'public'] 

class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(label='Username or Email')