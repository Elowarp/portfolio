from blog.models import Post
from django.shortcuts import redirect, get_object_or_404, render
from django.http import Http404

# Create your views here.
def index(request):
    articles = Post.objects.order_by("-pub_date").filter(is_visible=True)[:4]

    return render(request, "index.html", 
        {'articles': articles, "page": "index"})

def aboutme(request):
    return render(request, "aboutme.html", {"page": "aboutme"})

def mentionsLegales(request):
    return render(request, "mentionsLegales.html")