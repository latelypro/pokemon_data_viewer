from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView
from .models import PokemonData
from statistics import mean
import decimal
# Create your views here.
class IndexView(ListView):
    model = PokemonData
    template_name = 'index.html'
    context_object_name = 'pokemon_data_list'

class PokemonDataView(DetailView):
    model = PokemonData
    template_name = 'detail.html'

    def get_context_data(self, **kwargs):
        
        hp_list = [all_stats['hp'] for all_stats in self.model.objects.values('hp')]
        atk_list = [all_stats['attack'] for all_stats in self.model.objects.values('attack')]
        def_list = [all_stats['defence'] for all_stats in self.model.objects.values('defence')]
        spd_list = [all_stats['speed'] for all_stats in self.model.objects.values('speed')]
        spatk_list = [all_stats['spAttack'] for all_stats in self.model.objects.values('spAttack')]
        spdef_list = [all_stats['spDefence'] for all_stats in self.model.objects.values('spDefence')]
        context = super().get_context_data(**kwargs)
        context['full_data'] = get_object_or_404(self.model, name=context['pokemondata'])
        context['ave_hp'] = mean(hp_list)
        context['ave_atk'] = mean(atk_list)
        context['ave_def'] = mean(def_list)
        context['ave_spd'] = mean(spd_list)
        context['ave_spatk'] = mean(spatk_list)
        context['ave_spdef'] = mean(spdef_list)
        return context