from django.urls import path

from . import views

urlpatterns = [
    path('', views.hizmet, name='hizmetler'),
    path('<int:hizmet_id>', views.hizmet_ayrintili, name='hizmet_ozel')
]