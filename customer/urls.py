from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_details),
    path('create', views.createDetails),
    path('<int:cust_id>', views.deleteDetails),
]
