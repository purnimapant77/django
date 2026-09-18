from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("hello, welcome to my blog")

def about(request):
    return HttpResponse("Hello, yhis is baout page of my blog!!!")
