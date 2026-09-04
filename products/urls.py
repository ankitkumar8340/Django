from django.urls import path
from . import views

urlpatterns = [
    # path('', views.hello_products, name="hello_products"),
    path('', views.home, name="home"),
    path('about/', views.about, name="about")
]
