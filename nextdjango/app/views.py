from django.shortcuts import render
from rest_framework import generics
from .serializers import PostSerializers
from .models import Post
from rest_framework.permissions import AllowAny

# Create your views here.

class PostView(generics.ListAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers
  permission_classes = (AllowAny,) # permission_classesにAllowAnyを記述することでログインしてなくてもアクセスできるようになる


class PostDetailView(generics.RetrieveAPIView):
  queryset = Post.objects.all()
  serializer_class = PostSerializers
  permission_classes = (AllowAny,) # permission_classesにAllowAnyを記述することでログインしてなくてもアクセスできるようになる