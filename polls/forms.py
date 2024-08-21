from django.forms import ModelForm
from .models import Contact,Index

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

class IndexForm(ModelForm):
    class Meta:
        model = Index
        fields = ['message']