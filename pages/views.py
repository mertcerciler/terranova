from django.shortcuts import render

# Create your views here.

def index(request): 
    return render(request, 'pages/index.html')

def scio(request):
    return render(request, 'pages/scio.html')

def access_the_bars(request):
    return render(request, 'pages/access-the-bars.html')

def aile_dizilimi(request):
    return render(request, 'pages/aile-dizilimi.html')

def antar_satya_ile_aile_dizilimi(request):
    return render(request, 'pages/scio.antar-satya-ile-aile-dizilimi')

def antar_satya_ile_kadın_çemberi(request):
    return render(request, 'pages/antar-satya-ile-kadın-çemberi.html')

def asuman_kaplan_algın(request):
    return render(request, 'pages/asuman-kaplan-algın.html')

def aydan_cerciler(request):
    return render(request, 'pages/aydan-cerciler.html')

def bilinçaltı_kalıplarımız_ve_ilişkiler(request):
    return render(request, 'pages/bilinçaltı-kalıplarımız-ve-ilişkiler.html')

def bilinçaltı_kök_inançları(request):
    return render(request, 'pages/bilinçaltı-kök-inançları.html')



def bünhan_bengi(request):
    return render(request, 'pages/bünhan-bengi.html')

def bütünsel_koçluk(request):
    return render(request, 'pages/bütünsel-koçluk.html')

def çocuklar_için_yoga(request):
    return render(request, 'pages/çocuklar-için-yoga.html')

def çocuklarda_dışlanma_ve_zorbalık(request):
    return render(request, 'pages/çocuklarda-dışlanma-ve-zorbalık.html')

def eğitim_ve_öğrenci_koçluğu(request):
    return render(request, 'pages/eğitim-ve-öğrenci-koçluğu.html')

def eliff_şandan_doygun(request):
    return render(request, 'pages/elif-şandan-doygun.html')



def fatoş_berberoğlu(request):
    return render(request, 'pages/fatoş-berberoğlu.html')

def heal_your_life(request):
    return render(request, 'pages/heal-your-life.html')

def iletisim(request):
    return render(request, 'pages/iletisim.html')

def kinesiyoloji(request):
    return render(request, 'pages/kinesiyoloji.html')

def parama_çisem(request):
    return render(request, 'pages/parama-çisem.html')

def seda_bağcan(request):
    return render(request, 'pages/seda-bağcan.html')

def stres_ve_moral(request):
    return render(request, 'pages/stres-ve-moral.html')

def tiplemeler(request):
    return render(request, 'pages/tiplemeler.html')

def yazı_kampı(request):
    return render(request, 'pages/yazı-kampı.html')

def yoga_terapisi(request):
    return render(request, 'pages/yoga-terapisi.html')
