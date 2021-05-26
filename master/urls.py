from django.urls import path
from . import views
urlpatterns = [

    path('', views.DshbordView.as_view(), name='dashboard'),
    path('produit/', views.ProductView.as_view(), name='listProduct'),
    path('commande/', views.ComandeView.as_view(), name='listCommande'),
    path('users/', views.UtilisateurView.as_view(), name='listUtilisateur'),


]