from django.db import models
from django.contrib.auth.models import User

def upload_banner(instance, filename):
    slug = instance.slug_name
    return "article_images/%s/%s" % (slug, filename)


class Post(models.Model):
    title = models.CharField(max_length=50)
    slug_name = models.SlugField(primary_key=True)                   # Url assignée à l'article
    text = models.TextField()
    banner = models.ImageField(upload_to=upload_banner, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    last_modified_date = models.DateTimeField("date last modified", 
                                              auto_now=True)
    
    def __str__(self):
        return self.slug_name
    
def get_image_filename(instance, filename):
    slug = instance.post.slug_name
    return "article_images/%s/%s" % (slug, filename)

class Image(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=get_image_filename, verbose_name="Image")