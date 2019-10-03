from django.shortcuts import get_object_or_404, render
from .models import Etkinlik

def etkinlik(request):
    etkinlikler = Etkinlik.objects.all()
    kisa_icerik = []
   
    for etkinlik_element in etkinlikler:
        ch = 0
        str1 = ""
        for x in range(0,260):
            str1  = str1 + etkinlik_element.icerik[x]
        kisa_icerik.append(str1)
        ch = ch + 1
    mylist = zip(etkinlikler, kisa_icerik)
    context = {
        'etkinlikler' : etkinlikler,
        'mylist' : mylist,
    }
    return render(request, 'etkinlikler/etkinlikler.html', context)

def etkinlik_ayrintili(request, etkinlik_id):
    etkinlik1 = get_object_or_404(Etkinlik, pk= etkinlik_id)

    context = {
        'etkinlik1': etkinlik1,
    }
    return render(request, 'etkinlikler/etkinlik_ozel.html', context)