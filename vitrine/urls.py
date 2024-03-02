from django.urls import include, path

from .views import index, mentionsLegales, siteExemple

urlpatterns = [
    path('', index, name="index"),
    path('legal/', mentionsLegales, name="legal"),
    path('sites/', siteExemple),
]