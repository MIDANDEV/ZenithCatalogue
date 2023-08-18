from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.core.mail import send_mail
# Create your views here.

def home(request):

    produit=Product.objects.all().order_by('-created_at')[:6]


    context={
        'produit':produit
    }

    return render(request,'index/index.html', context)

def ordipro(request):
    ordipro=Product.objects.filter(categorie='Ordinateur pro').all()
    context={
        'ordipro':ordipro
    }
    return render(request, 'index/ordipro.html', context)


def ordigamer(request):
    gamer = Product.objects.filter(categorie='Ordinateur gamer').all()
    context = {
        'gamer': gamer
    }
    return render(request, 'index/gamer.html', context)



def addProduct(request):
    if request.method == 'POST':
        nom= request.POST.get('name',None)
        image=request.FILES.get('image',None)
        categorie=request.POST.get('category')
        prix=request.POST.get('price',None)
        detail=request.POST.get('detail',None)

        if categorie:
            new_product=Product.objects.create(name=nom, image=image, categorie=categorie, price=prix, detail=detail)
            new_product.save()


        return redirect('addProduct')


    return render(request,'ajout.html')


def detail(request,pk):
    product_detail=Product.objects.get(id=pk)
    context={
        'product_detail':product_detail
    }

    return render(request,'index/detail.html',context)

def bureautique(request):
    bureau=Product.objects.filter(categorie='Fourniture Bureautique').all()
    context={
        'bureau':bureau
    }
    return render(request,'index/Bureautique.html',context)

def accesoire(request):
    accesoire=Product.objects.filter(categorie='Accessoires').all()
    context={
        'accessoire':accesoire
    }
    return render(request, 'index/accessoire.html', context)



def electromenager(request):
    electromenager=Product.objects.filter(categorie='Electromenager').all()
    context={
        'electromenager':electromenager
    }
    return render(request,'index/Electromenager.html',context)

def subscribe(request):
    if request.method=='POST':
        email=request.POST.get('email')
        if email:
            newmail= Newsletter.objects.create(email=email)
            newmail.save()
            return redirect('home')

    return render(request, 'base.html')

def sendmail(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        objet=request.POST.get('subject')
        content=request.POST.get('message')

        data={
            'name':name,
            'email':email,
            'objet':objet,
            'content':content
        }

        message= '''
            Nouveau message:{}
            De:{}
        '''.format(data['content'], data['email'])


        send_mail(data['objet'], message,data['email'], ['burkinazenith@gmail.com'])
        messages.success('Message envoyé avec succès !')
    return render(request, 'base.html')