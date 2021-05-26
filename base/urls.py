from django.urls import path
from . import views

urlpatterns = [

    path('', views.HomeView.as_view(), name='home'),
    path('gestion/', views.BoardView.as_view(), name='board')

]
