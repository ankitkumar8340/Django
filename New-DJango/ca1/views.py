from django.shortcuts import render
import re
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("Welcome Students")

def product(request, product_id):
    if re.fullmatch(r'\d+', product_id):
        return HttpResponse(f"this is your product id : {product_id}")
    else:
        return HttpResponse("enter a valid product id")

        

def student(request):
    return HttpResponse("Home page")

def student_profile(request, student_id):
    return HttpResponse(f"Sudent id {student_id}")

def result(request):
    return render(request, 'ca1/profile.html')






