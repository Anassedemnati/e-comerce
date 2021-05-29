# Generated by Django 3.2 on 2021-05-23 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='produit',
            old_name='nom',
            new_name='nomPro',
        ),
        migrations.AlterField(
            model_name='produit',
            name='utilisateur',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.utilisateur'),
        ),
    ]