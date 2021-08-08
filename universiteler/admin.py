from django.contrib import admin
from .models import Ders, Universite, Bolumler

# Register your models here.
admin.site.register(Universite)
admin.site.register(Bolumler)
admin.site.register(Ders)
