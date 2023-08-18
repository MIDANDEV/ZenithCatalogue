from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('ajout/', views.addProduct, name='addProduct'),
    path('gamer/', views.ordigamer, name='gamer'),
    path('ordinateurpro/', views.ordipro, name='ordipro'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('Bureautique/', views.bureautique, name='bureautique'),
    path('Accessoires/', views.accesoire, name='accessoire'),
    path('Electromenager/', views.electromenager, name='electromenager'),
    path('newsletter/',views.subscribe, name='subscribe'),
    path('sendmail/', views.sendmail, name='sendmail')
]