
from django.urls import path,include
from .views import IndexView, PokemonDataView
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/detail', PokemonDataView.as_view(), name='detail')
]