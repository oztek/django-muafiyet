from django.db import models
from django.utils import timezone

# Create your models here.

class Universite(models.Model):
    isim = models.CharField(max_length=100)
    kisaisim = models.CharField(max_length=20)
    zaman = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.isim

class Bolumler(models.Model):
    universite = models.ForeignKey('Universite', on_delete=models.CASCADE)
    isim = models.CharField(max_length=100)
    zaman = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.isim

class Ders(models.Model):
  adi = models.CharField(max_length=100)
  kodu = models.CharField(max_length=10)
  akts = models.PositiveSmallIntegerField()
  icerik = models.TextField()
  universite = models.ForeignKey(Universite, on_delete=models.CASCADE)
  bolum = models.ForeignKey(Bolumler, on_delete=models.CASCADE)
  muafMi = models.BooleanField(null=True)

  def __str__(self):
    return f'{self.kodu} {self.adi}'