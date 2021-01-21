from django.urls import path
from . import views

urlpatterns = [
    path('', views.getDetails),
    path('create', views.createDetails),
    path('<int:cust_id>', views.deleteDetails),
]