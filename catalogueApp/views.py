from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
# Create your views here.

def home(request):

    produit=Product.objects.all().order_by('-created_at')

    context={
        'produit':produit
    }

    return render(request,'index/index.html', context)

def accer_list(request):
    accer=Product.objects.filter(marque='ACCER').all()
    context={
        'accer':accer
    }
    return render(request,'index/accer.html',context)


def dell_list(request):
    dell = Product.objects.filter(marque='DELL').all()
    context = {
        'dell': dell
    }
    return render(request, 'index/dell.html',context)


def hp_list(request):
    hp = Product.objects.filter(marque='HP').all()
    context = {
        'hp': hp
    }
    return render(request, 'index/hp.html',context)


def lenovo_list(request):
    lenovo = Product.objects.filter(marque='LENOVO').all()
    context = {
        'lenovo': lenovo
    }
    return render(request, 'index/lenovo.html',context)


def mac_list(request):
    mac = Product.objects.filter(marque='MAC').all()
    context = {
        'mac': mac
    }
    return render(request, 'index/mac.html',context)



def addProduct(request):
    nom= request.POST.get('name',None)
    image=request.POST.get('image',None)
    categorie=request.POST.get('category')
    marque=request.POST.get('marque',None)
    prix=request.POST.get('price',None)
    detail=request.POST.get('detail',None)

    new_product=Product.objects.create(name=nom, image=image, categorie=categorie, marque=marque, price=prix, detail=detail)

    if request.method=='POST':
        new_product.save()

    if new_product:
        messages.success(request,'Nouveau produit ajouté avec succès.')


    return render(request,'ajout.html')


def detail(request,pk):
    product_detail=Product.objects.get(id=pk)
    context={
        'product_detail':product_detail
    }

    return render(request,'index/detail.html',context)

def bureautique(request):
    bureau=Product.objects.filter(categorie='Bureautique').all()
    context={
        'bureau':bureau
    }
    return render(request,'index/Bureautique.html',context)

def stockage(request):
    stock=Product.objects.filter(categorie='Stockage').all()
    context={
        'stock':stock
    }
    return render(request,'index/Stockage.html',context)

def connexion(request):
    connexion=Product.objects.filter(categorie='Connexion').all()
    context={
        'connexion':connexion
    }
    return render(request,'index/Connexion.html',context)

def electromenager(request):
    electromenager=Product.objects.filter(categorie='Electromenager').all()
    context={
        'electromenager':electromenager
    }
    return render(request,'index/Electromenager.html',context)