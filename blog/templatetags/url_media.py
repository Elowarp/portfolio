import re

from django import template
from Portfolio.settings.common import MEDIA_URL

register = template.Library()

@register.filter
def url_media(text, base_url):
    """
    Prends le texte d'un article et remplace les occurrences 
    de ![Mon image](media image.png) par sa réelle url 
    ![Mon Image](MEDIA_URL/articles_images/slugname/image.png)
    """
    left = "!["
    mid = "]("
    right = ")"
    regex = re.compile('{}(.*?){}media (.*?){}'.format(
        re.escape(left), re.escape(mid), re.escape(right)))

    def replace(name_src):
        name, src = name_src.group(1, 2)
        return left + name + mid + MEDIA_URL + "article_images/" +\
             base_url + "/" + src + right
    
    return re.sub(regex, replace, text)