from django.contrib import admin
from .models import *


# Register your models here.
admin.site.unregister(User)

admin.site.register(Produit)
admin.site.register(Commande)
admin.site.register(Categorie)
admin.site.register(Game)
admin.site.register(User)
admin.site.register(AdresseLivraison)
admin.site.register(ProduitCommande)
