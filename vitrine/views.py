from django.shortcuts import render
from .models import Project, PageExemple
from .forms import ClientForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .sendTelegram import send

# Create your views here.
def index(request):
    projects = Project.objects.all().order_by('-date')[:4]

    if request.method == "POST":
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            send("Tu as reçu une nouvelle demande sur le site bg!")
            messages.success(request, "Message envoyé !")

        else :
            messages.error(request, "Quelque chose s'est mal passé avec l'envoie :(")
            
        return redirect('/')

    return render(request, "index.html", {'projects': projects})

def projects(request):
    return render(request, "projects.html")

def mentionsLegales(request):
    return render(request, "mentionsLegales.html")

def siteExemple(request):
    if request.method == "GET":
        id = request.GET.get("id", False)
        print(id)
        if id:
            page = get_object_or_404(PageExemple, pk=id)
            return render(request, "sites/"+page.page)

    return redirect("/")