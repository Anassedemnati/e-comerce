from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Categorie(models.Model):
    nomCat = models.CharField(max_length=100, null=True)
    descriptionCat = models.TextField(max_length=256, null=True, blank=True)

    def __str__(self):
        return self.nomCat


"""
class Utilisateur(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=200)
    password = models.CharField(max_length=200)
    admin = models.BooleanField(default=False)
    vendeur = models.BooleanField(default=False)

    def __str__(self):
        return self.nom + " " + self.prenom

"""


class Produit(models.Model):
    nomPro = models.CharField(max_length=100, null=True)
    image = models.ImageField(upload_to="images/")
    marque = models.CharField(max_length=100, null=True)
    descriptionPro = models.TextField(max_length=265, null=True, blank=True)
    prixPro = models.DecimalField(max_digits=7, decimal_places=2)
    contiteStock = models.IntegerField()
    categorie = models.ForeignKey(
        Categorie, null=True, on_delete=models.SET_NULL)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.nomPro




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
    prixTax = models.DecimalField(max_digits=7, decimal_places=2, default=0.0)
    prixLivraison = models.DecimalField(
        max_digits=7, decimal_places=2, default=0.0)
    prixTotal = models.DecimalField(max_digits=7, decimal_places=2)
    dateCom = models.DateField(auto_now_add=True)
    etatCom = models.CharField(max_length=30, choices=etatCom)
    dateLivraison = models.DateField(null=True)
    categorie = models.ForeignKey(Categorie, null=True, on_delete=models.SET_NULL)
    utilisateur = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    produit = models.ManyToManyField(Produit, through='ProduitCommande')

    def __str__(self):
        return str(self.id) + "_" + str(self.utilisateur_id)


class ProduitCommande(models.Model):
    commande = models.ForeignKey(Commande, on_delete=models.CASCADE)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    qte = models.IntegerField(null=True)


class AdresseLivraison(models.Model):
    commande = models.OneToOneField(Commande, on_delete=models.CASCADE)
    adresseLiv = models.TextField(max_length=256, null=True, blank=True)
    villeLiv = models.CharField(max_length=200)
    codePostal = models.IntegerField()
    payeLiv = models.CharField(max_length=200)

    def __str__(self):
        return str(self.commande_id)+"_"+self.villeLiv+"_"+self.payeLiv
