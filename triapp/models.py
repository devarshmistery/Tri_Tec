from django.db import models

# Create your models here.
class Contact_details(models.Model):
    Name = models.CharField(default = "",max_length=100)
    Email = models.EmailField(default = "",max_length=100)
    Subject = models.CharField(default="", max_length=10)
    message = models.CharField(default="",max_length=550)
   
    
    def __str__(self):
        return self.Name

class admin_detail(models.Model):
    a_Name = models.CharField(default = "",max_length=100)
    a_Email = models.EmailField(default = "",max_length=100)
    a_password = models.CharField(default="",max_length=100,blank=True,null=True)
    def __str__(self):
        return self.a_Name

