from django.urls import path
from triapp.views import *

urlpatterns = [
    path('',                index,      name='index'),
    path('blog/',           blog,       name='blog'),
    path('blog-details/',   blog_dtl,   name='blog_dtl'),
    path('contact/',        contact,    name='contact'),
    path('services/',       services,   name='services'),
    path('about/',          about,      name='about'),
    path('carrers/',        carrers,      name='carrers'),
    path('web_service/',web_service,name='web_service'),
    path('android_service/',android_service,name='android_service'),
    path('custom_software/',custom_software,name='custom_software'),
    path('it_service/',it_service,name='it_service'),
    path('ui_ux_service/',ui_ux_service,name='ui_ux_service'),
    
]