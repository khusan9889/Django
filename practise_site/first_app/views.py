from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def index(request):
    return HttpResponse("Страница приложения first_app.")

def categories(request):
    return HttpResponse("<h1>Статьи по категориям</h1>")