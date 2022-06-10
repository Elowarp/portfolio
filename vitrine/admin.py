from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Project, ProjectAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(PageExemple, PageExempleAdmin)
admin.site.register(Article, ArticleAdmin)