from .models import PageExemple
from blog.models import Post
from django.shortcuts import redirect, get_object_or_404, render
from django.http import Http404

# Create your views here.
def index(request):
    pages = PageExemple.objects.all().order_by("-date")
    articles = Post.objects.order_by("-pub_date")

    return render(request, "index.html", {'pages': pages, 'articles': articles})

def mentionsLegales(request):
    return render(request, "mentionsLegales.html")

def siteExemple(request):
    if request.method == "GET":
        id = request.GET.get("id", False)
        if id:
            page = get_object_or_404(PageExemple, pk=id)
            return render(request, "sites/"+page.page)

    return redirect("/")