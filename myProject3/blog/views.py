from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def post_detail(request,post_id):
    return HttpResponse(f"<h3>your id is {post_id}</h3>")

def user_detail(request, username):
    return HttpResponse(f"<h3>your username is {username}</h3>")

def article_date(request, year, month, day):
    return HttpResponse(f"<h3>your date is {year}-{month}-{day}</h3>")

def article_by_years(request, year):
    return HttpResponse(f"<h3>Articles from {year}</h3>")

def Birthday(request, **kwargs):
    return HttpResponse(f"<h3>your birth date is {kwargs} </h3>")