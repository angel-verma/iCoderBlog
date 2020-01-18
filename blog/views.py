from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'index.html')


def about(request):
    return HttpResponse('about Page')


def contact(request):
    return HttpResponse('Contact Page')


def blog(request):
    return HttpResponse('Blog Home Page')


def blogPost(request, slug):
    return HttpResponse(f'Blog Post Page {slug}')
