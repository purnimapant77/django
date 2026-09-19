from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return HttpResponse("Hello, this is shop home page.")

def about(request):
    return HttpResponse("Hello, this is shop about page.")

def products(request):
    return HttpResponse("Hello, this is shop products page.")