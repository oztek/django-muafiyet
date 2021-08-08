from django.db import models
from django.utils import timezone
from universiteler.models import Universite, Bolumler, Ders

# Create your models here.
class Ogrenci(models.Model):
  user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
  universite = models.ForeignKey("universiteler.Universite", on_delete=models.CASCADE)
  bolum = models.ForeignKey('universiteler.Bolumler', on_delete=models.CASCADE)
  no = models.CharField(max_length=10)
  dersler = models.ManyToManyField(Ders, blank=True, null=True)
  sonuclandiMi = models.BooleanField(default=False)
  zaman = models.DateTimeField(default=timezone.now)

  def __str__(self):
    return self.no