from django.contrib import admin

# Register your models here.

from .models import CustomerUser

admin.site.register(CustomerUser)