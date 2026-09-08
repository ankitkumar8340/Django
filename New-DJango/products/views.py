from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def hello(request):
    return HttpResponse('hello this is my first django views')

def product_detail(request, product_id):
    return HttpResponse(f"you are viewing product #{product_id}")

def product_description(request, product_desc):
    return HttpResponse(f"you are viewing product #{product_desc}")

def article_by_year(request, year):
    return HttpResponse(f"You are viewing request_date #{year}")



