from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.http import Http404

def hello(request):
    return HttpResponse('hello this is my first django views')

# def product_detail(request, product_id):
#     return HttpResponse(f"you are viewing product #{product_id}")

def product_description(request, product_desc):
    return HttpResponse(f"you are viewing product #{product_desc}")

def article_by_year(request, year):
    return HttpResponse(f"You are viewing request_date #{year}")

def product_detail(request, product_id):
    products = {1: "Laptop", 2: "Phone"}
    if product_id not in products:
        raise Http404("Product not found")
    return HttpResponse(products[product_id])

def name(request, name):
    return HttpResponse(f"Hello how are you..?? my name is #{name}")

