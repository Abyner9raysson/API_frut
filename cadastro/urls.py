from django.urls import path
from . import views

urlpatterns = [
    path('cadastro/', views.cad_view, name='cadastro')   
]