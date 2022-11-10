from django.contrib import admin

from .models import Priklad, Reseni, Ucebnice, Kapitola, Cviceni

admin.site.register(Priklad)
admin.site.register(Reseni)
admin.site.register(Ucebnice)
admin.site.register(Kapitola)
admin.site.register(Cviceni)