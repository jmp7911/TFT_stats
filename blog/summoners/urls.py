from django.urls import path
from django.views.generic import TemplateView
from .views import SummonerListView, SummonerMatchView

urlpatterns = [
    path('', TemplateView.as_view(template_name='summoners/index.html'), name='summoner_index'),
    path('stats/', SummonerListView.as_view(), name='summoner_stats'),
    path('stats/update/', SummonerMatchView.as_view(), name='summoner_update'),
    
] 