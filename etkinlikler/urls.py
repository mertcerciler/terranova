from django.urls import path

from . import views

urlpatterns = [
    path('', views.etkinlik, name='etkinlikler'),
    path('<int:etkinlik_id>', views.etkinlik_ayrintili, name='etkinlik_ozel')
]