from django.urls import URLPattern, re_path
from jobs.api import views

URLPatterns = [
    path("jobs/", views.ListView.as_(), name="list"),
    path("jobs/<int:pk>", views.DetailView.as_view(), name="list"),
]
