from django.shortcuts import render, redirect
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
    return render(request, 'korbex/store.html', context)


# Serwis
def service(request):
    error = ''
    type_repairs = TypeRepair.objects.all()
    repairs = Service.objects.all().order_by('type_repair')
    type_repairs_form = TypeRepairForm()
    repairs_form = ServiceForm()
    context = {'error': error, 'repairs': repairs, 'type_repairs': type_repairs,
               'type_repairs_form': type_repairs_form, 'repairsform': repairs_form}
    return render(request, 'korbex/service.html', context)


def new_type_repair(request):
    if request.method == "POST":
        form = TypeRepairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_p')
        else:
            error = 'Nieprawidłowo wypełnione'


def new_repair(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_p')
        else:
            error = 'Nieprawidłowo wypełnione'


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


# Kontakt
def contact(request):
    context = {}
    context['contact_data'] = ContactData.objects.all()

    context['working_hours'] = WorkingHours.objects.all()

    return render(request, 'korbex/contact.html', context)

