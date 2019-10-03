from django.db import models

class yararli_bilgi(models.Model):
    baslik = models.CharField(max_length=64)
    icerik = models.TextField(blank=True)
    resim = models.ImageField(upload_to='yararli_bilgiler/')
