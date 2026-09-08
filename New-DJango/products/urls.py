from django.urls import path
from . import views
from django.urls import re_path

urlpatterns =[
    path('hello/', views.hello, name='hello'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('thing/<str:product_desc>/', views.product_description, name='product_description'),
    re_path(r'^article/(?P<year>[0-9]{4})/$', views.article_by_year, name='article_by_year'),
    
]