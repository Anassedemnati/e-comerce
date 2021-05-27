from django.urls import path
from . import views
urlpatterns = [

    path('', views.DshbordView.as_view(), name='dashboard'),
    path('produit/', views.ProductList.as_view(), name='listProduct'),
    path('produit/create', views.ProducView.as_view(), name='ProductCreate'),
    path('produit/<str:pk>/edit', views.Produc_edit.as_view(), name='editProduct'),
    path('produit/<str:pk>/delete', views.Produc_delete.as_view(), name='deleteProduct'),
    path('commande/', views.ComandeList.as_view(), name='listCommande'),
    path('commande/<str:pk>/edit', views.Comand_edit.as_view(), name='editCommande'),
    path('commande/<str:pk>/delete', views.Comand_delete.as_view(), name='deleteCommande'),
    path('commande/create', views.ComandeView.as_view(), name='CommandeCreate'),
    path('user/', views.UtilisateurView.as_view(), name='listUtilisateur'),
    path('client/', views.ClientView.as_view(), name='listClient'),


]
