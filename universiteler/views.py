from django.shortcuts import get_object_or_404, render, redirect
from django.utils import timezone
from .models import Universite, Bolumler
from .forms import UniversiteForm, BolumForm
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def universite_duzenle(request, pk):
    universite = get_object_or_404(Universite, pk=pk)
    if request.method == "POST":
        form = UniversiteForm(request.POST, instance=universite)
        
        if form.is_valid():
            universite = form.save(commit=False)
            universite.user = request.user
            universite.zaman = timezone.now()
            universite.save()
            return redirect('universite_goster', pk=universite.pk)
    else:
        form = UniversiteForm(instance=universite)
    return render(request,'universiteler/universite_yeni.html', {'form': form})

@login_required
def universite_goster(request, pk):
    universite = get_object_or_404(Universite, pk=pk)
    if request.method == 'POST':
        form = BolumForm(request.POST)
        #ßprint(form.isim)
        if form.is_valid():
            # Eğer bölüm yoksa
            #print(Bolumler.objects.filter(universite_id=pk).filter(isim=form).count())
            #print(form.fields['isim'].values())
            #print(Bolumler.objects.filter(isim=form.fields['isim'].value))
            #print(form)
            bolum = form.save(commit=False)
            if Bolumler.objects.filter(universite_id=pk).filter(isim=bolum).count() == 0:
                bolum.universite = universite
                bolum.user = request.user
                bolum.zaman = timezone.now()
                bolum.save()
            return redirect('universite_goster', pk=pk)
    else:
        form = BolumForm()
    #bolumler = Bolumler.objects.get(universite__exact=pk)
    bolumler = Bolumler.objects.filter(universite__exact=pk).order_by('isim')
    
    return render(request, 'universiteler/universite_goster.html', {'universite': universite, 'bolumler': bolumler, 'form': form})

@login_required
def universite_listele(request):
    universiteler = Universite.objects.order_by('isim')
    return render(request, 'universiteler/universite_listele.html', {'universiteler': universiteler})

@login_required
def universite_yeni(request):
    if request.method == "POST":
        form = UniversiteForm(request.POST)
        if form.is_valid():
            universite = form.save(commit=False)
            universite.user = request.user
            universite.zaman = timezone.now()
            universite.save()
            return redirect('universite_goster', pk=universite.pk)
    else:
        form = UniversiteForm()
    return render(request,'universiteler/universite_yeni.html', {'form': form})
