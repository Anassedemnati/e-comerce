from django.db import models


# Create your models here.

class Categorie(models.Model):
    nomCat = models.CharField(max_length=100, null=True)
    descriptionCat = models.TextField(max_length=256, null=True, blank=True)

class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    admin = models.BooleanField(default=False)
    vendeur = models.BooleanField(default=False)


class Produit(models.Model):
    nom = models.CharField(max_length=100, null=True)
    image = models.CharField(max_length=256, null=True)
    marque = models.CharField(max_length=100, null=True)
    descriptionPro = models.TextField(max_length=265, null=True, blank=True)
    prixPro = models.DecimalField(max_digits=10, decimal_places=3)
    contiteStock = models.IntegerField()
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    utilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)





class Game(models.Model):
    nomGam = models.CharField(max_length=100, null=True)
    imageGam = models.CharField(max_length=100, null=True)
    descriptionGam = models.TextField(max_length=256, null=True, blank=True)
    Produit = models.ForeignKey(Produit, null=True, on_delete=models.SET_NULL)


class Commande(models.Model):
    # les mode de paiement
    modePaiement = (
        ('cart', 'carte'),
        ('paypal', 'paypal'),
        ('au livraison', 'au livraison'),
    )
    # les etat de la commande
    etatCom = (
        ('En attente', 'En attente'),
        ('En cours de livraison', 'En cours de livraison'),
        ('Livré', 'Livré'),
    )
    modePaiement = models.CharField(max_length=20, choices=modePaiement)
    prixTax = models.DecimalField(max_digits=10,decimal_places=3, default=0.0)
    prixLivraison = models.DecimalField(max_digits=10, decimal_places=3, default=0.0)
    prixTotal = models.DecimalField(max_digits=10, decimal_places=3)
    dateCom = models.DateField(auto_now_add=True)
    etatCom = models.CharField(max_length=30, choices=etatCom)
    dateLivraison = models.DateField(null=True)
    utilisateur = models.ForeignKey(Utilisateur, null=True, on_delete=models.CASCADE)
    produit = models.ManyToManyField(Produit, through='ProduitCommande')


class ProduitCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte = models.IntegerField(null=True)

class AdresseLivraison(models.Model):
    commande= models.OneToOneField(Commande, on_delete=models.CASCADE)
    adresseLiv = models.TextField(max_length=256, null=True,blank=True)
    villeLiv = models.CharField(max_length=200)
    codePostal = models.IntegerField()
    payeLiv = models.CharField(max_length=200)


