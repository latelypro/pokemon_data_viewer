from django.db import models

# Create your models here.
class PokemonData(models.Model):
    no = models.IntegerField()
    name = models.CharField(max_length=255)
    hp = models.IntegerField()
    attack = models.IntegerField()
    defence = models.IntegerField()
    spAttack = models.IntegerField()
    spDefence = models.IntegerField()
    speed = models.IntegerField()
    isMegaEvolution = models.BooleanField()
    types = models.CharField(max_length=255)
    evolutions = models.CharField(max_length=255)
    abilities = models.CharField(max_length=255)
    hiddenAbilities = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

