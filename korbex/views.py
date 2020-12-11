from django.shortcuts import render


def home(request):
    context = {}
    return render(request, 'korbex/home.html', context)


def store(request):
    context = {}
    return render(request, 'korbex/store.html')


def service(request):
    context = {}
    return render(request, 'korbex/service.html')


def blog(request):
    context = {}
    return render(request, 'korbex/blog.html')


def contact(request):
    context = {}
    return render(request, 'korbex/contact.html')
