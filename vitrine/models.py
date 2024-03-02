from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

# Create your models here.

class PageExemple(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to="sites/", null=True, blank=True)
    page = models.CharField(max_length=50)
    description = models.CharField(max_length=1000, null=True, blank=True)
    date = models.DateField('Date de mise en place du site', auto_created=True, auto_now_add=True)
    prix = models.IntegerField(blank=True, null=True)

class PageExempleAdmin(admin.ModelAdmin):
    list_display = ['name', 'page']
    list_filter = ['name', 'page']