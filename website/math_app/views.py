from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

import datetime

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

    muzou_pocitat = Ucebnice.objects.prefetch_related('muzou_pocitat')

    context = {
        'ucebnice': ucebnice,
        'kapitoly': kapitoly,
        'cviceni': cviceni,
        'priklady': priklady,
        'uzivatele': muzou_pocitat
    } 
    return render(request, 'ucebnice.html', context=context)

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

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

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

def spravne(request):
    return render(request, "spravne.html")

def spatne(request):
    return render(request, "spatne.html")

class StatView(LoginRequiredMixin, ListView):
    model = Reseni 
    paginate_by = 7
    context_object_name = 'posts'
    ordering = ['-cas']

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        today = datetime.date.today()
        labels = []
        for i in range(7):
            day = (today - datetime.timedelta(days=i)).strftime("%d.%m.").split('.')
            labels.append(f'{int(day[0])}.{int(day[1])}.')
        
        data = [0,0,0,0,0,0,0]
        data_uspesnost = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
        queryset = Reseni.objects.all()
        for i in queryset:
            for j in range(7):
                if i.cas.date() == today - datetime.timedelta(days=j):
                    data[j] += 1
                    data_uspesnost[j][int(i.je_spravne)] += 1
                    """if i.je_spravne == True:
                        data_uspesnost[j][0] += 1
                        print(f'Spravne: {int(i.je_spravne)}')
                    else:
                        data_uspesnost[j][1] += 1
                        print(f'Spatne: {int(i.je_spravne)}')"""

        data_uspesnost_final = [0,0,0,0,0,0,0]
        tmp = 0
        for i in data_uspesnost:
            if(i[0] + i[1]):
                data_uspesnost_final[tmp] = i[0] / (i[0] + i[1]) * 100
            tmp += 1
        context['labels'] = labels
        context['data'] = data
        context['data_uspesnost'] = data_uspesnost_final
        return context



@login_required
def ucebnice_edit(request, ucebnice_id):
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
    return render(request, "ucebnice_edit.html", context=context)

@login_required
def ucebnice_edit_ajax(request, ucebnice_id):
    if request.method == 'POST':
        # UCEBNICE
        nazev = request.POST['nazev']
        ucebnice = Ucebnice.objects.all()[ucebnice_id]
        ucebnice.nazev = nazev
        ucebnice.save()
        # KAPITOLY
        print(request.POST)
        #for k in kapitoly: print(k)
        # RESPONSE
        successful = 'successful'
        context = {
            'successful': successful,
        }
        return JsonResponse(context)

