from django.db import models

# Create your models here.

class MatchDto(models.Model):
    metadata = models.ForeignKey('MetadataDto', on_delete=models.CASCADE)
    info = models.ForeignKey('InfoDto', on_delete=models.CASCADE)

class MetadataDto(models.Model):
    data_version = models.CharField(max_length=100)
    match_id = models.CharField(max_length=100)
    participants = models.ManyToManyField('ParticipantDto', related_name='metadata')

class InfoDto(models.Model):
    game_datetime = models.BigIntegerField()
    game_length = models.FloatField()
    game_variation = models.CharField(max_length=100)
    game_version = models.CharField(max_length=100)
    participants = models.ManyToManyField('ParticipantDto')
    tft_set_number = models.IntegerField()
    queue_id = models.IntegerField()

class ParticipantDto(models.Model):
    augments = models.ManyToManyField('AugmentDto')
    companion = models.ForeignKey('CompanionDto', on_delete=models.CASCADE)
    gold_left = models.IntegerField()
    last_round = models.IntegerField()
    level = models.IntegerField()
    placement = models.IntegerField()
    players_eliminated = models.IntegerField()
    puuid = models.CharField(max_length=100)
    time_eliminated = models.FloatField()
    total_damage_to_players = models.IntegerField()
    traits = models.ManyToManyField('TraitDto')
    units = models.ManyToManyField('UnitDto')
    
class TraitDto(models.Model):
    # class TraitName(models.TextChoices):
    #     Set10_Brawler = '난동꾼'
    name = models.CharField(max_length=100)
    num_units = models.IntegerField()
    style = models.IntegerField()
    tier_current = models.IntegerField()
    tier_total = models.IntegerField()
    
class UnitDto(models.Model):
    items = models.ManyToManyField('ItemDto')
    character_id = models.CharField(max_length=100)
    chosen = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    rarity = models.IntegerField()
    tier = models.IntegerField()
    
class ItemDto(models.Model):
    class ItemName(models.TextChoices):
        B_F_SWORD = 'B.F. Sword'
        NEEDLESSLY_LARGE_ROD = 'Needlessly Large Rod'
        RECURVE_BOW = 'Recurve Bow'
        SPARRING_GLOVES = 'Sparring Gloves'
        TEAR_OF_THE_GODDESS = 'Tear of the Goddess'
        CHAIN_VEST = 'Chain Vest'
        GIANT_S_BELT = 'Giant_s Belt'
        NEGATRON_CLOAK = 'Negatron Cloak'
    name = models.CharField(max_length=100, choices=ItemName.choices)
    num_units = models.IntegerField()
    style = models.IntegerField()
    tier = models.IntegerField()
    
class CompanionDto(models.Model):
    content_ID = models.CharField(max_length=100)
    skin_ID = models.CharField(max_length=100)
    species = models.CharField(max_length=100)
    
class SummonerDto(models.Model):
    account_id = models.CharField(max_length=100)
    puuid = models.CharField(max_length=100)
    summoner_id = models.CharField(max_length=100)
    summonerLevel = models.IntegerField()
    profileIconId = models.IntegerField()
    revisionDate = models.BigIntegerField()
    
class AugmentDto(models.Model):
    pass