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
    path('client/', views.Clientlist.as_view(), name='listClient'),
    path('client/<str:pk>/Detaille', views.ClientDetaille.as_view(), name='ClientDetaille'),
    path('client/<str:pk>/edit', views.Clientedit.as_view(), name='editClient'),
    path('client/<str:pk>/delete', views.Clientdelete.as_view(), name='deleteClient'),
    path('client/create', views.ClientView.as_view(), name='ClientCreate'),
    path('user/', views.userList.as_view(), name='listUtilisateur'),
    path('user/<str:pk>/Detaille', views.userDetaille.as_view(), name='userDetaille'),
    path('user/<str:pk>/edit', views.Clientedit.as_view(), name='edituser'),
    path('user/<str:pk>/delete', views.Clientdelete.as_view(), name='deleteuser'),
    path('user/create', views.ClientView.as_view(), name='userCreate'),


]
