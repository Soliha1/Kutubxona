from django.shortcuts import render, redirect, get_object_or_404

from django.http import HttpResponse
from django.template.context_processors import request

from core.muallif_qoshish import MuallifForm
from .models import *

def hello_views(request):
    return HttpResponse("hello world from django")

def home_views(request):
    return render(request, 'home.html')


def muallif_views(request):
    mualliflar=Muallif.objects.all()
    search = request.GET.get('search')
    if search:
        mualliflar = Muallif.objects.filter(ism__contains=search)
    context={
        'mualliflar':mualliflar,
    }
    return render(request,'mualliflar.html',context)

def muallif_details_views(request, pk):
    muallif=Muallif.objects.get(id=pk)
    context={
        'muallif':muallif,
    }
    return render(request, 'muallifs_details.html',context)

def Kitoblar_views(request):
    if request.method== 'POST':
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=get_object_or_404(Muallif, id=request.POST.get('muallif_id')),
        )
        return redirect('/kitoblar/')

    kitoblar=Kitob.objects.all()
    mualliflar=Muallif.objects.all()

    context = {
        'kitoblar': kitoblar,
        'mualliflar':mualliflar,

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
    search = request.GET.get('search')
    if search:
        records=Record.objects.filter(talaba__ism__contains=search)
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


def recordlar_search_views(request, pk):
    recordlar=Record.objects.filter(id=pk)
    context={
        'recordlar':recordlar,
    }
    return render(request, 'recordlar_details.html', context)

def Muallif_delete_views(request, pk):
    mualliflar=get_object_or_404(Muallif, pk=pk)
    mualliflar.delete()
    return redirect('/mualliflar/')

def recordlar_delete_views(request, pk):
    recordlar = get_object_or_404(Record, pk=pk)
    recordlar.delete()
    return redirect('/recordlar/')


def Talabalar_views(request):
    if request.method=='POST':
        Talaba.objects.create(
            ism=request.POST.get('ism'),
            guruh=request.POST.get('guruh'),
            kurs=request.POST.get('kurs'),
            kitob_soni=request.POST.get('kitob_soni'),
        )
        Talabalar=Talaba.objects.all()
        context={
            'Talabalar':Talabalar,
        }

        return redirect('/talabalar/')
    return render(request, 'Talabalar.html')


def Muallif_update_views(request, pk):
    author=get_object_or_404(Muallif, id=pk)
    if request.method=='POST':
        author.ism=request.POST.get('ism')
        author.jins=request.POST.get('jins')
        author.tugilgan_sana=request.POST.get('tugilgan_sana')
        author.kitob_soni=request.POST.get('kitob_soni')
        author.save()

        return redirect('/muallif/')
    context={
        'author':author,
    }
    return render(request, 'student-update.html', context)



def Mualif_qoshshish_views(request):
    authors=Muallif.objects.all()
    if request.method == 'POST':
        form = MuallifForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')

    context = {
        'authors': authors,
        'form': form,
    }
    return render(request, 'authors.html', context)
