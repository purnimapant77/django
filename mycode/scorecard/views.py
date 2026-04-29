from django.shortcuts import render
from django.http import HttpResponse

def players(request):
    peoples=[
        {'name':"Purnima Pant", 'age':20},
        {'name':"Nidhi Pant", 'age':12},
        {'name':"Ananya Bhatta", 'age':10},
        {'name':"Anni Pathak", 'age':22}
    ]
    return render(request, 'home/index.html', context={"peoples":peoples}) #when we need to send data from bakhend to template we use context