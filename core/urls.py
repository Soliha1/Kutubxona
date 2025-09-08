"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_views),
    path('',home_views),
    path('mualliflar/',muallif_views),
    path('muallif/<int:pk>/',muallif_details_views),
    path('kitoblar_haqida/',Kitoblar_views),
    path('kitoblar_haqida/<int:pk>/',Kitob_details_views),
    path('recordlar/',Recordlar_views),
    path('tirik_mualliflar/',Tirik_mualliflar_views),
    path('sahifasi_katta_kitoblar/', Sahifasi_eng_katta_kitoblar_views),
    path('kitobi_kop_mualliflar', KItobi_kop_muallif_views),
    path('oxirgi_recordlar/',Oxirgi_recordlar_views),
    path('Tiriklarning_kitoblari/',Tirik_mualliflarning_kitoblari_views),
    path('Badiy_kitoblar/',Badiy_kitoblar_views),
    path('Yoshi_katta_mualliflar/',Yoshi_kattalar_views),
    path('Kitob_soni_10_kichik/', Kitob_soni_10_tadan_kichik_views),
    path('recordlar/<int:pk>/', recordlar_details_views),

]
