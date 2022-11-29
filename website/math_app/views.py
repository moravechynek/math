from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from django.core.paginator import Paginator

from datetime import datetime

from .models import Priklad, Reseni, Ucebnice, Kapitola, Cviceni
from .forms import ReseniForm, UcebniceForm, RegistraceForm
from .evaluate import evaluate


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

@login_required
def ucebniceEdit(request, ucebnice_id):
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
    return render(request, 'ucebnice_edit.html', context=context)

class UcebniceCreate(LoginRequiredMixin,CreateView):
    model = Ucebnice
    fields = ['nazev','obrazek','autor']
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')

class UcebniceUpdate(LoginRequiredMixin,UpdateView):
    model = Ucebnice
    fields = ['nazev',]

class UcebniceDelete(LoginRequiredMixin,DeleteView):
    model = Ucebnice
    success_url = reverse_lazy('index')

class KapitolaCreate(LoginRequiredMixin,CreateView):
    model = Kapitola
    fields = ['nazev',]
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')

class KapitolaUpdate(LoginRequiredMixin,UpdateView):
    model = Kapitola
    fields = ['nazev',]

class KapitolaDelete(LoginRequiredMixin,DeleteView):
    model = Kapitola
    success_url = reverse_lazy('index')

class CviceniCreate(LoginRequiredMixin,CreateView):
    model = Cviceni
    fields = ['text',]
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')

class CviceniUpdate(LoginRequiredMixin,UpdateView):
    model = Cviceni
    fields = ['text',]

class CviceniDelete(LoginRequiredMixin,DeleteView):
    model = Cviceni
    success_url = reverse_lazy('index')

class PrikladCreate(LoginRequiredMixin,CreateView):
    model = Priklad
    fields = ['priklad',]
    template_name_suffix = '_create'
    success_url = reverse_lazy('index')

class PrikladUpdate(LoginRequiredMixin,UpdateView):
    model = Priklad
    fields = ['priklad',]

class PrikladDelete(LoginRequiredMixin,DeleteView):
    model = Priklad
    success_url = reverse_lazy('index')

def register_request(request):
	if request.method == "POST":
		form = RegistraceForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = RegistraceForm()
	return render (request=request, template_name="registration/register.html", context={"register_form":form})

def vypocet(request, priklad_id):
    i = 1
    priklad = Priklad.objects.all()[priklad_id]
    if request.method == "POST":
        form = ReseniForm(request.POST, priklad=priklad)
        if form.is_valid():
            reseni = form.save(commit=False)
            reseni.FK_priklad = priklad
            
            if int(reseni.reseni) == eval(str(evaluate(priklad.priklad))):
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
    labels = []
    data = []

    queryset = Reseni.objects.all()
    for i in queryset:
        labels.append(i.FK_priklad.priklad)
    reseni = Reseni.objects.all()

    paginator = Paginator(reseni, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'reseni': reseni,
        'labels': labels,
        'data': data,
        'page_obj': page_obj,
    }
    return render(request, 'statistics.html', context=context)