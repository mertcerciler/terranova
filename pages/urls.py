from django.urls import path 
from  . import views

urlpatterns  = [
    path('index', views.index, name='index'),
    path('', views.index, name='index'),
    path('hizmetler/<int:hizmet_id>', views.hizmet_ayrintili, name='hizmet_ozel' ),
    path('<int:etkinlik_id>', views.etkinlik_ayrintili, name='etkinlik_ozel'),
    path('aydan-cerciler', views.aydan_cerciler, name='aydan-cerciler'),
    path('iletisim', views.iletisim, name='iletisim'),
    path('.well-known/pki-validation/', views.ssl, name='ssl'),
]