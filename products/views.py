from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


# def home(request):
#     return HttpResponse()


# def about(request):
#     return HttpResponse("About Page")


# def contact(request):
#     return HttpResponse("Contact Page")

# def hello_products(request):
#     return HttpResponse("Hello from products apps")



def home(request):
    return render(request, 'products/home.html')

def about(request):
    return render(request, 'products/about.html')



