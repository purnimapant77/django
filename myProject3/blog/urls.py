from django.urls import path, re_path
from . import views

urlpatterns=[
    path('post_detail/<int:post_id>/',views.post_detail, name='post-detail'),
    path('user_detail/<str:username>/',views.user_detail, name='user-detail'),
    re_path(r'^article_by_years/(?P<year>[0-9]{4})/$',views.article_by_years, name='article-by-year'),
]