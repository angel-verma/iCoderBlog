from django.shortcuts import render, HttpResponse
from .models import Contact


def home(request):
    # return HttpResponse('Home Page')
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    if request.method == 'POST':
        print("We are using post method")
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        msg = request.POST['msg']
        print(name, email, phone, msg)
        contact = Contact(name=name, email=email, phone=phone, msg=msg)
        contact.save()
    return render(request, 'contact.html')


def blog(request):
    # return HttpResponse('Blog Home Page')
    return render(request, 'blog.html')


def blogPost(request, slug):
    # return HttpResponse(f'Blog Post Page {slug}')
    return render(request, 'blogPost.html')
