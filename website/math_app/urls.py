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
    path('register/', views.register_request, name='register'),

    path('ucebnice/<int:ucebnice_id>/editace/', views.ucebniceEdit, name='ucebnice-editace'),
    path('ucebnice/create/', views.UcebniceCreate.as_view(), name='ucebnice-create'),
    path('ucebnice/<int:pk>/update/', views.UcebniceUpdate.as_view(), name='ucebnice-update'),
    path('ucebnice/<int:pk>/delete/', views.UcebniceDelete.as_view(), name='ucebnice-delete'),
    path('kapitola/create/', views.KapitolaCreate.as_view(), name='kapitola-create'),
    path('kapitola/<int:pk>/update/', views.KapitolaUpdate.as_view(), name='kapitola-update'),
    path('kapitola/<int:pk>/delete/', views.KapitolaDelete.as_view(), name='kapitola-delete'),
    path('cviceni/create/', views.CviceniCreate.as_view(), name='cviceni-create'),
    path('cviceni/<int:pk>/update/', views.CviceniUpdate.as_view(), name='cviceni-update'),
    path('cviceni/<int:pk>/delete/', views.CviceniDelete.as_view(), name='cviceni-delete'),
    path('priklad/create/', views.PrikladCreate.as_view(), name='priklad-create'),
    path('priklad/<int:pk>/update/', views.PrikladUpdate.as_view(), name='priklad-update'),
    path('priklad/<int:pk>/delete/', views.PrikladDelete.as_view(), name='priklad-delete'),
]