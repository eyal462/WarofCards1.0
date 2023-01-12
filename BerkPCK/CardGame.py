from Card import Card
from Deck_of_Cards import Deck_of_Cards
from Player import Player

class CardGame:
    def __init__(self, player1: Player, player2: Player, num_cards):
        self.pack = Deck_of_Cards()
        self.player1 = player1
        self.player2 = player2

        if num_cards > 26 or num_cards < 10:
            num_cards = 26
        self.num_cards = num_cards
        self.new_game(num_cards)


    def new_game(self, num_cards):
        count1 = 0
        count2 = 0
        self.pack.cards_shuffle()
        self.player1.num_of_cards = num_cards
        self.player2.num_of_cards = num_cards
        for i in range(num_cards):
            self.player1.pack_player.append(self.pack.deal_one())
        for i in range(num_cards):
            self.player2.pack_player.append(self.pack.deal_one())


    def get_winner(self):
        if self.player1.pack_player > self.player2.pack_player:
            return self.player1
        if self.player2.pack_player > self.player1.pack_player:
            return self.player2
        else:
            return None
