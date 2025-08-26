from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Bem-vindo à API Bookstore 🚀")
# Create your views here.
