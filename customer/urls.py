from django.urls import path
from .views import CreateDetails

urlpatterns = [
    path('create', CreateDetails),
]