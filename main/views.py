from django.shortcuts import render

from django.http import HttpResponse
from .models import *

def hello_views(request):
    return HttpResponse("hello world from django")

def home_views(request):
    return render(request, 'home.html')


def muallif_views(request):
    mualliflar=Muallif.objects.all()
    context={
        'mualliflar':mualliflar,
    }
    return render(request,'students.html',context)

def muallif_details_views(request, pk):
    muallif=Muallif.objects.get(id=pk)
    context={
        'muallif':muallif,
    }
    return render(request, 'muallifs_details.html',context)

def Kitoblar_views(request):
    kitoblar=Kitob.objects.all()
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'Kitoblar.html', context)


def Kitob_details_views(request, pk):
    kitob = Kitob.objects.get(id=pk)
    context = {
        'kitob': kitob,
    }
    return render(request, 'kitob_details.html',context)


def Recordlar_views(request):
    records=Record.objects.all()
    context={
        'records':records,
    }
    return render(request, 'records.html', context)


def Tirik_mualliflar_views(request):
    tiriklar=Muallif.objects.filter(tirik=True)
    context = {
        'tiriklar': tiriklar,
    }
    return render(request, 'tirik_mualliflar.html', context)


def Sahifasi_eng_katta_kitoblar_views(request):
    kitoblar=Kitob.objects.order_by('-sahifa')[:3]
    context = {
        'kitoblar': kitoblar,
    }
    return render(request, 'sahifa_kitoblar.html', context)

def KItobi_kop_muallif_views(request):
    mualliflar = Muallif.objects.order_by('-kitob_soni')[:3]
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'kitobi_kop_muallif.html', context)

def Oxirgi_recordlar_views(request):
    recordlar=Record.objects.order_by('-olingan_sana')[:3]
    context={
        'recordlar':recordlar,
    }
    return render(request, 'Oxirgi_recordlar.html', context)

def  Tirik_mualliflarning_kitoblari_views(request):
    kitoblar=Kitob.objects.filter(muallif__tirik=True)
    context = {
        'kitoblar': kitoblar,
    }
    return render(request, 'Tirik_mualliflarning_kitoblari.html', context)

def Badiy_kitoblar_views(request):
    Badiy_klar=Kitob.objects.filter(janr='badiy')
    context={
        'Badiy_klar': Badiy_klar,
    }
    return render(request, 'Badiy_kitoblar.html', context)

def Yoshi_kattalar_views(request):
    Yoshi_kattalar=Muallif.objects.order_by('tugilgan_sana')[:3]
    context = {

        'Yoshi_kattalar': Yoshi_kattalar,
    }
    return render(request, 'Yoshi_kattalar.html', context)

def Kitob_soni_10_tadan_kichik_views(request):
    KItobi_soni = Kitob.objects.filter(muallif__kitob_soni__lte=10)
    context = {

        'KItobi_soni': KItobi_soni,
    }
    return render(request, 'Kitob_soni.html', context)


def recordlar_details_views(request, pk):
    recordlar=Record.objects.filter(id=pk)
    context={
        'recordlar':recordlar,
    }
    return render(request, 'recordlar_details.html', context)
