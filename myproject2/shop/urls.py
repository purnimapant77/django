from django.urls import path
from . import views

urlpatterns=[
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('products/', views.products, name='blog-products'),
]