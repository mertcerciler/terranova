from django.urls import path 
from  . import views

urlpatterns  = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('scio', views.scio, name = 'scio'),
    path('access-the-bars', views.access_the_bars, name='access-the-bars'),
    path('aile-dizilimi', views.aile_dizilimi, name='aile-dizilimi'),
    path('antar-satya-ile-aile-dizilimi', views.antar_satya_ile_aile_dizilimi, name='antar-satya-ile-aile-dizilimi'),
    path('antar-satya-ile-kadın-çemberi', views.antar_satya_ile_kadın_çemberi, name='antar-satya-ile-kadın-çemberi'),
    path('asuman-kaplan-algın', views.asuman_kaplan_algın, name='asuman-kaplan-algın'),
    path('aydan-cerciler', views.aydan_cerciler, name='aydan-cerciler'),
    path('bilinçaltı-kalıplarımız-ve-ilişkiler', views.bilinçaltı_kalıplarımız_ve_ilişkiler, name='bilinçaltı-kalıplarımız-ve-ilişkiler'),
    path('bilinçaltı-kök-inançları', views.bilinçaltı_kök_inançları, name='bilinçaltı-kök-inançları'),
    path('bünhan-bengi', views.bünhan_bengi, name='bünhan-bengi'),
    path('bütünsel-koçluk', views.bütünsel_koçluk, name='bütünsel-koçluk'),
    path('çocuklar-için-yoga', views.çocuklar_için_yoga, name='çocuklar-için-yoga'),
    path('çocuklarda-dışlanma-ve-zorbalık', views.çocuklarda_dışlanma_ve_zorbalık, name='çocuklarda-dışlanma-ve-zorbalık'),
    path('eğitim-ve-öğrenci-koçluğu', views.eğitim_ve_öğrenci_koçluğu, name='eğitim-ve-öğrenci-koçluğu'),
    path('elif-şandan-doygun', views.eliff_şandan_doygun, name='elif-şandan-doygun'),
    
    path('fatoş-berberoğlu', views.fatoş_berberoğlu, name='fatoş-berberoğlu'),
    path('heal-your-life', views.heal_your_life, name='heal-your-life'),
    path('iletisim', views.iletisim, name='iletisim'),
    path('kinesiyoloji', views.kinesiyoloji, name='kinesiyoloji'),
    path('parama-çisem', views.parama_çisem, name='parama-çisem'),
    path('seda-bağcan', views.seda_bağcan, name='seda-bağcan'),
    path('stres-ve-moral', views.stres_ve_moral, name='stres-ve-moral'),
    path('tiplemeler', views.tiplemeler, name='tiplemeler'),
    path('yazı-kampı', views.yazı_kampı, name='yazı-kampı'),
    path('yoga-terapisi', views.yoga_terapisi, name='yoga-terapisi')
]