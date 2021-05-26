from django.urls import path
from . import views
urlpatterns = [

    path('', views.DshbordView.as_view(), name='dashboard'),


]