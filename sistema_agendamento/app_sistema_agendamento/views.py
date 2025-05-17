from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html')

def agendar(request):
    return render(request, 'agendar.html')

def cadastrar(request):
    return render(request, 'cadastrar.html')