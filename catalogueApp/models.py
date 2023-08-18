from django.db import models

# Create your models here.






class  Product(models.Model):
    CATEGORIE_LISTE=(
        ('Ordinateur pro','Ordinateur pro'),
        ('Ordinateur gamer', 'Ordinateur gamer'),
        ('Fourniture Bureautique','Fourniture Bureautique'),
        ('Acessoires','Accesoires'),
        ('Electromenager','Electromenager')
    )

    name=models.CharField(max_length=100,blank=False, null=True)
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