#from ogrenciler.views import user_login
from django.contrib.auth.models import User
from django import forms
from django.forms import fields
from django.forms.widgets import EmailInput, NumberInput, Textarea
from .models import Ogrenci
from universiteler.models import Ders
from django.forms.widgets import TextInput

class LoginForm(forms.Form):
  username = forms.CharField(label='Kullanıcı adı')
  password = forms.CharField(label='Parola', widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
  password = forms.CharField(label='Parola', widget=forms.PasswordInput(attrs={'style': 'width: 300px;','class': "form-control"}))
  password2 = forms.CharField(label='Yeniden Parola', widget=forms.PasswordInput(attrs={'style': 'width: 300px;','class': "form-control"}))
  
  class Meta:
    model = User
    fields = ('username', 'first_name', 'email')
    widgets = {
      'username': TextInput(attrs={'style': 'width: 300px;','class': "form-control"}),
      'first_name': TextInput(attrs={'style': 'width: 300px;','class': "form-control"}),
      'email': EmailInput(attrs={'style': 'width: 300px;','class': "form-control"}),
    }

  def clean_password2(self):
    cd = self.cleaned_data
    if cd['password'] != cd['password2']:
      raise forms.ValidationError('Parolalar uyuşmamaktadır.')
      return cd['password2']

class ogrenci_duzenle_form(forms.ModelForm):
  class Meta:
    model = Ogrenci
    fields = ('universite', 'bolum', 'no',)

class ogrenci_ders_ekle_form(forms.ModelForm):
  class Meta:
    model = Ders
    fields = ('kodu', 'adi', 'akts', 'icerik',)
    labels = {'kodu': 'Dersin kodu', 'adi': 'Dersin adı', 'akts': 'AKTS', 'icerik':'Dersin İçeriği'}
    widgets = {
      'kodu' : TextInput(attrs={'style': 'width: 300px;','class': "form-control"}),
      'adi' : TextInput(attrs={'style': 'width: 300px;', 'class': "form-control"}),
      'akts' : NumberInput(attrs={'style': 'width: 300px;','class': "form-control"}),
      'icerik': Textarea(attrs={'style': 'width: 300px; height=200px;','class': "form-control"}),
    }
