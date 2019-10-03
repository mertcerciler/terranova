from django.db import models

class Etkinlik(models.Model):
    baslik = models.CharField(max_length=64)
    icerik = models.TextField(blank=True)
    icerik2 = models.TextField(blank=True)
    resim = models.ImageField(upload_to='')
    resim2 = models.ImageField(upload_to='', blank=True)
    tarih = models.DateTimeField(blank=True)
