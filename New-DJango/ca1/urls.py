from django.urls import path
from . import views

urlpatterns=[
    path('home/', views.home, name='name'),
    # path(r"?P<product_id>[0-9]{5}/$", views.product, name='product')
    path('<str:product_id>/', views.product, name='product')

    path('student/', views.student, name='student'),
    path('student/<int:std_id>/', views.student_profile, name='studentprofile'),
    path('student/result/', views.result, name='result'),
    

]