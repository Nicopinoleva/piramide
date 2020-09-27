from django.db import models
import datetime
from django.utils import timezone

class Game(models.Model):
	game_status = models.BooleanField(default=False)

class Player(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	name = models.CharField(max_length=25)
	drinks = models.IntegerField(default=0)
	class Meta:
		constraints = [
			models.UniqueConstraint(fields=['game','name'], name='unique_player')
		]

class Deck(models.Model):
	game = models.ForeignKey(Game, on_delete=models.CASCADE)
	card_count = models.IntegerField(default=52)
	
class Card(models.Model):
	deck = models.ForeignKey(Deck, on_delete=models.CASCADE)
	player = models.ForeignKey(Player, on_delete=models.CASCADE, blank=True, null=True)
	type = models.CharField(max_length=1)
	num = models.IntegerField(default=1)
	deckNum = models.IntegerField(default=1)