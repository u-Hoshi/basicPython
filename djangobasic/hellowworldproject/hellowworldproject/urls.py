from django.contrib import admin
from django.urls import path,include
from .views import HellowWorldClass, helloworldfunction

urlpatterns = [
    path('admin/', admin.site.urls),
    path('helloworld/', helloworldfunction),
    path('helloworld2/', HellowWorldClass.as_view()), # クラスを使用する場合は".as_view()"をつける必要がある
    path("",include("helloworldapp.urls"))
]

