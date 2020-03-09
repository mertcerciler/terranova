from django.db import models
from datetime import datetime
class Blog(models.Model):
    baslik = models.CharField(max_length=64)
    icerik = models.TextField(blank=True)
    icerik2 = models.TextField(blank=True)
    resim = models.ImageField(upload_to='')
    resim2 = models.ImageField(upload_to='', blank=True)
    tarih = models.DateTimeField(blank=True, default=datetime.now)
    def __str__(self):
        return self.baslik

