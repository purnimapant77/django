from django.shortcuts import render
from django.http import HttpResponse

def players(request):
    peoples=[
        {'name':"Purnima Pant", 'age':20, 'score':100},
        {'name':"Nidhi Pant", 'age':12, 'score':250},
        {'name':"Ananya Bhatta", 'age':10, 'score': 90},
        {'name':"Anni Pathak", 'age':22, 'score':120}
    ]
    return render(request, 'home/index.html', context={"peoples":peoples}) #when we need to send data from bakhend to template we use context