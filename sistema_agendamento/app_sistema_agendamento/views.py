# app_sistema_agendamento/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente, Agendamento
from .forms import AgendamentoForm, PacienteForm


def index(request):
    return render(request, 'index.html')

# views.py
def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AgendamentoForm()
    
    return render(request, 'agendar.html', {'form': form})

def cadastrar(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')  # Redireciona para a página inicial após o cadastro
    else:
        form = PacienteForm()
    
    return render(request, 'cadastrar.html', {'form': form})