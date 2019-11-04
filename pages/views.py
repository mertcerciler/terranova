from django.shortcuts import render, get_object_or_404
from hizmetler.models import Hizmet

# Create your views here.

def index(request): 
    hizmetler = Hizmet.objects.all()
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
        'mylist' : mylist,
    }
    return render(request, 'pages/index.html', context)
def hizmet_ayrintili(request, hizmet_id):
    hizmet1 = get_object_or_404(Hizmet, pk= hizmet_id)

    context = {
        'hizmet1': hizmet1,
    }
    return render(request, 'hizmetler/hizmet_ozel.html', context)
    
def aydan_cerciler(request):
    return render(request, 'pages/aydan-cerciler.html')


def iletisim(request):
    return render(request, 'pages/iletisim.html')
