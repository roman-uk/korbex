from django.shortcuts import render
from .models import *


# Start
def home(request):
    homecontent = HomeContent.objects.all()
    blogcontent = Blog.objects.all().order_by("data_add")[:5]
    context = {"homecontent": homecontent, 'blogcontent': blogcontent}
    return render(request, 'korbex/home.html', context)


# Sklep
def store(request):
    context = {}
    return render(request, 'korbex/store.html')


# Serwis
def service(request):
    context = {}
    return render(request, 'korbex/service.html')


# Blog
def blog(request):
    blog_id = request.GET.get("id", '')
    if blog_id != '':
        home_blog = Blog.objects.get(id=blog_id)
    else:
        home_blog = None
    blogcontent = Blog.objects.all().order_by("data_add")
    context = {'blogcontent': blogcontent, "home_blog": home_blog}
    return render(request, 'korbex/blog.html', context)


# Kontact
def contact(request):
    context = {}
    return render(request, 'korbex/contact.html')
