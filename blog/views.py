from django.shortcuts import get_object_or_404, render
from django.forms import modelformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.template.defaultfilters import slugify
from django.utils.timezone import make_aware

import datetime

from .forms import ImageForm, PostForm
from .models import Image, Post

# Create your views here.
def index(request):
    articles = Post.objects.order_by("-pub_date")
    context = {
        "articles": articles,
        "page": "blog"
    }
    return render(request, "blog/index.html", context)

def read_article(request, slug_name):
    article = get_object_or_404(Post, slug_name=slug_name)
    article.view_count += 1
    article.save()
    return render(request, "blog/read.html", {"article":article})

@login_required(login_url="/")
def post(request):
    # Extra = nombre de photos maximum qu'on peut upload
    ImageFormSet = modelformset_factory(Image,
                                        form=ImageForm, extra=6)
    
    if request.method == 'POST':
        postForm = PostForm(request.POST, request.FILES)
        formset = ImageFormSet(request.POST, request.FILES,
                               queryset=Image.objects.none())
    
    
        if postForm.is_valid() and formset.is_valid():
            post_form = postForm.save(commit=False)
            post_form.author = request.user

            slug = slugify(post_form.title)
            post_form.slug_name = slug

            time = make_aware(datetime.datetime.now())
            post_form.pub_date = time
            post_form.save()
    
            # Sauvegarde des images en supplément
            for form in formset.cleaned_data:
                if form:
                    image = form['image']
                    photo = Image(post=post_form, image=image)
                    photo.save()

            messages.success(request,"L'article a été posté !")
            return HttpResponseRedirect("/blog/%s" % slug)
        else:
            print(postForm.errors, formset.errors)
    else:
        postForm = PostForm()
        formset = ImageFormSet(queryset=Image.objects.none())
        
    return render(request, 'blog/post.html',
                  {'postForm': postForm, 'formset': formset})