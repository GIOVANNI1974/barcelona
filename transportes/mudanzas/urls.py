from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('prueba', views.prueba, name='prueba'),
]
