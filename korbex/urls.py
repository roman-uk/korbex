from django.urls import path, re_path
from korbex import views


urlpatterns = [

    path('', views.home, name='home_p'),
    path('home', views.home, name='home_p'),
    path('home/create', views.CreateHome.as_view(), name='home_create'),
    path('home/update/<int:pk>', views.UpdateHome.as_view(), name='home_update'),
    path('home/delete/<int:pk>', views.home_delete, name='home_delete'),
    path('store', views.store, name='store_p'),
    path('store/one<int:pk>', views.one_product, name='one_product'),
    path('store/create', views.CreateStore.as_view(), name='store_create'),
    path('store/update<int:pk>', views.UpdateStore.as_view(), name='store_update'),
    path('store/delete<int:pk>', views.store_delete, name='store_delete'),
    path('service', views.service, name='service_p'),
    path('service/new_type', views.new_type_repair, name='new_type'),
    path('service/new_repair', views.new_repair, name='new_repair'),
    path('service/edit_repair', views.edit_repair, name='edit_repair'),
    path('service/edit_type', views.edit_type, name='edit_type'),
    path('service/delete_repair', views.delete_repair, name='delete_repair'),
    path('service/delete_type', views.delete_type, name='delete_type'),
    path('blog', views.blog, name='blog_p'),
    path('blog/create', views.CreateBlog.as_view(), name='blog_create'),
    path('blog/update/<int:pk>', views.UpdateBlog.as_view(), name='blog_update'),
    path('blog/delete/<int:pk>', views.blog_delete, name='blog_delete'),
    path('contact', views.contact, name='contact_p'),
    path('contact/create-data', views.CreateDataContact.as_view(), name='contact-data_create'),
    path('contact/create-day', views.CreateDayContact.as_view(), name='contact-day_create'),
    path('contact/update-data<int:pk>', views.UpdateDataContact.as_view(), name='contact-data_update'),
    path('contact/update-day<int:pk>', views.UpdateDayContact.as_view(), name='contact-day_update'),
    path('contact/delete<mod>/<int:pu>', views.contact_delete, name='contact-delete'),
    path('login', views.ServiceLogin.as_view(), name='login_p'),
    path('logout', views.ServiceLogout.as_view(), name='logout_p'),
    path('change-password', views.UpdatePassword.as_view(), name='change_password')
]
