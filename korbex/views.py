from django.shortcuts import render
from .models import *
from .forms import *


# Start
def home(request):
    homecontent = HomeContent.objects.all()
    blogcontent = Blog.objects.all().order_by("data_add")[:5]
    context = {"homecontent": homecontent, 'blogcontent': blogcontent}
    return render(request, 'korbex/home.html', context)


# Sklep
def store(request):
    context = {}
    context['sort_form'] = SortedForm()
    context['prices_form'] = PriceMinMax()
    context['search_form'] = SearchForm()
    context['products'] = StoreProducts.objects.all()
    # sort_name = request.GET.get('name', '')
    return render(request, 'korbex/store.html', context)


# Serwis
def service(request):
    repairs = Service.objects.all().order_by('type_repair')
    type_repairs = TypeRepair.objects.all()
    context = {'repairs': repairs, 'type_repairs': type_repairs}
    return render(request, 'korbex/service.html', context)


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
