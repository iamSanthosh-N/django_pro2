from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return HttpResponse('<h1>Welcome to django</h1>')

def sample(request):
    return render(request,'sample.html')