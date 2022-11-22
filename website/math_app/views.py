from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Priklad, Reseni, Ucebnice, Kapitola, Cviceni
from .forms import ReseniForm


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
    context = {
        'ucebnice': ucebnice
    } 
    return render(request, 'ucebnice.html', context=context)

def vypocet(request, priklad_id):
    i = 1
    priklad = Priklad.objects.all()[priklad_id]
    if request.method == "POST":
        form = ReseniForm(request.POST, priklad=priklad)
        if form.is_valid():
            reseni = form.save(commit=False)
            reseni.FK_priklad = priklad

            pyVyraz = priklad.priklad
            while i <= priklad.priklad.count('|'):
                if i % 2 == 0:
                    pyVyraz = pyVyraz.replace('|',')',1)
                elif i % 2 == 1:
                    pyVyraz = pyVyraz.replace('|','abs(',1)
                i += 1

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