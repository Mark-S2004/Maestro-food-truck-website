from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomerCreationForm, CustomerChangeForm
from .models import Customer

class CustomerAdmin(UserAdmin):
    add_form = CustomerCreationForm
    form = CustomerChangeForm
    model = Customer
    list_display = ['username', 'email', 'first_name', 'last_name', "phone", "address"]

admin.site.register(Customer, CustomerAdmin)