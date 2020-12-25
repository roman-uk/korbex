from django.urls import path, re_path
from korbex import views


urlpatterns = [
    path('', views.home, name='home_p'),
    path('home', views.home, name='home_p'),
    path('store', views.store, name='store_p'),
    path('service', views.service, name='service_p'),
    path('blog/int:id', views.blog, name='blog_p'),
    path('contact', views.contact, name='contact_p'),
]
