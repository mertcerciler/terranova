from django.urls import path

from . import views

urlpatterns = [
    path('', views.blog, name='bloglar'),
    path('<int:blog_id>', views.blog_ayrintili, name='blog_ozel')
]