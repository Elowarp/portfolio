from django.forms import ModelForm
from vitrine.models import Client

class ClientForm(ModelForm):
    class Meta:
        model = Client
        fields = ['fullname', 'email', 'phone', 'message']