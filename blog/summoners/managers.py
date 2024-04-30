import requests
import os
from .models import SummonerDto

class SummonerManager:
    '''
    소환사 정보를 가져오는 클래스
    '''
    summoner_url = os.environ.get('SUMMONER_URL')
    account_url = os.environ.get('ACCOUNT_URL')
    match_url = os.environ.get('MATCH_URL')
    league_url = os.environ.get('LEAGUE_URL')
    season_startTime = {"11" : 1710892800}
    headers = {}
    headers['Content-Type'] = 'application/json'
    headers['X-Riot-Token'] = os.environ.get('RIOT_API_KEY')
    summoner = None
    '''
    decorator
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
            return response.json()
        return wrapper
    '''
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
    
    # 소환사의 게임 정보를 가져오는 함수
    def get_match_ids(self):
        if self.summoner is None:
            raise Exception("Summoner is not set.")
        puuid = self.summoner["puuid"]
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
        
