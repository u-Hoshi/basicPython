from django.http import HttpResponse

def helloworldfunction(request):
  returnedobject=HttpResponse("<h1>hellow world</h1>")
  return returnedobject
