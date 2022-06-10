from .models import Project, PageExemple, Article
from .forms import ClientForm
from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from .sendTelegram import send
from django.http import Http404

# Create your views here.
def index(request):
    pages = PageExemple.objects.all().order_by("-date")
    articles = Article.objects.all().order_by("-date")

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            send("Tu as reçu une nouvelle demande sur le site bg!")
            messages.success(request, "Message envoyé !")

        else :
            messages.error(request, "Quelque chose s'est mal passé avec l'envoie :(")
            
        return redirect('/')

    return render(request, "index.html", {'pages': pages, 'articles': articles})

def articles(request):
    if request.method == "GET":
        id = request.GET.get("id", False)
        if id:
            article = get_object_or_404(Article, pk=id)
            return render(request, "articles.html", {"article": article})

        raise Http404("L'article n'existe pas.")

def mentionsLegales(request):
    return render(request, "mentionsLegales.html")

def siteExemple(request):
    if request.method == "GET":
        id = request.GET.get("id", False)
        if id:
            page = get_object_or_404(PageExemple, pk=id)
            return render(request, "sites/"+page.page)

    return redirect("/")