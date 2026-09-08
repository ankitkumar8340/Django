from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def greet(request):
    query = request.GET.get('q')
    if query:
        return HttpResponse(f"Hello, {query}!")
    else:
        return HttpResponse("Hello, Stranger")

def calc(request):
    query1 = request.GET.get('a')
    quuery2 = request.GET.get('b')

    if (query1 & query2):
        return HttpResponse(f" Sum = {query1 + query2}")