from django.shortcuts import render
from .models import *


def home(request):
    homecontent = HomeContent.objects.all()
    blogcontent = Blog.objects.all()[:5]
    context = {"homecontent": homecontent, 'blogcontent': blogcontent}
    return render(request, 'korbex/home.html', context)


def store(request):
    context = {}
    return render(request, 'korbex/store.html')


def service(request):
    context = {}
    return render(request, 'korbex/service.html')


def blog(request):
    blogcontent = Blog.objects.all().order_by("data_add")
    context = {'blogcontent': blogcontent}
    return render(request, 'korbex/blog.html', context)


def contact(request):
    context = {}
    return render(request, 'korbex/contact.html')
