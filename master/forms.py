from django import forms
from django.contrib.auth.models import User
from .models import *







class ComandeForm(forms.ModelForm):
    class Meta:
        model = Commande
        fields = "__all__"


class ProductForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = "__all__"


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Categorie
        fields = "__all__"


class AdresseLivraisonForm(forms.ModelForm):
    class Meta:
        model = AdresseLivraison
        fields = "__all__"
