from django.http import HttpResponse
from django.views.generic import TemplateView

def helloworldfunction(request):
  returnedobject=HttpResponse("<h1>hellow world</h1>")
  return returnedobject

class HellowWorldClass(TemplateView):
  template_name: str = "hello.html" 