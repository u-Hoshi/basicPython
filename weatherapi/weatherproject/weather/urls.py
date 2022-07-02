from django.urls import path
from .views import TopView

urlpatterns = [
  path("top/", TopView.as_view())
]
