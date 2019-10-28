from django.db import models

class Hizmet(models.Model):
    baslik = models.CharField(max_length=64)
    icerik1 = models.TextField(blank=True, )
    icerik2 = models.TextField(blank=True)
    resim = models.ImageField(upload_to='')
    resim2 = models.ImageField(upload_to='', blank=True)

