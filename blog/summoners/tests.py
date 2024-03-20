import json
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework.test import APITestCase 
from unittest.mock import Mock, patch

from .summoner_manager import get_summoner_name, headers

import requests

User = get_user_model()

class SummonerTest(APITestCase):
    @patch("requests.get")
    def test_get_summoner_name(self, mock_get):
        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = {'id': '_W2ZdmV8930K5gjJBMoIMWyfyDpWDTOoP6pnR113R2guolg', 'accountId': 'TiDSnGC0RehGjoj9YDJo3rOJLiHIzMNQh9uYl0uqE8snQzo', 'puuid': 'cMxlrieGR92AHikvnZayJAUjRGAPjBdZHQKCaO8JJoQv9X9uTBv8B61GtwNGm-h6O7QtGL-hnozYkg', 'name': '안해봤지만', 'profileIconId': 6502, 'revisionDate': 1710912336000, 'summonerLevel': 113}

        summoner_name = '안해봤지만'
        
        summoner = get_summoner_name(summoner_name)
        
        self.assertEqual(summoner["id"], "_W2ZdmV8930K5gjJBMoIMWyfyDpWDTOoP6pnR113R2guolg")
        self.assertEqual(summoner["accountId"], "TiDSnGC0RehGjoj9YDJo3rOJLiHIzMNQh9uYl0uqE8snQzo")
        self.assertEqual(summoner["puuid"], "cMxlrieGR92AHikvnZayJAUjRGAPjBdZHQKCaO8JJoQv9X9uTBv8B61GtwNGm-h6O7QtGL-hnozYkg")
        self.assertEqual(summoner["name"], "안해봤지만")
        self.assertEqual(summoner["profileIconId"], 6502)
        self.assertEqual(summoner["revisionDate"], 1710912336000)
        self.assertEqual(summoner["summonerLevel"], 113)
        mock_get.assert_called_once_with("https://kr.api.riotgames.com/tft/summoner/v1/summoners/by-name/안해봤지만", headers=headers)
    
    