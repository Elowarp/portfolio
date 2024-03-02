from django.shortcuts import get_object_or_404, render

from .models import Post

# Create your views here.
def index(request):
    articles = Post.objects.order_by("-pub_date")
    context = {
        "articles": articles
    }
    return render(request, "blog/index.html", context)

def read_article(request, slug_name):
    article = get_object_or_404(Post, slug_name=slug_name)
    return render(request, "blog/read.html", {"article":article})