from django import forms
from .models import Post, Image

class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=50, label="Titre",
                            widget=forms.TextInput(attrs={"class":"form-control"}))
    banner = forms.ImageField(label="Bannière",
                            widget=forms.FileInput(attrs={"class":"form-control"}),
                            required=False)
    text = forms.CharField(label="Article", widget=forms.Textarea(attrs={"class":"form-control"}))
 
    class Meta:
        model = Post
        fields = ('title', 'text', 'banner', )
 
 
class ImageForm(forms.ModelForm):
    image = forms.ImageField(label='Image', widget=forms.FileInput(attrs={"class":"form-control"}))    
    class Meta:
        model = Image
        fields = ('image', )