from django.urls import path
from . import views
from .views import create_superuser

urlpatterns = [
    path('', views.home, name="home"),
    path('create_admin/', create_superuser),
]