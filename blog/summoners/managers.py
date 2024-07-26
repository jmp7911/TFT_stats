import requests
import os
from .models import SummonerDto, MetadataDto, InfoDto, ParticipantDto, TraitDto, UnitDto, CompanionDto, MatchDto, ItemDto
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
            # 100 requests every 2 minutes
            # 20 requests every 1 second
            cnt = 0
            for match_id in match_ids:
                row = MetadataDto.objects.filter(match_id=match_id).count()
                if row > 0:
                    continue
                cnt += 1
                while True:
                    response = requests.get(f"{manager.match_url}{match_id}", headers=manager.headers)
                    if response.status_code == 429 and response.json()["status"]["message"] == "Rate limit exceeded":
                        if cnt % 20 == 0:
                            sleep(1)
                        if cnt % 100 == 0:
                            sleep(120)
                            cnt = 0
                    elif response.status_code == 200:
                        break
                    else:
                        raise Exception("Failed to get a match.", response.json())                    
                match = response.json()
                metadata = match["metadata"]
                metaObj = MetadataDto.objects.update_or_create(
                    match_id = metadata["match_id"],
                    defaults={
                        'data_version' : metadata["data_version"],
                    }
                )[0]
                metaObj.set_participants(metadata["participants"])
                info = match["info"]
                participants = info["participants"]
                info.pop("participants")
                infoObj = InfoDto.objects.update_or_create(
                    game_datetime = info["game_datetime"],
                    defaults={
                        'gameId' : info["gameId"],
                        'mapId' : info["mapId"],
                        'game_length' : info["game_length"],
                        'gameCreation' : info["gameCreation"],
                        'game_version' : info["game_version"],
                        'tft_set_number' : info["tft_set_number"],
                        'queue_id' : info["queue_id"],
                    }
                )[0]
                MatchDto.objects.update_or_create(
                    metadata = metaObj,
                    info = infoObj
                )
                for participant in participants:
                    companion = CompanionDto.objects.update_or_create(
                        defaults={
                            'content_ID': participant["companion"]["content_ID"],
                            'item_ID': participant["companion"]["item_ID"],
                            'skin_ID': participant["companion"]["skin_ID"],
                            'species': participant["companion"]["species"],
                        }
                    )[0]
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
                                        
                    participantObj = ParticipantDto.objects.update_or_create(
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
                    )[0]
                    
                    for trait in traits:
                        participantObj.traits.add(TraitDto.objects.update_or_create(
                            name = trait["name"],
                            defaults={
                                'num_units' : trait["num_units"],
                                'style' : trait["style"],
                                'tier_current' : trait["tier_current"],
                                'tier_total' : trait["tier_total"],
                            }
                        )[0])
                    for unit in units:
                        character_id = unit["character_id"]
                        name = unit["name"]
                        rarity = unit["rarity"]
                        tier = unit["tier"]
                        
                        UnitObj = UnitDto.objects.update_or_create(
                            character_id = character_id,
                            defaults={
                                'name' : name,
                                'rarity' : rarity,
                                'tier' : tier,
                            }
                        )[0]
                        
                        for item in unit["itemNames"]:
                            UnitObj.items.add(ItemDto.objects.update_or_create(
                                name=item
                            )[0])
                    
                    participantObj.units.add(UnitObj)
                    infoObj.participants.add(participantObj)
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

