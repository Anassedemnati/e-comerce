from django.shortcuts import render
from django.views import View


# Create your views here.
class DshbordView(View):
    def get(self, request):
        return render(request, "admin/dashboard.html", {})
