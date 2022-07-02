from django.shortcuts import render
from django.views.generic import ListView
from bookproject.book.selializers import BookSerializer
from .models import Book
from rest_framework.generics import ListCreateAPIView

# Create your views here.

class BookList(ListView):
  template_name: str="list.html"
  model = Book

class BookListAPI(ListCreateAPIView):
  queryset = Book.objects.all()
  serializer_class = BookSerializer
  permission_classes=[]
