from django.contrib import auth
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, login
from .models import Ogrenci
from universiteler.models import Bolumler, Universite, Ders
from .forms import LoginForm, UserRegistrationForm, ogrenci_ders_ekle_form, ogrenci_duzenle_form

# Create your views here.

def index(request, uniid):
  bolumler = Bolumler.objects.filter(universite__exact=uniid).order_by('isim')
  return render(request, '', {'bolumler': bolumler})

def ogrenci_bos(request):
  return render(request, 'ogrenciler/bos.html', {})

def ogrenci_listele(request):
  kullanici = request.user
  if kullanici.is_authenticated:
    if kullanici.is_superuser:
      ogrenciler = Ogrenci.objects.order_by('no')
      return render(request, 'ogrenciler/ogrenci_listele.html', {'ogrenciler': ogrenciler})
    else:
      return redirect('ogrenci_goster')
  return redirect('ogrenci_bos')
  
def ogrenci_ders_ekle(request, pk):
  ogrenci = get_object_or_404(Ogrenci, pk=pk)
  if request.method == 'POST':
    ders_ekle_form = ogrenci_ders_ekle_form(request.POST)
    if ders_ekle_form.is_valid():
      ders = ders_ekle_form.save(commit=False)
      ders.universite = ogrenci.universite
      ders.bolum = ogrenci.bolum
      ders.save()
      ogrenci.dersler.add(ders)
      return redirect('ogrenci_goster')
  else:
    ders_ekle_form = ogrenci_ders_ekle_form
  return render(request, 'ogrenciler/ogrenci_ders_ekle.html', {'ders_ekle_form': ders_ekle_form})

def ogrenci_duzenle(request, pk):
  ogrenci = get_object_or_404(Ogrenci, pk=pk)
  if request.method == 'POST':
    ogrenci_form = ogrenci_duzenle_form(request.POST)
    print(ogrenci_form)
  else:
    ogrenci_form = ogrenci_duzenle()
    return render(request, 'ogrenciler/ogrenci_duzenle.html', {'ogrenci_form': ogrenci_form})

def ogrenci_goster(request):
  user = request.user
  if Ogrenci.objects.all().filter(user_id = user.pk).count()>0:
    ogrenci = get_object_or_404(Ogrenci, user_id=user.pk)
    #print(ogrenci.dersler.all())
    dersler = ogrenci.dersler.all().order_by('adi')
    return render(request, 'ogrenciler/ogrenci_goster.html', {'ogrenci': ogrenci, 'dersler' : dersler})
  else:
    return redirect('ogrenci_yeni')

def ogrenci_ayrinti(request, pk):
  kullanici = request.user
  if kullanici.is_superuser:
    ogrenci = get_object_or_404(Ogrenci, pk=pk)
    dersler = ogrenci.dersler.all().order_by('adi')
    return render(request, 'ogrenciler/ogrenci_goster.html', {'ogrenci': ogrenci, 'dersler' : dersler})    
  else:
    return redirect('ogrenci_goster')  

def ogrenci_yeni(request):
  if request.method == 'POST':
    form = ogrenci_duzenle_form(request.POST)
    if form.is_valid():
      ogrenci = form.save(commit=False)
      ogrenci.user = request.user
      ogrenci.zaman = timezone.now()
      ogrenci.save()
  else:
    form = ogrenci_duzenle_form()
  return render(request, 'ogrenciler/ogrenci_yeni.html', {'ogrenci_form': form})

def register(request):
  if request.method == 'POST':
    user_form = UserRegistrationForm(request.POST)
    if user_form.is_valid():
      #Create new user
      new_user = user_form.save(commit=False)
      new_user.set_password(user_form.cleaned_data['password'])
      new_user.save()
      return render(request,'registration/register_done.html', {'new_user': new_user})
  else:
    user_form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'user_form': user_form})


def user_login(request):
  if request.method == 'POST':
    form = LoginForm(request.POST)
    if form.is_valid():
      cd = form.cleaned_data
      user = authenticate(request, username=cd['username'], password=cd['password'])
      if user is not None:
        if user.is_active:
          login(request, user)
          return redirect('/')
          #return HttpResponse('Giris Başarılı')
        else:
          return HttpResponse('Pasif hesap')
      else:
        #return HttpResponse('Geçersiz Giriş')
        return redirect('register')
  else:
    form = LoginForm()
    return render(request, 'registration/login.html', {'form': form})