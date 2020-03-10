from django.shortcuts import render, get_object_or_404
from hizmetler.models import Hizmet
from etkinlikler.models import Etkinlik

# Create your views here.

def index(request): 
    hizmetler = Hizmet.objects.all()
    etkinlikler = Etkinlik.objects.all()
    kisa_icerik = []
   
    for hizmet_element in hizmetler:
        ch = 0
        str1 = ""
        for x in range(0,260):
            str1  = str1 + hizmet_element.icerik1[x]
        kisa_icerik.append(str1)
        ch = ch + 1
    mylist = zip(hizmetler, kisa_icerik)
    context = {
        'hizmetler' : hizmetler,
        'etkinlikler' : etkinlikler,
        'mylist' : mylist,
    }
    return render(request, 'pages/index.html', context)
def hizmet_ayrintili(request, hizmet_id):
    hizmet1 = get_object_or_404(Hizmet, pk= hizmet_id)

    context = {
        'hizmet1': hizmet1,
    }
    return render(request, 'hizmetler/hizmet_ozel.html', context)

def etkinlik_ayrintili(request, etkinlik_id):
    etkinlik1 = get_object_or_404(Etkinlik, pk= etkinlik_id)

    context = {
        'etkinlik1': etkinlik1,
    }
    return render(request, 'etkinlikler/etkinlik_ozel.html', context)

def aydan_cerciler(request):
    return render(request, 'pages/aydan-cerciler.html')

def iletisim(request):
    return render(request, 'pages/iletisim.html')

def ssl(request):
    return render(request, 'pages/.well-known/pki-validation/BF8F702CAEBE3A19AD0CE7F89CEC5A27.txt')
