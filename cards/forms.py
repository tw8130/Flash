from django import forms
from .models import FlashCards, Category
from django.forms import CharField

class FlashCreationForm(forms.ModelForm):
    class Meta:
        model=FlashCards

        exclude=['user']

        # fields=['title', 'notes', 'category']

class DeckCreateForm(forms.Form):
    name = CharField(label='Deck Name', max_length=124)

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')