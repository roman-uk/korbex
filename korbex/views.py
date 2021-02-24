from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import *
from .forms import *
from django.http import HttpResponseNotFound
from django.views.generic import CreateView, UpdateView
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages


#   Login/Logout
class ServiceLogin(LoginView):
    template_name = 'korbex/login.html'
    form_class = LoginForm
    success_url = reverse_lazy('home_p')

    def get_success_url(self):
        return self.success_url


class ServiceLogout(LogoutView):
    next_page = reverse_lazy('home_p')


# Change password
class UpdatePassword(LoginRequiredMixin, PasswordChangeView):
    form_class = UpdatePasswordForm
    success_url = reverse_lazy('home_p')
    template_name = 'korbex/change-password.html'



# >>>>>>>>>>>>>>>>>>>>>> Start/ Home page <<<<<<<<<<<<<<<<<<<<<<
def home(request):
    homecontent = HomeContent.objects.all().order_by('-data_add')
    blogcontent = Blog.objects.all().order_by("-data_add")[:5]
    context = {"homecontent": homecontent, 'blogcontent': blogcontent}
    return render(request, 'korbex/home.html', context)


# Adding a new entry on the home page
class CreateHome(LoginRequiredMixin, CreateView):
    model = HomeContent
    form_class = HomeContentForm
    template_name = 'korbex/home_create.html'
    success_url = reverse_lazy('home_p')


# Updating a entry on the home page
class UpdateHome(LoginRequiredMixin, UpdateView):
    model = HomeContent
    form_class = HomeContentForm
    template_name = 'korbex/home_create.html'
    success_url = reverse_lazy('home_p')


# Deleting entry on the home page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
def home_delete(request, pk=''):
    article = HomeContent.objects.get(id=pk)
    article.image.delete()
    article.delete()
    return redirect('home_p')


#   --------------Sklep-----------------
#            product page
def store(request):
    content = StoreProducts.objects.all()
    search = request.GET.get('search', '')
    if search != '':
        content = StoreProducts.objects.filter(name_product__icontains=search)
    sort = str(request.GET.get('sort', 'name_product'))
    price_min = request.GET.get('pr_min', 0)
    if price_min == '':
        price_min = 0
    price_max = request.GET.get('pr_max', 100000)
    if price_max == '':
        price_max = 100000
    context = {}
    context['search'] = search
    context['price_min'] = price_min
    context['price_max'] = price_max
    context['products'] = content.order_by(sort).filter(price__gte=price_min, price__lte=price_max)
    return render(request, 'korbex/store.html', context)


#       one product that a visitor clicked on
def one_product(request, pk=''):
    context = {}
    product = StoreProducts.objects.get(id=pk)
    context['product'] = product
    return render(request, 'korbex/one_product.html', context)


#       adding a new product to the page
class CreateStore(LoginRequiredMixin, CreateView):
    model = StoreProducts
    form_class = StoreProductsForm
    template_name = 'korbex/store-update.html'
    success_url = '/store'


#       product editing
class UpdateStore(LoginRequiredMixin, UpdateView):
    model = StoreProducts
    form_class = StoreProductsForm
    template_name = 'korbex/store-update.html'
    success_url = '/store'


#       deleting an product
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
def store_delete(request, pk=''):
    prod = StoreProducts.objects.get(id=pk)
    prod.delete()
    return redirect('store_p')


# --------- SERWIS -----------

# render service page
def service(request):
    error = ''
    type_repairs = TypeRepair.objects.all().order_by('type_repair')
    repairs = Service.objects.all().order_by('type_repair')
    type_repairs_form = TypeRepairForm()
    repairs_form = ServiceForm()
    context = {'error': error, 'repairs': repairs, 'type_repairs': type_repairs,
               'type_repairs_form': type_repairs_form, 'repairsform': repairs_form}
    return render(request, 'korbex/service.html', context)


# Adding a new type repair on the service page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
def new_type_repair(request):
    if request.method == "POST":
        form = TypeRepairForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_p')
        else:
            error = 'Nieprawidłowo wypełnione'


# Updating type repair on the service page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
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

# Deleting type repair on the service page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
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


# Adding a new repair on the service page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
def new_repair(request):
    if request.method == "POST":
        form = ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('service_p')
        else:
            error = 'Nieprawidłowo wypełnione'


# Updating repair on the service page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
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


# Deleting record on the service page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
def delete_repair(request):
    try:
        dr = request.GET.get('id', '')
        repair = Service.objects.get(id=dr)
        repair.delete()
        return redirect('service_p')
    except:
        return HttpResponseNotFound("<h1> Zapys ne znajdeno </h1>")


# _______ BLOG________
# render Blog page
def blog(request):
    blog_id = request.GET.get("id", '')
    if blog_id != '':
        home_blog = Blog.objects.get(id=blog_id)
    else:
        home_blog = None
    blogcontent = Blog.objects.all().order_by("-data_add")
    context = {'blogcontent': blogcontent, "home_blog": home_blog}
    return render(request, 'korbex/blog.html', context)


#  Adding a new record on the blog page
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    form_class = BlogForm
    template_name = 'korbex/blog-create.html'
    success_url = '/blog'


#  Updating the record on the blog page
class UpdateBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'korbex/blog-create.html'
    success_url = '/blog'


#  Deleting the record on the blog page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
def blog_delete(request, pk=''):
    art = Blog.objects.get(id=pk)
    art.image.delete()  # or:  pip install django-cleanup / INSTALLED_APPS = ('django_cleanup',)
    art.delete()
    return redirect('blog_p')


# Kontakt
# render Contact page
def contact(request):
    context = {}
    context['contact_data'] = ContactData.objects.all()
    context['working_hours'] = WorkingHours.objects.all().order_by('working_day')
    return render(request, 'korbex/contact.html', context)


#  Adding a new contact(address, telephone, facebook) on the contact page
class CreateDataContact(LoginRequiredMixin, CreateView):
    model = ContactData
    form_class = ContactDataForm
    template_name = 'korbex/contact-update.html'
    success_url = '/contact'


#  Adding a new work day(and hour) on the contact page
class CreateDayContact(LoginRequiredMixin, CreateView):
    model = WorkingHours
    form_class = WorkingHoursForm
    template_name = 'korbex/contact-update.html'
    success_url = '/contact'


#  Updating the contact(address, telephone, facebook) on the contact page
class UpdateDataContact(LoginRequiredMixin, UpdateView):
    model = ContactData
    form_class = ContactDataForm
    template_name = 'korbex/contact-update.html'
    success_url = '/contact'


#  Updating the work day on the contact page
class UpdateDayContact(LoginRequiredMixin, UpdateView):
    model = WorkingHours
    form_class = WorkingHoursForm
    template_name = 'korbex/contact-update.html'
    success_url = '/contact'


#  Deleting the record on the contact page
@login_required(login_url=reverse_lazy('login_p'))  # Verifying user authorization
def contact_delete(request, mod='', pu=''):
    if mod == 'data':
        cont = ContactData.objects.get(id=pu)
    else:
        cont = WorkingHours.objects.get(id=pu)
    cont.delete()
    return redirect('contact_p')
