from django.shortcuts import render, redirect
from django.views import View

from .models import *
from .forms import *
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.
class DshbordView(View):

    def get(self, request):
        commands = Commande.objects.all()
        clients = User.objects.filter(is_staff=False, is_superuser=False)
        totalCom = Commande.objects.count()
        totalLivre = Commande.objects.filter(etatCom='Livré').count()
        totalenatent = Commande.objects.filter(etatCom='En attente').count()
        context = {'clients': clients, 'totalCom': totalCom, 'totalLivre': totalLivre, 'totalenatent': totalenatent,
                   'commands': commands}
        return render(request, "admin/dashboard.html", context)


class ProductList(View):
    def get(self, request):
        products = Produit.objects.all()
        context = {'products': products}
        return render(request, "admin/listProduct.html", context)


class ProducView(View):
    def get(self, request):
        form = ProductForm()
        return render(request, "admin/Formproduit.html", {'form': form})

    def post(self, request):
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("listProduct")


class ComandeList(View):

    def get(self, request):
        Commandes = Commande.objects.all()
        context = {'Commandes': Commandes}
        return render(request, "admin/listComande.html", context)


class ComandeView(View):

    def get(self, request):
        form = ComandeForm()
        return render(request, "admin/FormComande.html", {'form': form})

    def post(self, request):
        form = ComandeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect("listCommande")


class Comand_edit(View):
    def get(self, request, pk):
        comand = get_object_or_404(Commande, id=pk)
        form = ComandeForm(instance=comand)
        return render(request, 'admin/FormComande.html', {'form': form})

    def post(self, request, pk):
        comand = get_object_or_404(Commande, id=pk)
        form = ComandeForm(request.POST, instance=comand)
        if form.is_valid():
            form.save()
            return redirect('listCommande')


class Comand_delete(View):
    def get(self, request, pk):
        comand = get_object_or_404(Commande, id=pk)
        return render(request, 'admin/deleteComande.html', {'comand': comand})

    def post(self, request, pk):
        comand = get_object_or_404(Commande, id=pk)
        comand.delete()
        return redirect('listCommande')


class userList(View):
    def get(self, request):
        sellers = User.objects.filter(is_staff=True)
        return render(request, "admin/listUser.html", {'sellers': sellers})


class Clientlist(View):
    def get(self, request):
        clients = User.objects.filter(is_staff=False, is_superuser=False)

        return render(request, "admin/listClient.html", {'clients': clients})


class Produc_edit(View):
    def get(self, request, pk):
        product = get_object_or_404(Produit, id=pk)
        form = ProductForm(instance=product)
        return render(request, 'admin/Formproduit.html', {'form': form})

    def post(self, request, pk):
        product = get_object_or_404(Produit, id=pk)
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('listProduct')


class Produc_delete(View):
    def get(self, request, pk):
        product = get_object_or_404(Produit, id=pk)
        return render(request, 'admin/deleteProduct.html', {'product': product})

    def post(self, request, pk):
        product = get_object_or_404(Produit, id=pk)
        product.delete()
        return redirect('listProduct')


class ClientDetaille(View):
    def get(self, request, pk):
        client = get_object_or_404(User, id=pk)
        commandes = client.commande_set.all()
        Totalcom = client.commande_set.count()
        context = {'client': client, 'comandes': commandes, 'Totalcom': Totalcom}

        return render(request, 'admin/ClientDetaille.html', context)


class Clientedit(View):
    def get(self, request, pk):
        client = get_object_or_404(User, id=pk)
        form = UserForm(instance=client)
        return render(request, 'admin/FormClient.html', {'form': form})

    def post(self, request, pk):
        client = get_object_or_404(User, id=pk)
        form = UserForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            if not form.instance.is_staff:
                return redirect("listClient")
            else:
                return redirect("listUtilisateur")


class Clientdelete(View):
    def get(self, request, pk):
        client = get_object_or_404(User, id=pk)
        return render(request, 'admin/deleteclient.html', {'client': client})

    def post(self, request, pk):
        client = get_object_or_404(User, id=pk)
        client.delete()
        return redirect('listClient')


class ClientView(View):
    def get(self, request):
        form = UserForm()
        return render(request, "admin/FormClient.html", {'form': form})

    def post(self, request):
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
             #data = form.cleaned_data

            # test before redirection if it is staff or not
            if not form.instance.is_staff:
                return redirect("listClient")
            else:
                return redirect("listUtilisateur")


class userDetaille(View):
    def get(self, request, pk):
        seller = get_object_or_404(User, id=pk)

        produits = seller.produit_set.all()
        TotalProd = seller.produit_set.count()
        context = {'seller': seller, 'produits': produits, 'TotalProd': TotalProd}

        return render(request, 'admin/userDetaille.html', context)
