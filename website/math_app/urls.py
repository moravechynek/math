from django.urls import path

from . import views
#import frontend.views

urlpatterns = [
    path('', views.index, name='index'),
    path('spravne/', views.spravne, name='spravne'),
    path('spatne/', views.spatne, name='spatne'),
    path('ucebnice/<int:ucebnice_id>/', views.ucebnice, name='ucebnice'),
    path('priklad/<int:priklad_id>/', views.vypocet, name='vypocet'),
    path('register/', views.register_request, name='register'),

    path('ucebnice/<int:ucebnice_id>/editace/', views.ucebnice_edit, name='ucebnice-editace'),
    path('ucebnice/<int:ucebnice_id>/editace/ajax', views.ucebnice_edit_ajax, name='ucebnice-editace-ajax'),

    path('ucebnice/create/', views.UcebniceCreate.as_view(), name='ucebnice-create'),
    path('ucebnice/<int:pk>/update/', views.UcebniceUpdate.as_view(), name='ucebnice-update'),
    path('ucebnice/<int:pk>/delete/', views.UcebniceDelete.as_view(), name='ucebnice-delete'),

    path('statistiky/', views.StatView.as_view(), name='statistics'),

    path('vyhledavani', views.vyhledavani, name='vyhledavani'),
]