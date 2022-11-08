from django.http import HttpResponse
from django.shortcuts import render

from .models import Priklad


def index(request):
    priklady = Priklad.objects.all()
    output = ', '.join([p.priklad for p in priklady])
    return HttpResponse(output)

def calc(request):
    return render(request, "calc.html")
