# app_sistema_agendamento/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendar/', views.agendar, name='agendar'),
    path('cadastrar/', views.cadastrar, name='cadastrar'),  # Adicionei o name
]