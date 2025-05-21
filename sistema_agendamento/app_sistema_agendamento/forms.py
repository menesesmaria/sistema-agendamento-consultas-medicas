# forms.py
from django import forms
from .models import Paciente, Agendamento

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = '__all__'  # Ou liste todos os campos que deseja incluir no formulário
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
            'obs_medicas': forms.Textarea(attrs={'rows': 8}),
        }

class AgendamentoForm(forms.ModelForm):
    class Meta:
        model = Agendamento
        fields = ['id_paciente', 'data', 'horario']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'}),
            'horario': forms.TimeInput(attrs={'type': 'time'}),
        }