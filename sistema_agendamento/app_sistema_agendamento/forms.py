# app_sistema_agendamento/forms.py
from django import forms
from .models import Agendamento

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['id_paciente', 'data', 'horario']  # Ajuste conforme necessário