# Generated by Django 4.2.3 on 2023-08-18 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogueApp', '0003_alter_product_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.EmailField(max_length=254, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='marque',
        ),
        migrations.AlterField(
            model_name='product',
            name='categorie',
            field=models.CharField(choices=[('Ordinateur pro', 'Ordinateur pro'), ('Ordinateur gamer', 'Ordinateur gamer'), ('Fourniture Bureautique', 'Fourniture Bureautique'), ('Acessoires', 'Accesoires'), ('Electromenager', 'Electromenager')], max_length=100, null=True),
        ),
    ]
