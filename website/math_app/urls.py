from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calc/', views.calc, name='calc'),
    path('spravne/', views.spravne, name='spravne'),
    path('spatne/', views.spatne, name='spatne'),
]