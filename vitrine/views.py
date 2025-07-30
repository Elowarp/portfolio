from .models import PageExemple
from blog.models import Post
from django.shortcuts import redirect, get_object_or_404, render
from django.http import Http404

# Create your views here.
def index(request):
    pages = PageExemple.objects.all().order_by("-date")
    articles = Post.objects.order_by("-pub_date").filter(is_visible=True)[:4]

    return render(request, "index.html", {'pages': pages, 'articles': articles})

def aboutme(request):
    return render(request, "aboutme.html")

def mentionsLegales(request):
    return render(request, "mentionsLegales.html")