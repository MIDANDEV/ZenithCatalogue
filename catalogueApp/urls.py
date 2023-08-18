from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajout/', views.addProduct, name='addProduct'),
    path('accer/', views.accer_list, name='accer_list'),
    path('dell/', views.dell_list, name='dell_list'),
    path('hp/', views.hp_list, name='hp_list'),
    path('lenovo/', views.lenovo_list, name='lenovo_list'),
    path('mac/', views.mac_list, name='mac_list'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('Bureautique/', views.bureautique, name='bureautique'),
    path('Stockage/', views.stockage, name='stockage'),
    path('Connexion/', views.connexion, name='connexion'),
    path('Electromenager/', views.electromenager, name='electromenager'),
    path('newsletter/',views.subscribe, name='subscribe'),
    path('sendmail/', views.sendmail, name='sendmail')
]