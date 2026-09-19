from django.urls import path
from . import views

urlpatterns=[
    path('post_detail/<int:post_id>/',views.post_detail, name='post-detail'),
    path('user_detail/<str:username>/',views.user_detail, name='user-detail'),
]