from django.shortcuts import render
from django.views.generic import ListView
from .models import Book
from rest_framework.views import APIView

# Create your views here.

class BookList(ListView):
  template_name: str="list.html"
  model = Book

class BookListAPI(APIView):
  permission_classes=[]