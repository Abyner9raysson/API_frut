from django.urls import path
from . import views

urlpatterns = [
    path('produto/', views.produtos_view, name='produto')   
]