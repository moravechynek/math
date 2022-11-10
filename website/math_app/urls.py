from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calc, name='calc'),
    path('spravne/', views.spravne, name='spravne'),
    path('spatne/', views.spatne, name='spatne'),
    path('statistiky/', views.statistics, name='statistics'),
    path('ucebnice/<int:ucebnice_id>/', views.ucebnice, name='ucebnice'),
    path('priklad/<int:priklad_id>/', views.vypocet, name='vypocet'),
]