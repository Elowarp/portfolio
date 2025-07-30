from django.urls import include, path

from .views import index, mentionsLegales, aboutme

urlpatterns = [
    path('', index, name="index"),
    path('aboutme/', aboutme, name="aboutme"),
    path('legal/', mentionsLegales, name="legal"),
]