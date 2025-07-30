from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="blog"),
    path("post/", views.post, name="blog_post"),
    path("<str:slug_name>/", views.read_article, name="blog_read")
]
