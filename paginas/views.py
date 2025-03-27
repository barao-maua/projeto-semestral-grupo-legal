from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def cadastro_view(request):
    return render(request, 'cadastro.html')