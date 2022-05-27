from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class Project(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    article = models.CharField(max_length=3000)
    image = models.ImageField(upload_to="projects/", blank=True, null=True)
    date = models.DateField('Date de mise en place du projet')

class Client(models.Model):
    fullname = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone = models.IntegerField(blank=True, null=True)
    message = models.TextField(max_length=1000)

class PageExemple(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="sites/", null=True, blank=True)
    page = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField('Date de mise en place du site', auto_created=True, auto_now_add=True)
    prix = models.IntegerField(blank=True, null=True)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['author', 'title', 'date']
    list_filter = ['author', 'title', 'date']

class ClientAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'email']
    list_filter = ['fullname', 'email']

class PageExempleAdmin(admin.ModelAdmin):
    list_display = ['name', 'page']
    list_filter = ['name', 'page']