from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *




@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal Info', {'fields': ('first_name', 'last_name', 'email')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
        ('Custom fields', {'fields': ('role',)}),  # Add custom field to fieldset
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2'),
        }),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'role')  # Add 'role' to list_display
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups', 'role')  # Add 'role' to list_filter
    search_fields = ('username', 'first_name', 'last_name', 'email', 'role')  # Add 'role' to search_fields
    ordering = ('username',)

# admin.site.register(CustomUser, CustomUserAdmin)
