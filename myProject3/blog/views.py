from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def post_detail(request,post_id):
    return HttpResponse(f"<h3>your id is {post_id}")

def user_detail(request, username):
    return HttpResponse(f"<h3>your username is {username}")