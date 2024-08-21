import json
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from rest_framework.test import APITestCase 
from unittest.mock import Mock, patch

from .managers import SummonerManager
from .models import CompanionDto, InfoDto, ItemDto, MatchDto, MetadataDto, ParticipantDto, TraitDto, UnitDto
from django.db.models import Q
import requests

User = get_user_model()

class SummonerTest(APITestCase):
    def setUp(self):
        self.manager = SummonerManager()
        
        self.test_get_summoner_by_account()
        self.match = {
            "metadata": {
                "data_version": "5",
                "match_id": "KR_6986076420",
                "participants": [
                    "s5r9nGpuZYoKjbuBbNSUan64Mtlumjg8F0Jgfi7lXIIcUvtD46N_le4emK8ihPluzvy6uZFEC9qDHw",
                    "5x9w13ejBrzQ64fUBbNui0MkXMX7wQfFlvledz8esfJqIbNVLbSUiLM0V8eoyv1zzvDFewCFPnepKw",
                    "ErsfHsgd7yCzyRcZxR4jSuDik_2Ow0GMYYdd3ogNG03YLxUqsAdf2V0bdlrNAX_br7GOdC4RNXslLg",
                    "92HQ7Ql6TDQWW93EDp3MzNfue2bMK1-vyKyeKW7E_VbRypLHl52D-AmFOGz1DQvscQUHnmT8ZFpypg",
                    "LJZWdiCN3CCTT1t_8EWJcCfTuaxWR2kJxFgeT5RpHyvKBdoZfcmXUmF6FxhzKcMzf8oS2zF7S5nmYQ",
                    "zGIw-nZAp7iEmfOfkTThKiOoM6wWxFzm7VkYSIanatrOY9dmaXnt53DmvVj8gg2rQ6w-us-FLcQpMg",
                    "Cz6ZH3lpt5T46gRKkknUK2KOXNWFMM7z9gKZOnJewAlPXUPJGD4PzhZ00-6NRzDMtLDfp4Yfy_prHg",
                    "2DJxPUOXg8l1mHXcgUzYBZyXts-H9T0Zo-3Qyl5blaD2fzJZHGfFfoluWwd2SuTTV6UTY7ZoEyikcQ"
                ]
            },
            "info": {
                "endOfGameResult": "Abort_TooFewPlayers",
                "gameCreation": 1710297061000,
                "gameId": 6986076420,
                "game_datetime": 1710299252994,
                "game_length": 2173.651123046875,
                "game_version": "Version 14.5.565.1230 (Mar 05 2024/13:42:42) [PUBLIC] <Releases/14.5>",
                "mapId": 22,
                "participants": [
                    {
                        "augments": [
                            "TFT6_Augment_ClearMind",
                            "TFT9_Augment_CapriciousForge",
                            "TFT9_Augment_SupportCache"
                        ],
                        "companion": {
                            "content_ID": "6f3f9e25-6e91-436c-8621-5c74ee136635",
                            "item_ID": 44003,
                            "skin_ID": 3,
                            "species": "PetChibiLeeSin"
                        },
                        "gold_left": 1,
                        "last_round": 28,
                        "level": 9,
                        "missions": {
                            "Assists": 9,
                            "DamageDealt": 1,
                            "DamageDealtToObjectives": 1,
                            "DamageDealtToTurrets": 0,
                            "DamageTaken": 12,
                            "DoubleKills": 0,
                            "GoldEarned": 12,
                            "GoldSpent": 5,
                            "InhibitorsDestroyed": 0,
                            "Kills": 0,
                            "LargestKillingSpree": 0,
                            "LargestMultiKill": 3,
                            "MagicDamageDealt": 8,
                            "MagicDamageDealtToChampions": 9,
                            "NeutralMinionsKilledTeamJungle": 9,
                            "PhysicalDamageDealt": 4,
                            "PhysicalDamageTaken": 0,
                            "PlayerScore0": 7,
                            "PlayerScore1": 0,
                            "PlayerScore10": 169598,
                            "PlayerScore11": 7,
                            "PlayerScore2": 84,
                            "PlayerScore3": 114,
                            "PlayerScore4": 1,
                            "PlayerScore5": 1,
                            "PlayerScore6": 10,
                            "PlayerScore9": 18,
                            "QuadraKills": 7,
                            "Spell1Casts": 22542,
                            "Spell2Casts": 0,
                            "Spell3Casts": 0,
                            "Spell4Casts": 31,
                            "SummonerSpell1Casts": 24,
                            "TimeCCOthers": 0,
                            "TotalMinionsKilled": 0,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 7,
                            "VisionScore": 21729,
                            "WardsKilled": 0
                        },
                        "placement": 7,
                        "players_eliminated": 0,
                        "puuid": "s5r9nGpuZYoKjbuBbNSUan64Mtlumjg8F0Jgfi7lXIIcUvtD46N_le4emK8ihPluzvy6uZFEC9qDHw",
                        "time_eliminated": 1675.2586669921875,
                        "total_damage_to_players": 83,
                        "traits": [
                            {
                                "name": "Set10_Brawler",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Classical",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_CrowdDive",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Dazzler",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Deadeye",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_EDM",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Edgelord",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Fighter",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Guardian",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Hyperpop",
                                "num_units": 1,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Jazz",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Pentakill",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_PopBand",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Bard",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_MissFortune",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Yone",
                                "itemNames": [
                                    "TFT_Item_Shroud"
                                ],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Sett",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Ezreal",
                                "itemNames": [],
                                "name": "",
                                "rarity": 4,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Zed",
                                "itemNames": [
                                    "TFT9_Item_OrnnPrototypeForge",
                                    "TFT9_Item_OrnnHullbreaker",
                                    "TFT4_Item_OrnnEternalWinter"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Jhin",
                                "itemNames": [
                                    "TFT_Item_InfinityEdge",
                                    "TFT_Item_GuardianAngel"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Ziggs",
                                "itemNames": [
                                    "TFT_Item_JeweledGauntlet",
                                    "TFT_Item_GuinsoosRageblade",
                                    "TFT_Item_UnstableConcoction"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Yorick",
                                "itemNames": [
                                    "TFT_Item_GargoyleStoneplate",
                                    "TFT_Item_SpectralGauntlet"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 2
                            }
                        ]
                    },
                    {
                        "augments": [
                            "TFT10_Augment_VampirismPlus",
                            "TFT9_Augment_HealingOrbsII",
                            "TFT9_Augment_BigGrabBag"
                        ],
                        "companion": {
                            "content_ID": "24567fc4-e861-40c5-9e82-ef509f7b8735",
                            "item_ID": 2021,
                            "skin_ID": 21,
                            "species": "PetGriffin"
                        },
                        "gold_left": 0,
                        "last_round": 30,
                        "level": 9,
                        "missions": {
                            "Assists": 15,
                            "DamageDealt": 0,
                            "DamageDealtToObjectives": 1,
                            "DamageDealtToTurrets": 0,
                            "DamageTaken": 11,
                            "DoubleKills": 0,
                            "GoldEarned": 12,
                            "GoldSpent": 16,
                            "InhibitorsDestroyed": 14,
                            "Kills": 0,
                            "LargestKillingSpree": 1,
                            "LargestMultiKill": 4,
                            "MagicDamageDealt": 8,
                            "MagicDamageDealtToChampions": 11,
                            "NeutralMinionsKilledTeamJungle": 8,
                            "PhysicalDamageDealt": 4,
                            "PhysicalDamageTaken": 0,
                            "PlayerScore0": 5,
                            "PlayerScore1": 0,
                            "PlayerScore10": 212306,
                            "PlayerScore11": 8,
                            "PlayerScore2": 88,
                            "PlayerScore3": 122,
                            "PlayerScore4": 2,
                            "PlayerScore5": 3,
                            "PlayerScore6": 10,
                            "PlayerScore9": 15,
                            "QuadraKills": 8,
                            "Spell1Casts": 99416,
                            "Spell2Casts": 0,
                            "Spell3Casts": 0,
                            "Spell4Casts": 41,
                            "SummonerSpell1Casts": 21,
                            "TimeCCOthers": 0,
                            "TotalMinionsKilled": 7,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 7,
                            "VisionScore": 164301,
                            "WardsKilled": 0
                        },
                        "placement": 5,
                        "players_eliminated": 0,
                        "puuid": "5x9w13ejBrzQ64fUBbNui0MkXMX7wQfFlvledz8esfJqIbNVLbSUiLM0V8eoyv1zzvDFewCFPnepKw",
                        "time_eliminated": 1770.173583984375,
                        "total_damage_to_players": 76,
                        "traits": [
                            {
                                "name": "Set10_Brawler",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_DJ",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_Emo",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Guardian",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_IllBeats",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_KDA",
                                "num_units": 4,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Pentakill",
                                "num_units": 0,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Sentinel",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Spellweaver",
                                "num_units": 5,
                                "style": 2,
                                "tier_current": 2,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Superfan",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_TrueDamage",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Lillia",
                                "itemNames": [],
                                "name": "",
                                "rarity": 0,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Annie",
                                "itemNames": [
                                    "TFT_Item_Leviathan",
                                    "TFT_Item_SpearOfShojin",
                                    "TFT_Item_JeweledGauntlet"
                                ],
                                "name": "",
                                "rarity": 0,
                                "tier": 3
                            },
                            {
                                "character_id": "TFT10_Kennen",
                                "itemNames": [],
                                "name": "",
                                "rarity": 0,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Seraphine",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Neeko",
                                "itemNames": [
                                    "TFT_Item_GargoyleStoneplate"
                                ],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Ekko",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Ahri",
                                "itemNames": [
                                    "TFT_Item_JeweledGauntlet",
                                    "TFT_Item_Leviathan",
                                    "TFT_Item_HextechGunblade"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Illaoi",
                                "itemNames": [
                                    "TFT_Item_FrozenHeart"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Sona",
                                "itemNames": [
                                    "TFT_Item_StatikkShiv"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            }
                        ]
                    },
                    {
                        "augments": [
                            "TFT10_Augment_VampirismPlus",
                            "TFT9_Augment_JeweledLotus",
                            "TFT10_Augment_HeroicGrabBag"
                        ],
                        "companion": {
                            "content_ID": "51e12c33-bf9a-4cd7-b619-36fe636952ee",
                            "item_ID": 44001,
                            "skin_ID": 1,
                            "species": "PetChibiLeeSin"
                        },
                        "gold_left": 1,
                        "last_round": 38,
                        "level": 9,
                        "missions": {
                            "Assists": 15,
                            "DamageDealt": 1,
                            "DamageDealtToObjectives": 1,
                            "DamageDealtToTurrets": 1,
                            "DamageTaken": 18,
                            "DoubleKills": 0,
                            "GoldEarned": 16,
                            "GoldSpent": 10,
                            "InhibitorsDestroyed": 15,
                            "Kills": 0,
                            "LargestKillingSpree": 1,
                            "LargestMultiKill": 5,
                            "MagicDamageDealt": 8,
                            "MagicDamageDealtToChampions": 10,
                            "NeutralMinionsKilledTeamJungle": 16,
                            "PhysicalDamageDealt": 6,
                            "PhysicalDamageTaken": 0,
                            "PlayerScore0": 1,
                            "PlayerScore1": 0,
                            "PlayerScore10": 357304,
                            "PlayerScore11": 6,
                            "PlayerScore2": 216,
                            "PlayerScore3": 130,
                            "PlayerScore4": 2,
                            "PlayerScore5": 3,
                            "PlayerScore6": 11,
                            "PlayerScore9": 48,
                            "QuadraKills": 7,
                            "Spell1Casts": 78422,
                            "Spell2Casts": 1,
                            "Spell3Casts": 0,
                            "Spell4Casts": 38,
                            "SummonerSpell1Casts": 25,
                            "TimeCCOthers": 1,
                            "TotalMinionsKilled": 8,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 6,
                            "VisionScore": 24638,
                            "WardsKilled": 0
                        },
                        "placement": 1,
                        "players_eliminated": 2,
                        "puuid": "ErsfHsgd7yCzyRcZxR4jSuDik_2Ow0GMYYdd3ogNG03YLxUqsAdf2V0bdlrNAX_br7GOdC4RNXslLg",
                        "time_eliminated": 2169.73486328125,
                        "total_damage_to_players": 157,
                        "traits": [
                            {
                                "name": "Set10_8Bit",
                                "num_units": 6,
                                "style": 3,
                                "tier_current": 3,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Brawler",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Edgelord",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Fighter",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Guardian",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_IllBeats",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_Jazz",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Pentakill",
                                "num_units": 4,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Quickshot",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Sentinel",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Kayle",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Garen",
                                "itemNames": [
                                    "TFT_Item_SpectralGauntlet"
                                ],
                                "name": "",
                                "rarity": 1,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Mordekaiser",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Riven",
                                "itemNames": [
                                    "TFT_Item_Quicksilver",
                                    "TFT_Item_Bloodthirster",
                                    "TFT_Item_NightHarvester"
                                ],
                                "name": "",
                                "rarity": 2,
                                "tier": 3
                            },
                            {
                                "character_id": "TFT10_Viego",
                                "itemNames": [
                                    "TFT10_Item_8bitEmblem",
                                    "TFT_Item_TitansResolve"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Caitlyn",
                                "itemNames": [
                                    "TFT_Item_SpearOfShojin",
                                    "TFT_Item_GuinsoosRageblade"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Illaoi",
                                "itemNames": [],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Lucian",
                                "itemNames": [
                                    "TFT10_Item_8bitEmblem"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Yorick",
                                "itemNames": [],
                                "name": "",
                                "rarity": 6,
                                "tier": 2
                            }
                        ]
                    },
                    {
                        "augments": [
                            "TFT9_Augment_NotToday",
                            "TFT6_Augment_Keepers2",
                            "TFT9_Augment_BigGrabBag"
                        ],
                        "companion": {
                            "content_ID": "ed292b35-08d3-4291-b345-29d07c2812fa",
                            "item_ID": 29006,
                            "skin_ID": 6,
                            "species": "PetDowsie"
                        },
                        "gold_left": 25,
                        "last_round": 24,
                        "level": 7,
                        "missions": {
                            "Assists": 0,
                            "DamageDealt": 1,
                            "DamageDealtToObjectives": 1,
                            "DamageDealtToTurrets": 1,
                            "DamageTaken": 4,
                            "DoubleKills": 2,
                            "GoldEarned": 10,
                            "GoldSpent": 4,
                            "InhibitorsDestroyed": 0,
                            "Kills": 0,
                            "LargestKillingSpree": 1,
                            "LargestMultiKill": 3,
                            "MagicDamageDealt": 6,
                            "MagicDamageDealtToChampions": 0,
                            "NeutralMinionsKilledTeamJungle": 10,
                            "PhysicalDamageDealt": 3,
                            "PhysicalDamageTaken": 11,
                            "PlayerScore0": 8,
                            "PlayerScore1": 0,
                            "PlayerScore10": 106097,
                            "PlayerScore11": 4,
                            "PlayerScore2": 69,
                            "PlayerScore3": 78,
                            "PlayerScore4": 0,
                            "PlayerScore5": 0,
                            "PlayerScore6": 8,
                            "PlayerScore9": 28,
                            "QuadraKills": 8,
                            "Spell1Casts": 30265,
                            "Spell2Casts": 0,
                            "Spell3Casts": 0,
                            "Spell4Casts": 12,
                            "SummonerSpell1Casts": 17,
                            "TimeCCOthers": 1,
                            "TotalMinionsKilled": 9,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 6,
                            "VisionScore": 17869,
                            "WardsKilled": 0
                        },
                        "placement": 8,
                        "players_eliminated": 0,
                        "puuid": "92HQ7Ql6TDQWW93EDp3MzNfue2bMK1-vyKyeKW7E_VbRypLHl52D-AmFOGz1DQvscQUHnmT8ZFpypg",
                        "time_eliminated": 1392.8875732421875,
                        "total_damage_to_players": 77,
                        "traits": [
                            {
                                "name": "Set10_Brawler",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Country",
                                "num_units": 2,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_EDM",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Emo",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Fighter",
                                "num_units": 6,
                                "style": 3,
                                "tier_current": 3,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Funk",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Pentakill",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_PopBand",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_PunkRock",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Spellweaver",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Superfan",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Vi",
                                "itemNames": [],
                                "name": "",
                                "rarity": 0,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Gnar",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Jax",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Gragas",
                                "itemNames": [
                                    "TFT_Item_ThiefsGloves",
                                    "TFT_Item_GuinsoosRageblade",
                                    "TFT_Item_MadredsBloodrazor"
                                ],
                                "name": "",
                                "rarity": 1,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Sett",
                                "itemNames": [
                                    "TFT_Item_ThiefsGloves",
                                    "TFT_Item_RunaansHurricane",
                                    "TFT_Item_UnstableConcoction"
                                ],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Urgot",
                                "itemNames": [
                                    "TFT_Item_Morellonomicon",
                                    "TFT_Item_GuardianAngel"
                                ],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Poppy",
                                "itemNames": [],
                                "name": "",
                                "rarity": 4,
                                "tier": 1
                            }
                        ]
                    },
                    {
                        "augments": [
                            "TFT10_Augment_GoodForSomething",
                            "TFT9_Augment_Harmacist2",
                            "TFT9_Augment_YouHaveMySword"
                        ],
                        "companion": {
                            "content_ID": "2fc3a4c0-7322-4ef5-b434-0cea1d1997e6",
                            "item_ID": 35001,
                            "skin_ID": 1,
                            "species": "PetChibiJinx"
                        },
                        "gold_left": 0,
                        "last_round": 33,
                        "level": 9,
                        "missions": {
                            "Assists": 9,
                            "DamageDealt": 0,
                            "DamageDealtToObjectives": 1,
                            "DamageDealtToTurrets": 0,
                            "DamageTaken": 16,
                            "DoubleKills": 2,
                            "GoldEarned": 46,
                            "GoldSpent": 20,
                            "InhibitorsDestroyed": 0,
                            "Kills": 0,
                            "LargestKillingSpree": 0,
                            "LargestMultiKill": 4,
                            "MagicDamageDealt": 8,
                            "MagicDamageDealtToChampions": 15,
                            "NeutralMinionsKilledTeamJungle": 8,
                            "PhysicalDamageDealt": 6,
                            "PhysicalDamageTaken": 0,
                            "PlayerScore0": 3,
                            "PlayerScore1": 0,
                            "PlayerScore10": 253252,
                            "PlayerScore11": 8,
                            "PlayerScore2": 192,
                            "PlayerScore3": 112,
                            "PlayerScore4": 2,
                            "PlayerScore5": 3,
                            "PlayerScore6": 9,
                            "PlayerScore9": 47,
                            "QuadraKills": 6,
                            "Spell1Casts": 82281,
                            "Spell2Casts": 0,
                            "Spell3Casts": 0,
                            "Spell4Casts": 40,
                            "SummonerSpell1Casts": 27,
                            "TimeCCOthers": 0,
                            "TotalMinionsKilled": 6,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 6,
                            "VisionScore": 23872,
                            "WardsKilled": 0
                        },
                        "placement": 3,
                        "players_eliminated": 2,
                        "puuid": "LJZWdiCN3CCTT1t_8EWJcCfTuaxWR2kJxFgeT5RpHyvKBdoZfcmXUmF6FxhzKcMzf8oS2zF7S5nmYQ",
                        "time_eliminated": 1924.120361328125,
                        "total_damage_to_players": 94,
                        "traits": [
                            {
                                "name": "Set10_Brawler",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_CrowdDive",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Dazzler",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Deadeye",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_EDM",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Fighter",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Guardian",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Hyperpop",
                                "num_units": 1,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_IllBeats",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_Jazz",
                                "num_units": 3,
                                "style": 2,
                                "tier_current": 2,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Pentakill",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_PopBand",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Quickshot",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Bard",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_MissFortune",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Sett",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Zac",
                                "itemNames": [
                                    "TFT_Item_Crownguard",
                                    "TFT_Item_NightHarvester"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Zed",
                                "itemNames": [
                                    "TFT_Item_GuardianAngel",
                                    "TFT_Item_Bloodthirster"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Illaoi",
                                "itemNames": [],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Lucian",
                                "itemNames": [
                                    "TFT_Item_InfinityEdge"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Ziggs",
                                "itemNames": [
                                    "TFT_Item_BlueBuff",
                                    "TFT_Item_RapidFireCannon",
                                    "TFT_Item_UnstableConcoction"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Yorick",
                                "itemNames": [
                                    "TFT_Item_ThiefsGloves",
                                    "TFT_Item_SteraksGage",
                                    "TFT_Item_RunaansHurricane"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            }
                        ]
                    },
                    {
                        "augments": [
                            "TFT9_Augment_LearningFromExperience2",
                            "TFT10_Augment_CrashTestDummies",
                            "TFT10_Augment_LittleBuddies"
                        ],
                        "companion": {
                            "content_ID": "721ab104-4188-4ce3-b64c-2126b889f37f",
                            "item_ID": 29010,
                            "skin_ID": 10,
                            "species": "PetDowsie"
                        },
                        "gold_left": 1,
                        "last_round": 38,
                        "level": 9,
                        "missions": {
                            "Assists": 26,
                            "DamageDealt": 1,
                            "DamageDealtToObjectives": 4,
                            "DamageDealtToTurrets": 1,
                            "DamageTaken": 22,
                            "DoubleKills": 1,
                            "GoldEarned": 17,
                            "GoldSpent": 21,
                            "InhibitorsDestroyed": 0,
                            "Kills": 0,
                            "LargestKillingSpree": 1,
                            "LargestMultiKill": 5,
                            "MagicDamageDealt": 8,
                            "MagicDamageDealtToChampions": 17,
                            "NeutralMinionsKilledTeamJungle": 16,
                            "PhysicalDamageDealt": 8,
                            "PhysicalDamageTaken": 6,
                            "PlayerScore0": 2,
                            "PlayerScore1": 0,
                            "PlayerScore10": 319852,
                            "PlayerScore11": 11,
                            "PlayerScore2": 216,
                            "PlayerScore3": 130,
                            "PlayerScore4": 1,
                            "PlayerScore5": 6,
                            "PlayerScore6": 13,
                            "PlayerScore9": 54,
                            "QuadraKills": 11,
                            "Spell1Casts": 74869,
                            "Spell2Casts": 0,
                            "Spell3Casts": 0,
                            "Spell4Casts": 32,
                            "SummonerSpell1Casts": 23,
                            "TimeCCOthers": 1,
                            "TotalMinionsKilled": 7,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 6,
                            "VisionScore": 233168,
                            "WardsKilled": 0
                        },
                        "placement": 2,
                        "players_eliminated": 2,
                        "puuid": "zGIw-nZAp7iEmfOfkTThKiOoM6wWxFzm7VkYSIanatrOY9dmaXnt53DmvVj8gg2rQ6w-us-FLcQpMg",
                        "time_eliminated": 2169.634765625,
                        "total_damage_to_players": 164,
                        "traits": [
                            {
                                "name": "Set10_Brawler",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Dazzler",
                                "num_units": 4,
                                "style": 3,
                                "tier_current": 2,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Funk",
                                "num_units": 5,
                                "style": 3,
                                "tier_current": 3,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Hyperpop",
                                "num_units": 2,
                                "style": 3,
                                "tier_current": 2,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_IllBeats",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_Jazz",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Sentinel",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Spellweaver",
                                "num_units": 2,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Nami",
                                "itemNames": [],
                                "name": "",
                                "rarity": 0,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Nami",
                                "itemNames": [],
                                "name": "",
                                "rarity": 0,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Bard",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Gragas",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Lulu",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_TwistedFate",
                                "itemNames": [
                                    "TFT_Item_Morellonomicon",
                                    "TFT_Item_SpearOfShojin",
                                    "TFT_Item_Leviathan"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Blitzcrank",
                                "itemNames": [
                                    "TFT_Item_DragonsClaw",
                                    "TFT_Item_Crownguard"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 3
                            },
                            {
                                "character_id": "TFT10_Illaoi",
                                "itemNames": [
                                    "TFT_Item_Crownguard"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Ziggs",
                                "itemNames": [
                                    "TFT_Item_Leviathan",
                                    "TFT_Item_GuinsoosRageblade",
                                    "TFT_Item_RabadonsDeathcap"
                                ],
                                "name": "",
                                "rarity": 6,
                                "tier": 2
                            }
                        ]
                    },
                    {
                        "augments": [
                            "TFT10_Augment_LuckyStreak",
                            "TFT10_Augment_CrashTestDummies",
                            "TFT9_Augment_HealingOrbsII"
                        ],
                        "companion": {
                            "content_ID": "50891d73-0465-4076-99c2-f5e372e4647c",
                            "item_ID": 24022,
                            "skin_ID": 22,
                            "species": "PetBellswayer"
                        },
                        "gold_left": 52,
                        "last_round": 31,
                        "level": 8,
                        "missions": {
                            "Assists": 0,
                            "DamageDealt": 1,
                            "DamageDealtToObjectives": 3,
                            "DamageDealtToTurrets": 1,
                            "DamageTaken": 16,
                            "DoubleKills": 0,
                            "GoldEarned": 5,
                            "GoldSpent": 16,
                            "InhibitorsDestroyed": 8,
                            "Kills": 0,
                            "LargestKillingSpree": 0,
                            "LargestMultiKill": 4,
                            "MagicDamageDealt": 7,
                            "MagicDamageDealtToChampions": 10,
                            "NeutralMinionsKilledTeamJungle": 9,
                            "PhysicalDamageDealt": 5,
                            "PhysicalDamageTaken": 0,
                            "PlayerScore0": 4,
                            "PlayerScore1": 0,
                            "PlayerScore10": 208525,
                            "PlayerScore11": 9,
                            "PlayerScore2": 183,
                            "PlayerScore3": 149,
                            "PlayerScore4": 2,
                            "PlayerScore5": 3,
                            "PlayerScore6": 13,
                            "PlayerScore9": 26,
                            "QuadraKills": 11,
                            "Spell1Casts": 76338,
                            "Spell2Casts": 0,
                            "Spell3Casts": 0,
                            "Spell4Casts": 25,
                            "SummonerSpell1Casts": 21,
                            "TimeCCOthers": 0,
                            "TotalMinionsKilled": 7,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 6,
                            "VisionScore": 109463,
                            "WardsKilled": 0
                        },
                        "placement": 4,
                        "players_eliminated": 0,
                        "puuid": "Cz6ZH3lpt5T46gRKkknUK2KOXNWFMM7z9gKZOnJewAlPXUPJGD4PzhZ00-6NRzDMtLDfp4Yfy_prHg",
                        "time_eliminated": 1830.54150390625,
                        "total_damage_to_players": 70,
                        "traits": [
                            {
                                "name": "Set10_Breakout",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_Edgelord",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Executioner",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Fighter",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Guardian",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_KDA",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Pentakill",
                                "num_units": 5,
                                "style": 2,
                                "tier_current": 2,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Sentinel",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Superfan",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Lillia",
                                "itemNames": [],
                                "name": "",
                                "rarity": 0,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Gnar",
                                "itemNames": [],
                                "name": "",
                                "rarity": 1,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Kayle",
                                "itemNames": [
                                    "TFT_Item_GuinsoosRageblade",
                                    "TFT7_Item_ShimmerscaleGamblersBlade",
                                    "TFT_Item_GuinsoosRageblade"
                                ],
                                "name": "",
                                "rarity": 1,
                                "tier": 3
                            },
                            {
                                "character_id": "TFT10_Neeko",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Mordekaiser",
                                "itemNames": [
                                    "TFT_Item_ThiefsGloves",
                                    "TFT_Item_PowerGauntlet",
                                    "TFT_Item_BlueBuff"
                                ],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Viego",
                                "itemNames": [
                                    "TFT_Item_GuardianAngel"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Karthus",
                                "itemNames": [
                                    "TFT_Item_SpearOfShojin",
                                    "TFT_Item_HextechGunblade"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Akali",
                                "itemNames": [
                                    "TFT_Item_Bloodthirster",
                                    "TFT_Item_UnstableConcoction"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            }
                        ]
                    },
                    {
                        "augments": [
                            "TFT10_Augment_BigGains",
                            "TFT10_Augment_VampirismPlus",
                            "TFT9_Augment_Commander_TeamingUp2"
                        ],
                        "companion": {
                            "content_ID": "3699a18b-fad8-43e0-89e2-359c00765982",
                            "item_ID": 5020,
                            "skin_ID": 20,
                            "species": "PetMiniGolem"
                        },
                        "gold_left": 2,
                        "last_round": 28,
                        "level": 8,
                        "missions": {
                            "Assists": 1,
                            "DamageDealt": 0,
                            "DamageDealtToObjectives": 1,
                            "DamageDealtToTurrets": 1,
                            "DamageTaken": 8,
                            "DoubleKills": 0,
                            "GoldEarned": 16,
                            "GoldSpent": 3,
                            "InhibitorsDestroyed": 10,
                            "Kills": 0,
                            "LargestKillingSpree": 0,
                            "LargestMultiKill": 3,
                            "MagicDamageDealt": 7,
                            "MagicDamageDealtToChampions": 7,
                            "NeutralMinionsKilledTeamJungle": 7,
                            "PhysicalDamageDealt": 4,
                            "PhysicalDamageTaken": 0,
                            "PlayerScore0": 6,
                            "PlayerScore1": 0,
                            "PlayerScore10": 189490,
                            "PlayerScore11": 1,
                            "PlayerScore2": 84,
                            "PlayerScore3": 131,
                            "PlayerScore4": 2,
                            "PlayerScore5": 3,
                            "PlayerScore6": 2,
                            "PlayerScore9": 27,
                            "QuadraKills": 8,
                            "Spell1Casts": 38692,
                            "Spell2Casts": 1,
                            "Spell3Casts": 0,
                            "Spell4Casts": 21,
                            "SummonerSpell1Casts": 21,
                            "TimeCCOthers": 0,
                            "TotalMinionsKilled": 7,
                            "TrueDamageDealtToChampions": 0,
                            "UnrealKills": 6,
                            "VisionScore": 51542,
                            "WardsKilled": 0
                        },
                        "placement": 6,
                        "players_eliminated": 0,
                        "puuid": "2DJxPUOXg8l1mHXcgUzYBZyXts-H9T0Zo-3Qyl5blaD2fzJZHGfFfoluWwd2SuTTV6UTY7ZoEyikcQ",
                        "time_eliminated": 1680.4068603515625,
                        "total_damage_to_players": 56,
                        "traits": [
                            {
                                "name": "Set10_8Bit",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Breakout",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_Classical",
                                "num_units": 1,
                                "style": 5,
                                "tier_current": 1,
                                "tier_total": 1
                            },
                            {
                                "name": "Set10_Deadeye",
                                "num_units": 2,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Executioner",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_Funk",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_KDA",
                                "num_units": 3,
                                "style": 1,
                                "tier_current": 1,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_PopBand",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Sentinel",
                                "num_units": 4,
                                "style": 2,
                                "tier_current": 2,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Spellweaver",
                                "num_units": 2,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            },
                            {
                                "name": "Set10_Superfan",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 3
                            },
                            {
                                "name": "Set10_TrueDamage",
                                "num_units": 1,
                                "style": 0,
                                "tier_current": 0,
                                "tier_total": 4
                            }
                        ],
                        "units": [
                            {
                                "character_id": "TFT10_Lillia",
                                "itemNames": [],
                                "name": "",
                                "rarity": 0,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Garen",
                                "itemNames": [
                                    "TFT_Item_TitansResolve",
                                    "TFT_Item_ArchangelsStaff",
                                    "TFT_Item_Bloodthirster"
                                ],
                                "name": "",
                                "rarity": 1,
                                "tier": 3
                            },
                            {
                                "character_id": "TFT10_Ekko",
                                "itemNames": [],
                                "name": "",
                                "rarity": 2,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Ahri",
                                "itemNames": [
                                    "TFT_Item_PowerGauntlet",
                                    "TFT_Item_HextechGunblade"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Ezreal",
                                "itemNames": [],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Akali",
                                "itemNames": [
                                    "TFT_Item_GuardianAngel"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 2
                            },
                            {
                                "character_id": "TFT10_Blitzcrank",
                                "itemNames": [
                                    "TFT_Item_ZekesHerald"
                                ],
                                "name": "",
                                "rarity": 4,
                                "tier": 1
                            },
                            {
                                "character_id": "TFT10_Jhin",
                                "itemNames": [],
                                "name": "",
                                "rarity": 6,
                                "tier": 1
                            }
                        ]
                    }
                ],
                "queueId": 1100,
                "queue_id": 1100,
                "tft_game_type": "standard",
                "tft_set_core_name": "TFTSet10",
                "tft_set_number": 10
            }
        }
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
        
    @patch("requests.get")
    def test_get_match_ids(self, mock_get):
        response = mock_get.return_value
        response.status_code = 200
        response.json.return_value = self.match
        
        # participants = self.manager.get_match_ids(self.manager.summoner["puuid"])
        # print('test_get_match_ids')
        # self.assertIsInstance(match_ids, list)
    
    def test_set_match(self):
        metadata = self.match["metadata"]
        metaObj = MetadataDto.objects.update_or_create(
            match_id = metadata["match_id"],
            defaults={
                'data_version' : metadata["data_version"],
            }
        )[0]
        metaObj.set_participants(metadata["participants"])
        info = self.match["info"]
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
        matchObj = MatchDto(metadata=metaObj, info=infoObj)
        matchObj.save()
        
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
            
        self.assertEqual(matchObj.metadata, metaObj)
        self.assertEqual(matchObj.info, infoObj)
        
    def test_get_match(self):
        self.test_set_match()
        puuid = self.manager.summoner["puuid"]
        
        metaObj = MetadataDto.objects.filter(Q(participants__icontains=puuid))
        
        matches = MatchDto.objects.filter(metadata__in=metaObj)
        
        
        
        