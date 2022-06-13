from django.urls import include, path
from .views import BookList

urlpatterns = [
    path('list/',BookList.as_view()),
]
