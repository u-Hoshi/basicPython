from django.contrib import admin
from .models import Weather

# Register your models here.
# 管理画面(8000/admin)に表示させるmodelsを記述

admin.site.register(Weather)