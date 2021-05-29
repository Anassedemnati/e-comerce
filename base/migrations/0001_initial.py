# Generated by Django 3.2.3 on 2021-05-23 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomCat', models.CharField(max_length=100, null=True)),
                ('descriptionCat', models.TextField(blank=True, max_length=256, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Commande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('modePaiement', models.CharField(choices=[('cart', 'carte'), ('paypal', 'paypal'), ('au livraison', 'au livraison')], max_length=20)),
                ('prixTax', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('prixLivraison', models.DecimalField(decimal_places=3, default=0.0, max_digits=10)),
                ('prixTotal', models.DecimalField(decimal_places=3, max_digits=10)),
                ('dateCom', models.DateField(auto_now_add=True)),
                ('etatCom', models.CharField(choices=[('En attente', 'En attente'), ('En cours de livraison', 'En cours de livraison'), ('Livré', 'Livré')], max_length=30)),
                ('dateLivraison', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Produit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100, null=True)),
                ('image', models.CharField(max_length=256, null=True)),
                ('marque', models.CharField(max_length=100, null=True)),
                ('descriptionPro', models.TextField(blank=True, max_length=265, null=True)),
                ('prixPro', models.DecimalField(decimal_places=3, max_digits=10)),
                ('contiteStock', models.IntegerField()),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.categorie')),
            ],
        ),
        migrations.CreateModel(
            name='Utilisateur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('admin', models.BooleanField(default=False)),
                ('vendeur', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='ProduitCommande',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qte', models.IntegerField(null=True)),
                ('commande', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.commande')),
                ('produit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.produit')),
            ],
        ),
        migrations.AddField(
            model_name='produit',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.utilisateur'),
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomGam', models.CharField(max_length=100, null=True)),
                ('imageGam', models.CharField(max_length=100, null=True)),
                ('descriptionGam', models.TextField(blank=True, max_length=256, null=True)),
                ('Produit', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.produit')),
            ],
        ),
        migrations.AddField(
            model_name='commande',
            name='produit',
            field=models.ManyToManyField(through='base.ProduitCommande', to='base.Produit'),
        ),
        migrations.AddField(
            model_name='commande',
            name='utilisateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='base.utilisateur'),
        ),
        migrations.CreateModel(
            name='AdresseLivraison',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresseLiv', models.TextField(blank=True, max_length=256, null=True)),
                ('villeLiv', models.CharField(max_length=200)),
                ('codePostal', models.IntegerField()),
                ('payeLiv', models.CharField(max_length=200)),
                ('commande', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='base.commande')),
            ],
        ),
    ]