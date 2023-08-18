from django.contrib import admin
from .models import *
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','marque','image','categorie','price','detail','created_at')


admin.site.register(Product, ProductAdmin  )

class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('mail','created_at')

admin.site.register(Newsletter,NewsletterAdmin)