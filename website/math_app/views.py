from django.http import HttpResponse
from django.shortcuts import render, redirect

from .models import Priklad
from .forms import ReseniForm

def index(request):
    priklady = Priklad.objects.all()
    context = {
        'priklady': priklady
    }
    return render(request, 'index.html', context=context)

def vypocet(request, priklad_id):
    priklad = Priklad.objects.all()[priklad_id]
    if request.method == "POST":
        form = ReseniForm(request.POST, priklad=priklad)
        if form.is_valid():
            reseni = form.save(commit=False)
            reseni.FK_priklad = priklad
            reseni.save()
            print(eval(priklad.priklad))
            print(reseni.reseni)
            if int(reseni.reseni) == eval(priklad.priklad):
                return redirect('/spravne')
            else: return redirect('/spatne')
    else:
        form = ReseniForm(priklad=priklad)
    return render(request, 'form.html', {'form': form, 'priklad': priklad })

def calc(request):
    return render(request, "calc.html")

def spravne(request):
    return render(request, "spravne.html")

def spatne(request):
    return render(request, "spatne.html")
