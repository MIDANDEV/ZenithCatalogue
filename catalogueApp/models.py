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
    name=models.CharField(max_length=100,blank=True,null=True)
    marque=models.CharField(max_length=200, choices=MARQUE_TYPE, null=True, blank=True)
    image= models.ImageField(upload_to='product_image', null=False, blank=False)
    categorie=models.CharField(max_length=100, choices=CATEGORIE_LISTE, null=True, blank=True)
    price=models.IntegerField( null=True, blank=True)
    detail=models.TextField(blank=True, null=True)
    created_at=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.name}"