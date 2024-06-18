import json
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework.test import APITestCase 
from unittest.mock import Mock, patch

from .managers import SummonerManager

import requests

User = get_user_model()

class SummonerTest(APITestCase):
    def setUp(self):
        self.manager = SummonerManager()
        
        self.test_get_summoner_by_account()
    
    '''
    소환사 이름 검색 테스트 (deprecated)
    '''
    @patch("requests.get")
    def test_get_summoner_name(self, mock_get):
        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = {'id': '_W2ZdmV8930K5gjJBMoIMWyfyDpWDTOoP6pnR113R2guolg', 'accountId': 'TiDSnGC0RehGjoj9YDJo3rOJLiHIzMNQh9uYl0uqE8snQzo', 'puuid': 'cMxlrieGR92AHikvnZayJAUjRGAPjBdZHQKCaO8JJoQv9X9uTBv8B61GtwNGm-h6O7QtGL-hnozYkg', 'name': '안해봤지만', 'profileIconId': 6502, 'revisionDate': 1710912336000, 'summonerLevel': 113}

        summoner_name = '안해봤지만'
        
        summoner = self.manager.get_summoner_name(summoner_name)
        
        self.assertEqual(summoner["id"], "_W2ZdmV8930K5gjJBMoIMWyfyDpWDTOoP6pnR113R2guolg")
        self.assertEqual(summoner["accountId"], "TiDSnGC0RehGjoj9YDJo3rOJLiHIzMNQh9uYl0uqE8snQzo")
        self.assertEqual(summoner["puuid"], "cMxlrieGR92AHikvnZayJAUjRGAPjBdZHQKCaO8JJoQv9X9uTBv8B61GtwNGm-h6O7QtGL-hnozYkg")
        self.assertEqual(summoner["name"], "안해봤지만")
        self.assertEqual(summoner["profileIconId"], 6502)
        self.assertEqual(summoner["revisionDate"], 1710912336000)
        self.assertEqual(summoner["summonerLevel"], 113)
        mock_get.assert_called_once_with(f"https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/{summoner_name}", headers=self.manager.headers)
    
    @patch("requests.get")
    def test_get_summoner_by_account(self, mock_get):
        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = {'id': '6R2fdnyUsGYGnxc00U5w5CmCWZHZwCAuzOR8mfI8kQhqdM0', 'accountId': 'wZHkAi8hC0uB37X9p-aMR_HbASxWQK1vh5FtR7GH81zaCAo', 'puuid': 'ErsfHsgd7yCzyRcZxR4jSuDik_2Ow0GMYYdd3ogNG03YLxUqsAdf2V0bdlrNAX_br7GOdC4RNXslLg', 'profileIconId': 6502, 'revisionDate': 1714399589043, 'summonerLevel': 113}
        
        tagLine = '만인만사'
        gameName = '만사'
        
        summoner = self.manager.get_summoner_by_account(tagLine, gameName)
        
        self.assertEqual(summoner.summoner_id, "6R2fdnyUsGYGnxc00U5w5CmCWZHZwCAuzOR8mfI8kQhqdM0")
        self.assertEqual(summoner.account_id, "wZHkAi8hC0uB37X9p-aMR_HbASxWQK1vh5FtR7GH81zaCAo")
        self.assertEqual(summoner.puuid, "ErsfHsgd7yCzyRcZxR4jSuDik_2Ow0GMYYdd3ogNG03YLxUqsAdf2V0bdlrNAX_br7GOdC4RNXslLg")
        self.assertEqual(summoner.profileIconId, 6502)
        self.assertEqual(summoner.revisionDate, 1714399589043)
        self.assertEqual(summoner.summonerLevel, 113)
        
    @patch("requests.get")
    def test_get_league(self, mock_get):
        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = {
            "puuid": "ErsfHsgd7yCzyRcZxR4jSuDik_2Ow0GMYYdd3ogNG03YLxUqsAdf2V0bdlrNAX_br7GOdC4RNXslLg",
            "leagueId": "c9353fab-a304-3562-bdf5-e7375f43e1cd",
            "queueType": "RANKED_TFT",
            "tier": "MASTER",
            "rank": "I",
            "summonerId": "6R2fdnyUsGYGnxc00U5w5CmCWZHZwCAuzOR8mfI8kQhqdM0",
            "leaguePoints": 83,
            "wins": 228,
            "losses": 220,
            "veteran": True,
            "inactive": False,
            "freshBlood": False,
            "hotStreak": True
        }
        
        tagLine = '만인만사'
        gameName = '만사'
        
        summoner = self.manager.get_league()
        
        self.assertEqual(summoner["puuid"], "ErsfHsgd7yCzyRcZxR4jSuDik_2Ow0GMYYdd3ogNG03YLxUqsAdf2V0bdlrNAX_br7GOdC4RNXslLg")
        self.assertEqual(summoner["leagueId"], "c9353fab-a304-3562-bdf5-e7375f43e1cd")
        self.assertEqual(summoner["queueType"], "RANKED_TFT")
        self.assertEqual(summoner["tier"], "MASTER")
        self.assertEqual(summoner["rank"], "I")
        self.assertEqual(summoner["summonerId"], "6R2fdnyUsGYGnxc00U5w5CmCWZHZwCAuzOR8mfI8kQhqdM0")
        self.assertEqual(summoner["leaguePoints"], 83)
        self.assertEqual(summoner["wins"], 228)
        self.assertEqual(summoner["losses"], 220)
        self.assertEqual(summoner["veteran"], True)
        self.assertEqual(summoner["inactive"], False)
        self.assertEqual(summoner["freshBlood"], False)
        self.assertEqual(summoner["hotStreak"], True)
        
    # @patch("requests.get")
    def test_get_match_ids(self):
        # response = mock_get.return_value
        # response.status_code = 200
        # response.json.return_value = [] # KR_7002143070
        
        match_ids = self.manager.get_match_ids()
        
        # self.assertIsInstance(match_ids, list)
        # pass