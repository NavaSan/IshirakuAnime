from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('search/', views.search, name="search"),
    path('directorio/', views.directorio, name="directorio"),
    path('<str:id>', views.anime, name="anime"),
    path('ver/<str:anime>/<str:episodio>', views.episodio, name="episodio")
]