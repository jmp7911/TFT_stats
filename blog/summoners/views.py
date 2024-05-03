from django.shortcuts import render
from django.views.generic import TemplateView
from .managers import SummonerManager
# Create your views here.


class SummonerListView(TemplateView):
    template_name = 'summoners/stats.html'
    
    
    def get(self, request, *args, **kwargs):
        
        manager = SummonerManager()
        search = request.GET.get('search').split("#")
        
        tagLine = search[1]
        gameName = search[0]
        summoner = manager.get_summoner_by_account(tagLine, gameName)
        
        self.extra_context = {}
        self.extra_context['account'] = {'tagLine': tagLine, 'gameName': gameName}
        self.extra_context['summoner'] = summoner
        
        context = self.get_context_data()
        print(context)
        return self.render_to_response(context)
    