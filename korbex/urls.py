from django.urls import path, re_path
from korbex import views


urlpatterns = [
    path('', views.home, name='home_p'),
    path('home/create', views.CreateHome.as_view(), name='home_create'),
    path('home/update/<int:pk>', views.UpdateHome.as_view(), name='home_update'),
    path('home/delete/<int:pk>', views.home_delete, name='home_delete'),
    path('home', views.home, name='home_p'),
    path('store', views.store, name='store_p'),
    path('service/new_type', views.new_type_repair, name='new_type'),
    path('service/new_repair', views.new_repair, name='new_repair'),
    path('service/edit_repair', views.edit_repair, name='edit_repair'),
    path('service/edit_type', views.edit_type, name='edit_type'),
    path('service/delete_repair', views.delete_repair, name='delete_repair'),
    path('service/delete_type', views.delete_type, name='delete_type'),
    path('service', views.service, name='service_p'),
    path('blog', views.blog, name='blog_p'),
    path('contact', views.contact, name='contact_p'),
]
