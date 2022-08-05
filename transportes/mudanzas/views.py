from string import capwords
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def inicio(request):
    return HttpResponse("<h1>PROGRAMA DE PRUEBA</h1>")

def prueba(request):
    return render(request, 'paginas/prueba.html')

   

