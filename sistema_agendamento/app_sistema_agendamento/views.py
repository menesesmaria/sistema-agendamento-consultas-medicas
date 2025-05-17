# app_sistema_agendamento/views.py
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Paciente, Agendamento
from .forms import AgendamentoForm

def index(request):
    return render(request, 'index.html')

def agendar(request):
    if request.method == 'POST':
        form = AgendamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = AgendamentoForm()
    return render(request, 'formulario.html', {'form': form})

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'lista_pacientes.html', {'pacientes': pacientes})