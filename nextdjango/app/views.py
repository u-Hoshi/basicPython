from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializers
from .models import Post

# Create your views here.

class PostView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers


class PostDetailView(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers