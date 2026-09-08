from . import views
from django.urls import path
from django.urls import re_path

urlpatterns = [
    path('welcome/', views.welcome, name='welcome'),
    path('about/', views.about, name='about'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    path('post/<str:post_category>/<int:post_id>/', views.category_post, name='category_post'),
    path('search/', views.search, name='search'),
    re_path(r'(?P<year>[0-9]{4})/$', views.blog_year, name='blog_year'),
    path('', views.blog_home, name='blog_home'),

    

]



