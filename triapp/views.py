from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
import random
import smtplib
import email.message
# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def blog_dtl(request):
    return render(request, 'blog-details.html')

def contact(request):
    if request.POST:
        name = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mg = request.POST.get('msgs')
      
        
        con = Contact_details()
        con.Name = name
        con.Email = em
        con.Subject = sub
        con.message = mg
        con.save()
        return render(request, 'contact.html')
    return render(request, 'contact.html')

def services(request):
    return render(request, 'services.html')

def blog(request):
    return render(request, 'blog.html')

def carrers(request):
    return render(request, 'carrers.html')
    
    
def web_service(request):
    return render(request,'web_service.html')


def android_service(request):
    return render(request,'android_service.html')
def custom_software(request):
    return render(request,'custom_software.html')
def it_service(request):
    return render(request,'it.html')
def ui_ux_service(request):
    return render(request,'ux_ui.html')