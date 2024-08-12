from django.shortcuts import render
from django.core.paginator import Paginator
from animeflv import AnimeFLV
from django import forms
from django.http import Http404

api = AnimeFLV()
# Create your views here.
def index(request):
    client = AnimeFLV()
    animes = client.get_latest_episodes
    animesEstrenos = client.get_latest_animes
    print(animes)

    return render(request, "Sugoi/index.html", {
        'animes': animes,
        'estrenos': animesEstrenos,
        'form': SearchFrom()
    })

def search(request):
    if request.method == "GET":
        form = SearchFrom(request.GET)
        
        if form.is_valid():
            searchquery = form.cleaned_data["name"]
            searchAnime = api.search(searchquery)

    return render(request, "Sugoi/search.html", {
        "animeSearch": searchAnime,
        "form": SearchFrom()
    })

def directorio(request):
    directorioAnime = api.get_all_animes
    

    return render(request, "Sugoi/directorio.html", {
        "directorio": directorioAnime,
        "form": SearchFrom()
    })

def anime(request, id):
    infoAnime = api.get_anime_info(id)

    return render(request, "Sugoi/animeinfo.html", {
        "infoAnime": infoAnime,
        "form": SearchFrom()
    })

def episodio(request, anime, episodio):
    episodioSeleccionado = api.get_links(anime, episodio)
    servidores = api.get_video_servers(anime, episodio)


    return render(request, "Sugoi/verepisodio.html", {
        "episodio": episodioSeleccionado,
        "servidores": servidores[0],
        "form": SearchFrom()
    })


class SearchFrom(forms.Form):
    name = forms.CharField(label= "", widget= forms.TextInput(
        attrs={'type': 'search','placeholder': 'Buscar animes...', 'class': 'form-control'}
    ))