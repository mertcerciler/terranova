from django.db import models

class takvim_icerik(models.Model):
    baslangic_zamani = models.CharField(max_length=5)
    bitis_zamani = models.CharField(max_length=5)
    icerik = models.CharField(max_length=100)
    tarih = models.DateTimeField()
