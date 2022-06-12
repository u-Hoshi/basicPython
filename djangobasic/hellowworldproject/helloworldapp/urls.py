from django.urls import path
from .views import  helloworldapp

urlpatterns = [
    path("helloworldapp/",helloworldapp)
]

