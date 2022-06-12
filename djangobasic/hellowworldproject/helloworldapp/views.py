from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def helloworldapp(request):
  return HttpResponse("hoge")