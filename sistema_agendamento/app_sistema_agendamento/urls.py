# app_sistema_agendamento/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('agendar/', views.agendar, name='agendar'),
    path('sucesso/', lambda request: render(request, 'sucesso.html'), name='sucesso'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),  # Adicionei o name
]