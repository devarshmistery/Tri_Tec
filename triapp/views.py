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


def admin_index(request):
    return render(request,'admin.html')

def admin_message(request):
 
      
        view = Contact_details.objects.all()
        return render(request,'admin_message.html',{'data':view})


def admin_Register(request):
    if request.POST:
        fnm = request.POST['fname']
        lnm = request.POST['lname']
        em = request.POST['email']
        pass1 = request.POST['pass']
        pass2 = request.POST['re_pass']
        
        try:
            valid = admin_detail.objects.get(a_Email=em)
            return HttpResponse("<a href=''> Email Id Already Registerd </a>")
        except:
            if pass1 == pass2:
                obj = admin_detail()
                obj.a_Name = fnm
                obj.a_Email = em
                obj.a_password = pass2
                obj.save()
            else:
                return HttpResponse("<a href=''> Passwords Are Not Same </a>")
            
    return render(request,'admin_reg.html')
def admin_Login(request):
    if request.POST:
        em = request.POST['email']
        pass1 = request.POST['pass1']
        
        try:
            valid = admin_detail.objects.get(semail=em)
            if valid.password == pass1:
                request.session['admin_info'] = valid.id
                return redirect('admin_index')
            else:
                return HttpResponse("<a href=''> Wrong Password </a>")
        except:
            return HttpResponse("<a href=''> Email Id Not Found </a>")
    return render(request,'admin_login.html.html')