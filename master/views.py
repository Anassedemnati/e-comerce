from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .models import *
from .forms import *
from django.shortcuts import get_list_or_404, get_object_or_404


# Create your views here.
class DshbordView(View):

    def get(self, request):
        return render(request, "admin/dashboard.html", {})


class ProductList(View):
    def get(self, request):
        products =Produit.objects.all()
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


class UtilisateurView(View):
    def get(self, request):
        return render(request, "admin/listUser.html", {})


class ClientView(View):
    def get(self, request):
        return render(request, "admin/listClient.html", {})


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
