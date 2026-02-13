from django.contrib import admin

from .models import Post, PostAdmin, Image

# Register your models here.
admin.site.register(Post, PostAdmin)
admin.site.register(Image)