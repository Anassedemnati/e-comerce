# Generated by Django 3.2 on 2021-05-29 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_commande_categorie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
