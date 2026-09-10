from . import views
from django.urls import path
from django.urls import re_path


urlpatterns =[
    path('blog/', views.greet, name='greet'),
    path('calc/', views.calc, name='calc'),
    path('products/', views.sort_products, name='sort_product'),
]


