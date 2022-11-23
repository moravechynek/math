from django.urls import path

from . import views
import frontend.views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calc, name='calc'),
    path('spravne/', views.spravne, name='spravne'),
    path('spatne/', views.spatne, name='spatne'),
    path('statistiky/', views.statistics, name='statistics'),
    path('ucebnice/<int:ucebnice_id>/', views.ucebnice, name='ucebnice'),
    path('priklad/<int:priklad_id>/', views.vypocet, name='vypocet'),
    path('react/', frontend.views.index, name='react'),
    path('ucebnice/create/', views.UcebniceCreate.as_view(), name='ucebnice-create'),
]