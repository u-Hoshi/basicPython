from .views import GoogleLoginView
from django.urls import path, include

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('google/', GoogleLoginView.as_view(),name="google"),
]
