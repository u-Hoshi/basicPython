from django.urls import path
from .views import TopView, WeatherAPIView

urlpatterns = [
  path("top/", TopView.as_view()),
  path("api/", WeatherAPIView.as_view())
]
