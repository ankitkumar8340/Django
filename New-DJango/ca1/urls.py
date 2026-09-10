from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='name'),
    # path(r"?P<product_id>[0-9]{5}/$", views.product, name='product')
    path('<str:product_id>/', views.product, name='product')

]