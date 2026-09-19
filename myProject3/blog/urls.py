from django.urls import path, re_path
from . import views

urlpatterns=[
    path('post_detail/<int:post_id>/',views.post_detail, name='post-detail'),
    path('user_detail/<str:username>/',views.user_detail, name='user-detail'),
    path('article_date/<int:year>/<int:month>/<int:day>/',views.article_date, name='article-date'), #multiple parameters using path
    re_path(r'^article_by_years/(?P<year>[0-9]{4})/$',views.article_by_years, name='article-by-year'), #repath
    #mulriple argumants using kwargs
    path('birthday/<int:year>/<int:month>/',views.Birthday, name='birthday'), #multiple parameters using path
]