from django.contrib import admin
from .models import AddUser

class AddUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'patronym')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'patronym')

admin.site.register(AddUser, AddUserAdmin)

# Register your models here.
