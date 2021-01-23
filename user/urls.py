from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>', views.user_detail),
    path('all', views.get_users),
    path('create', views.create_user),
]
