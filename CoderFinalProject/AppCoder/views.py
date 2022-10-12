from django.shortcuts import render

# Create your views here.

def banda(request):
    return render(request, "AppCoder/banda.html")


def empresa(request):
    return render(request, "AppCoder/empresa.html")


def integrantes(request):
    return render(request, "AppCoder/integrantes.html")
