from django.shortcuts import render

from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hola desde Django")

def saludar_usuario(request, nombre):
    return HttpResponse(f"Hola, {nombre}!")

def mostrar_numero(request, numero):
    return HttpResponse(f"El numero es: {numero}")


def inicio(request):
    contexto = {
        'nombre':'Juan'
    }
    return render(request, 'index.html', contexto)