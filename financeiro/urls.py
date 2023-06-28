from django.urls import path
from . import views

urlpatterns = [
    path('financeiro/', views.financeiro_view, name='financeiro'),
]