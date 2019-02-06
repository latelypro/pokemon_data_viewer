from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import PokemonData
# Create your views here.
class IndexView(ListView):
    model = PokemonData
    template_name = 'index.html'
    context_object_name = 'pokemon_data_list'

class PokemonDataView(DetailView):
    model = PokemonData
    template_name = 'detail.html'
    context_object_name = 'pokemon_data'