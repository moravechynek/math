from django.http import HttpResponse

from .models import Priklad


def index(request):
    priklady = Priklad.objects.all()
    output = ', '.join([p.priklad for p in priklady])
    return HttpResponse(output)
