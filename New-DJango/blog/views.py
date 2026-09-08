from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.


def welcome(request):
    return HttpResponse("Welcome to my blog")

def about(request):
    return HttpResponse("Ankit kumar, Lpu")

def post_detail(request, post_id):
    return HttpResponse(f"you are viewing post number {post_id}")

def category_post(request, post_category, post_id):
    return HttpResponse(f"Post {post_id} in Category: {post_category}")

def blog_year(request, year):
    return HttpResponse(f"Archieve for year {year}")

def search(request):
    query = request.GET.get('q')
    if query:
        return HttpResponse(f"you searched for query {query}")
    else:
        return HttpResponse("No search term provided")


def blog_home(request):
    return render(request, 'blog/home.html')

