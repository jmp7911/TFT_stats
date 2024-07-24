import requests
import os
from .models import SummonerDto, MetadataDto, InfoDto, ParticipantDto, TraitDto, UnitDto, ItemDto, CompanionDto, MatchDto
from time import sleep

SUMMONER_URL='https://kr.api.riotgames.com/tft/summoner/v1/summoners/'
ACCOUNT_URL='https://asia.api.riotgames.com/riot/account/v1/accounts/by-riot-id/'
MATCH_URL='https://asia.api.riotgames.com/tft/match/v1/matches/'
LEAGUE_URL='https://kr.api.riotgames.com/tft/league/v1/entries/'
class SummonerManager:
    '''
    소환사 정보를 가져오는 클래스
    '''
    summoner_url = SUMMONER_URL
    account_url = ACCOUNT_URL
    match_url = MATCH_URL
    league_url = LEAGUE_URL
    season_startTime = {"11" : 1710892800}
    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['X-Riot-Token'] = os.environ.get('RIOT_API_KEY')
    summoner = None
    '''
    decorator
    ========================================================
    '''
    # puuid를 이용해 소환사 정보를 가져오는 함수에 사용
    def get_summoner(func):
        def wrapper(*args, **kwargs):
            summoner = func(*args, **kwargs)
            manager = args[0]
            puuid = summoner["puuid"]
            response = requests.get(f"{manager.summoner_url}by-puuid/{puuid}", headers=manager.headers)
            if response.status_code != 200:
                raise Exception("Failed to get a summoner.", response.json())
            manager.summoner = response.json()
            return SummonerDto.objects.update_or_create(
                account_id = manager.summoner["accountId"],
                defaults={
                    'puuid' : manager.summoner["puuid"],
                    'summoner_id' : manager.summoner["id"],
                    'summonerLevel' : manager.summoner["summonerLevel"],
                    'profileIconId' : manager.summoner["profileIconId"],
                    'revisionDate' : manager.summoner["revisionDate"],    
                }
            )[0]
        return wrapper
    
    # 전적 갱신 함수
    def update_match(func):
        def wrapper(*args, **kwargs):
            match_ids = func(*args, **kwargs)
            
            manager = args[0]
            summoner = manager.summoner
            
            for match_id in match_ids:
                row = MetadataDto.objects.filter(match_id=match_id).count()
                if row > 0:
                    continue
                    
                response = requests.get(f"{manager.match_url}{match_id}", headers=manager.headers)
                if response.status_code != 200:
                    raise Exception("Failed to get a match info.", response.json())
                match = response.json()
                metadata = match["metadata"]
                info = match["info"]
                MatchDto.objects.create(
                    metadata=MetadataDto.objects.create(metadata),
                    info=InfoDto.objects.create(info),
                )
                participants = info["participants"]
                for participant in participants:
                    companion = participant["companion"]
                    gold_left = participant["gold_left"]
                    last_round = participant["last_round"]
                    level = participant["level"]
                    placement = participant["placement"]
                    players_eliminated = participant["players_eliminated"]
                    puuid = participant["puuid"]
                    time_eliminated = participant["time_eliminated"]
                    total_damage_to_players = participant["total_damage_to_players"]
                    traits = participant["traits"]
                    units = participant["units"]
                    for trait in traits:
                        TraitDto.objects.update_or_create(
                            name = trait["name"],
                            defaults={
                                'num_units' : trait["num_units"],
                                'style' : trait["style"],
                                'tier_current' : trait["tier_current"],
                                'tier_total' : trait["tier_total"],
                            }
                        )
                    for unit in units:
                        items = unit["items"]
                        character_id = unit["character_id"]
                        chosen = unit["chosen"]
                        name = unit["name"]
                        rarity = unit["rarity"]
                        tier = unit["tier"]
                        for item in items:
                            ItemDto.objects.update_or_create(
                                name = item["name"],
                                defaults={
                                    'num_units' : item["num_units"],
                                    'style' : item["style"],
                                    'tier' : item["tier"],
                                }
                            )
                        UnitDto.objects.update_or_create(
                            character_id = character_id,
                            defaults={
                                'items' : items,
                                'chosen' : chosen,
                                'name' : name,
                                'rarity' : rarity,
                                'tier' : tier,
                            }
                        )
                    return ParticipantDto.objects.update_or_create(
                        puuid = puuid,
                        defaults={
                            'companion' : companion,
                            'gold_left' : gold_left,
                            'last_round' : last_round,
                            'level' : level,
                            'placement' : placement,
                            'players_eliminated' : players_eliminated,
                            'time_eliminated' : time_eliminated,
                            'total_damage_to_players' : total_damage_to_players,
                        }
                    )
        return wrapper
        
    '''
    decorator
    ========================================================
    function
    '''
    # 소환사 이름으로 소환사 정보를 가져오는 함수 (deprecated)
    def get_summoner_name(self, name):
        response = requests.get(f"{self.summoner_url}by-name/{name}", headers=self.headers)
        if response.status_code != 200:
            raise Exception("Failed to get a summoner.", response.json())
        return response.json()

    # gameName과 tagLine으로 소환사 정보를 가져오는 함수
    @get_summoner
    def get_summoner_by_account(self, tagLine, gameName):
        response = requests.get(f"{self.account_url}{gameName}/{tagLine}", headers=self.headers)
        if response.status_code != 200:
            if response.status_code == 404:
                return response.json()
            else:
                raise Exception("Failed to get a summoner.", response.json())
        return response.json()
    
    # 소환사의 match_id 를 가져오는 함수
    @update_match
    def get_match_ids(self, puuid):
        total_match_ids = []
        for i in range(0, 2**31-1, 100):
            response = requests.get(f"{self.match_url}by-puuid/{puuid}/ids", headers=self.headers, params={"start" : i, "count" : 100, "startTime": self.season_startTime["11"]})
            match_ids = response.json()
            
            if response.status_code != 200:
                raise Exception("Failed to get a match ids.", response.json())
            elif match_ids == []:
                break
            total_match_ids += match_ids
        return total_match_ids
    
    # 소환사의 리그 정보를 가져오는 함수
    def get_league(self):
        if self.summoner is None:
            raise Exception("Summoner is not set.")
        summoner_id = self.summoner["id"]
        response = requests.get(f"{self.league_url}by-summoner/{summoner_id}", headers=self.headers)
        if response.status_code != 200:
            raise Exception("Failed to get a league.", response.json())
        return response.json()

