from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Product

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ['email', 'username', 'address', 'phone', 'user_type', 'is_staff', 'is_active']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('address', 'phone', 'user_type')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('address', 'phone', 'user_type')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Product)