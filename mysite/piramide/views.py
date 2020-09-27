from django.shortcuts import get_object_or_404,render,redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.utils import timezone
from django.template import loader
from django.urls import reverse
from django.views.generic import View
from .models import Game,Deck,Player,Card
from .forms import *
import random, string

def shuffleDeck(deck0,deck1):
		cardList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
		21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
	 	42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
		cardList2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
		21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41,
	 	42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52]
		random.shuffle(cardList)
		random.shuffle(cardList2)
		temp = 0
		Deck = deck0
		num = cardList
		for x in range(1,105):
			if x == 53:
				temp = 52
				Deck = deck1
				num = cardList2
			if x - temp < 14:
				newCard = Card(deck=Deck, type='c', num=x-temp, deckNum=num.pop())
			elif x - temp < 27:
				newCard = Card(deck=Deck, type='d', num=x-13-temp, deckNum=num.pop())
			elif x - temp < 40:
				newCard = Card(deck=Deck, type='h', num=x-26-temp, deckNum=num.pop())
			elif x - temp <= 52:
				newCard = Card(deck=Deck, type='s', num=x-39-temp, deckNum=num.pop())
			newCard.save()

class Start(View):
	def get(self,request):
		form = CreateForm()
		return render(request, 'piramide/start.html', context={'form': form})

	def post(self,request):
		form = CreateForm(request.POST)
		if form.is_valid():
			newGame = Game(game_status=False)
			newGame.save()
			newPlayer = Player(game=newGame,name=request.POST['name'])
			newPlayer.save()
			return redirect('add_players_url', game_id=newGame.id)
		else:
			return render(request, 'piramide/start.html', context={'form': form})

class AddPlayers(View):
	def get(self,request,game_id):
		form = CreateForm()
		newGame = Game.objects.get(id=game_id)
		PlayerList=newGame.player_set.all()
		return render(request, 'piramide/addplayer.html', context={'form': form, 'newGame': newGame, 'PlayerList': PlayerList})
	
	def post(self,request,game_id):
		form = CreateForm(request.POST)
		curr_game = Game.objects.get(id=game_id)
		PlayerList=curr_game.player_set.all()
		if form.is_valid():
			if Player.objects.filter(name=request.POST['name'],game=game_id):
				Error_player = request.POST['name']
				return render(request, 'piramide/addplayer.html', context={'form': form, 'newGame': curr_game, 'PlayerList': PlayerList, 'Error_player': Error_player})
			else:
				newPlayer = Player(game=curr_game,name=request.POST['name'])
				newPlayer.save()
				return redirect('add_players_url', game_id=game_id)
		else:
			return render(request, 'piramide/addplayer.html', context={'form': form, 'newGame': curr_game, 'PlayerList': PlayerList})

class StartGame(View):
	def get(self,request,game_id):
		curr_game = Game.objects.get(id=game_id)
		PlayerList = curr_game.player_set.all()
		deck0 = Deck(game=curr_game)
		deck1 = Deck(game=curr_game)
		deck0.save()
		deck1.save()
		shuffleDeck(deck0,deck1)
		print("Deck N1")
		for x in range(1,53):
			t = deck0.card_set.get(deckNum=x)
			print("the card number {} is a: {} of {}".format(x,t.num,t.type))
		print("Deck N2")
		for x in range(1,53):
			t = deck1.card_set.get(deckNum=x)
			print("the card number {} is a: {} of {}".format(x,t.num,t.type))
		cards0 = deck0.card_set.all()
		cards1 = deck1.card_set.all()
		return render(request, 'piramide/game.html', context={'newGame': curr_game, 'PlayerList': PlayerList})

class DeletePlayer(View):
	def get(self,request,game_id,player_name):
		form = CreateForm()
		curr_game = Game.objects.get(id=game_id)
		PlayerList=curr_game.player_set.all()
		PlayerDelete = Player.objects.get(game=game_id,name=player_name)
		print("Jugador {} fue eliminado".format(PlayerDelete.name))
		PlayerDelete.delete()
		return redirect('add_players_url', game_id=game_id)