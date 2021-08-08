from django import forms
from django.forms import fields, widgets, TextInput
from .models import Universite, Bolumler

class UniversiteForm(forms.ModelForm):
  class Meta:
    model = Universite
    fields = ('isim', 'kisaisim',)

class BolumForm(forms.ModelForm):
  class Meta:
    model = Bolumler
    fields = ('isim',)
    labels = {'isim': 'Bölüm'}
    #widgets = { 'isim' : TextInput(attrs={'label_tag': 'Bölüm', 'placeholder' : 'Bölüm'})}
