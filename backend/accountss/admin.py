from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Account

#Esta clase se corresponde con el encabezado que aparece en el apartado de account
#Mostrando los elementos que aparecen en la lista de abajo email, first_name etc

class AccountAdmin(UserAdmin):  
    list_display = ('email', 'first_name', 'last_name',  'username', 'last_login', 'is_active', 'date_joined')
    list_display_links = ('email', 'first_name', 'last_name')
    readonly_fields = ('last_login', 'date_joined')
    ordering = ('-date_joined',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()  #This makes our password only readable not editable

admin.site.register(Account, AccountAdmin)
