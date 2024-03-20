import requests
import os

summoner_url = os.environ.get('SUMMONER_URL')
headers = {}
headers['Content-Type'] = 'application/json'
headers['X-Riot-Token'] = os.environ.get('RIOT_API_DEVELOPMENT_KEY') if os.environ.get('DEBUG') else os.environ.get('RIOT_API_KEY')

def get_summoner_name(name):
    response = requests.get(f"{summoner_url}by-name/{name}", headers=headers)
    if response.status_code != 200:
        raise Exception("Failed to get a summoner.")
    return response.json()

