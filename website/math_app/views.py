from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Priklad, Reseni, Ucebnice, Kapitola, Cviceni
from .forms import ReseniForm, UcebniceForm


"""
from django.contrib.auth.decorators import login_required

@login_required
"""

def index(request):
    ucebnice = Ucebnice.objects.all()
    context = {
        'ucebnice': ucebnice
    } 
    return render(request, 'index.html', context=context)

def ucebnice(request, ucebnice_id):
    ucebnice = Ucebnice.objects.all()[ucebnice_id]
    kapitoly = Kapitola.objects.filter(FK_ucebnice_id=ucebnice_id + 1)
    cviceni = []
    priklady = []
    for k in kapitoly:
        cviceni += Cviceni.objects.filter(FK_kapitola=k)
    for c in cviceni:
        priklady += Priklad.objects.filter(FK_cviceni=c)

    context = {
        'ucebnice': ucebnice,
        'kapitoly': kapitoly,
        'cviceni': cviceni,
        'priklady': priklady
    } 
    return render(request, 'ucebnice.html', context=context)

def ucebniceCreate(request):
    if request.method == "POST":
        form = UcebniceForm(request.POST, priklad=priklad)
        if form.is_valid():
            ucebnice = form.save(commit=False)
            reseni.FK_priklad = priklad
            return redirect('/spatne')
    else:
        form = ReseniForm(priklad=priklad)
    return render(request, 'form.html', {'form': form, 'priklad': priklad })

class UcebniceCreate(CreateView):
    model = Ucebnice
    fields = ['nazev',]
    template_name_suffix = '-create'
    success_url = reverse_lazy('index')

def vypocet(request, priklad_id):
    i = 1
    priklad = Priklad.objects.all()[priklad_id]
    if request.method == "POST":
        form = ReseniForm(request.POST, priklad=priklad)
        if form.is_valid():
            reseni = form.save(commit=False)
            reseni.FK_priklad = priklad

            pyVyraz = priklad.priklad
            if pyVyraz.find('|'):
                while i <= priklad.priklad.count('|'):
                    if i % 2 == 0:
                        pyVyraz = pyVyraz.replace('|',')',1)
                    elif i % 2 == 1:
                        pyVyraz = pyVyraz.replace('|','abs(',1)
                    i += 1
            i = 0

            jmenovatel = ''
            citatel = ''
            position = priklad.priklad.find('\\frac{')
            if position != -1:
                while priklad.priklad[position + len('\\frac{') + i] != '}':
                    jmenovatel += priklad.priklad[position + len('\\frac{')]
                    i += 1
                i = 0
                while priklad.priklad[position + len('\\frac{' + jmenovatel + '}{') + i] != '}':
                    citatel += priklad.priklad[position + len('\\frac{')]
                    i += 1
                i = 0
                print(f'Oldvyraz: {pyVyraz}')
                pyVyraz = pyVyraz.replace('\\frac{' + jmenovatel + '}{' + citatel + '}',str(int(jmenovatel)/int(citatel)))
            
            if int(reseni.reseni) == eval(str(pyVyraz)):
                reseni.je_spravne = True
                reseni.save()
                return redirect('/spravne')
            else:
                reseni.je_spravne = False
                reseni.save()
                return redirect('/spatne')
    else:
        form = ReseniForm(priklad=priklad)
    return render(request, 'form.html', {'form': form, 'priklad': priklad })

def calc(request):
    return render(request, "calc.html")

def spravne(request):
    return render(request, "spravne.html")

def spatne(request):
    return render(request, "spatne.html")

def statistics(request):
    return render(request, "statistics.html")