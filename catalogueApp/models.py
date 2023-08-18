from django.db import models

# Create your models here.






class  Product(models.Model):
    CATEGORIE_LISTE=(
        ('Ordinateur','Ordinateur'),
        ('Bureautique','Bureautique'),
        ('Stockage','Stockage'),
        ('Connexion','Connexion'),
        ('Electromenager','Electromenager')
    )
    MARQUE_TYPE = (

        ('ACCER', 'Accer'),
        ('DELL', 'DELL'),
        ('HP', ' HP'),
        ('LENOVO', 'Lenovo'),
        ('MAC', 'MAC'),
        ('Au', 'Autre')
    )
    name=models.CharField(max_length=100,blank=False, null=True)
    marque=models.CharField(max_length=200, choices=MARQUE_TYPE, blank=False, null=True)
    image= models.ImageField(upload_to='product_image/')
    categorie=models.CharField(max_length=100, choices=CATEGORIE_LISTE, blank=False, null=True)
    price=models.IntegerField(blank=False, null=True)
    detail=models.TextField(blank=False, null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"

class Newsletter(models.Model):
    mail= models.EmailField(unique=True)
    created_at= models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.mail}"