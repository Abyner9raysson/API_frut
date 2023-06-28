from django.urls import path
from . import views

urlpatterns = [
    path('recursosHumanos/', views.RH_view, name='recursosHumanos')   
]