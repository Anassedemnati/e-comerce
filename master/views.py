from django.shortcuts import render
from django.views import View


# Create your views here.
class DshbordView(View):
    def get(self, request):
        return render(request, "admin/dashboard.html", {})


class ProductView(View):
    def get(self, request):
        return render(request, "admin/listProduct.html", {})


class ComandeView(View):
    def get(self, request):
        return render(request, "admin/listComande.html", {})


class UtilisateurView(View):
    def get(self, request):
        return render(request, "admin/listUsebr.html", {})


class ClientView(View):
    def get(self, request):
        return render(request, "admin/listClient.html", {})
