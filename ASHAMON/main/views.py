from django.shortcuts import render
from django.http import HttpResponse
from .models import ToDoList, Item
# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get()
    return HttpResponse("<h1>%s</h1>" %ls.name)

def v1(response):
    return HttpResponse("<h1>Welcome to the ASHAMON homepage!</h1>")

