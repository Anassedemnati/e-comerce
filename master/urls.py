from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
urlpatterns = [

    path('', login_required(views.DshbordView.as_view(), login_url='loginPage'), name='dashboard'),
    path('produit/', login_required(views.ProductList.as_view(), login_url='loginPage'), name='listProduct'),
    path('produit/create', login_required(views.ProducView.as_view(), login_url='loginPage'), name='ProductCreate'),
    path('produit/<str:pk>/edit', login_required(views.Produc_edit.as_view(), login_url='loginPage'), name='editProduct'),
    path('produit/<str:pk>/delete', login_required(views.Produc_delete.as_view(), login_url='loginPage'), name='deleteProduct'),
    path('commande/', login_required(views.ComandeList.as_view(), login_url='loginPage'), name='listCommande'),
    path('commande/<str:pk>/edit', login_required(views.Comand_edit.as_view(), login_url='loginPage'), name='editCommande'),
    path('commande/<str:pk>/delete', login_required(views.Comand_delete.as_view(), login_url='loginPage'), name='deleteCommande'),
    path('commande/create', login_required(views.ComandeView.as_view(), login_url='loginPage'), name='CommandeCreate'),
    path('client/', login_required(views.Clientlist.as_view(), login_url='loginPage'), name='listClient'),
    path('client/<str:pk>/Detaille', login_required(views.ClientDetaille.as_view(), login_url='loginPage'), name='ClientDetaille'),
    path('client/<str:pk>/edit', login_required(views.Clientedit.as_view(), login_url='loginPage'), name='editClient'),
    path('client/<str:pk>/delete', login_required(views.Clientdelete.as_view(), login_url='loginPage'), name='deleteClient'),
    path('client/create', login_required(views.ClientView.as_view(), login_url='loginPage'), name='ClientCreate'),
    path('user/', login_required(views.userList.as_view(), login_url='loginPage'), name='listUtilisateur'),
    path('user/<str:pk>/Detaille', login_required(views.userDetaille.as_view(), login_url='loginPage'), name='userDetaille'),
    path('user/<str:pk>/edit', login_required(views.Clientedit.as_view(), login_url='loginPage'), name='edituser'),
    path('user/<str:pk>/delete', login_required(views.Clientdelete.as_view(), login_url='loginPage'), name='deleteuser'),
    path('user/create', login_required(views.ClientView.as_view(), login_url='loginPage'), name='userCreate'),
    path('login', views.loginPage.as_view(), name='loginPage'),
    path('logout', views.logoutUSER, name='logout'),




]
