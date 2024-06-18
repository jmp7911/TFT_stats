import json
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView
from .managers import SummonerManager
# Create your views here.


class SummonerListView(TemplateView):
    template_name = 'summoners/stats.html'
    
    
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search').split("#")
        
        tagLine = search[1]
        gameName = search[0]
        manager = SummonerManager()
        summoner = manager.get_summoner_by_account(tagLine, gameName)
        
        self.extra_context = {}
        self.extra_context['account'] = {'tagLine': tagLine, 'gameName': gameName}
        self.extra_context['summoner'] = summoner
        
        context = self.get_context_data()
        
        
        return self.render_to_response(context)

class SummonerMatchView(View):
    def post(self, *args, **kwargs):
        body = json.loads(self.request.body)
        puuid = body["puuid"]
        manager = SummonerManager()
        ids = manager.get_match_ids(puuid)
        print(ids)
        return HttpResponse("Success")