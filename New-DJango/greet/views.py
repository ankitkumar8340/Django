from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def greet(request):
    name = request.GET.get('name')
    if name:
        return HttpResponse(f"Hello, {name}!")
    else:
        return HttpResponse("Hello, Stranger")

def calc(request):
    query1 = request.GET.get('a')
    query2 = request.GET.get('b')

    if query1 and query2:
        query1 = int(query1)
        query2 = int(query2)
        return HttpResponse(f" Sum = {query1 + query2}")
    else:
        return HttpResponse(" a or b is missing")

def sort_products(request):
    products = ['Laptop', 'Monitor', 'Keyboard', 'pc', 'Mouse']
    order = request.GET.get('order', 'asc')

    if order == 'asc':
        products =sorted(products)
    else:
        products= sorted(products, reverse=True)

    context ={
        'products':products,
        'order':order
    }
    return render(request, 'greet/product.html', context)
