from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.

def homeView(request):
    return render(request, 'home/home.html') # busca el html para mostrarlo al usuario


def contacto(request):
    return render(request, 'home/contacto.html')

def galeria(request):
    return render(request, 'home/galeria.html')
