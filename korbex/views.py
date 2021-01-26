from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.http import HttpResponseNotFound


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


# --------- SERWIS -----------
def service(request):
    error = ''
    type_repairs = TypeRepair.objects.all().order_by('type_repair')
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


def edit_type(request):
    ed = request.GET.get('id', '')
    type = TypeRepair.objects.get(id=ed)
    try:
        if request.method == 'POST':
            type.type_repair = request.POST.get('type')
            type.save()
            return redirect('service_p')
    except:
        return HttpResponseNotFound('<h1> Zapys ne znajdeno </h1>')


def delete_type(request):
    try:
        dt = request.GET.get('id', '')
        type = TypeRepair.objects.get(id=dt)
        type.delete()
        return redirect('service_p')
    except:
        error = 'Niemożliwe usunięcia tego wpisu. Najpierw usuń wszystkie naprawy,<br> ' \
                'które mają typ naprawy <strong>"{}"</strong> lub ustaw dla nich inny rodzaj naprawy'.format(type)
        return HttpResponseNotFound(error)


def new_repair(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_p')
        else:
            error = 'Nieprawidłowo wypełnione'


def edit_repair(request):
    er = request.GET.get('id', '')
    service = Service.objects.get(id=er)
    try:
        if request.method == "POST":
            type = request.POST.get('type')
            service.type_repair = TypeRepair.objects.get(type_repair=type)
            service.name_repair = request.POST.get('repair')
            service.price = request.POST.get('price')
            service.save()
            return redirect('service_p')
    except:
        return HttpResponseNotFound("<h1> Zapys ne znajdeno </h1>")


def delete_repair(request):
    try:
        dr = request.GET.get('id', '')
        repair = Service.objects.get(id=dr)
        repair.delete()
        return redirect('service_p')
    except:
        return HttpResponseNotFound("<h1> Zapys ne znajdeno </h1>")


# _______ BLOG________
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
