from Card import Card
from Deck_of_Cards import Deck_of_Cards
from Player import Player

class CardGame:
    def __init__(self, player1, player2, num_cards):
        self.pack = Deck_of_Cards()
        self.player1 = Player(player1, num_cards)
        self.player2 = Player(player2, num_cards)

        if num_cards > 26 or num_cards < 10:    #Number of cards each player can't exceed 26 or below 10 cards
            num_cards = 26

        self.num_cards = num_cards
        self.new_game(self.num_cards)


    def new_game(self, num_cards):

        if len(self.player1.pack_player) == 0 and len(self.player2.pack_player) == 0:
            self.pack.cards_shuffle()
            self.player1.num_of_cards = num_cards
            self.player2.num_of_cards = num_cards
            for i in range(num_cards):
                self.player1.pack_player.append(self.pack.deal_one())
            for i in range(num_cards):
                self.player2.pack_player.append(self.pack.deal_one())
        else:
            print("error massage")
            raise TypeError("the player's pack is not empty")

    def get_winner(self):
        """The winner of the game is the player with most cards"""
        if self.player1.num_of_cards > self.player2.num_of_cards:
            return self.player1
        if self.player1.num_of_cards < self.player2.num_of_cards:
            return self.player2
        if self.player1.num_of_cards == self.player2.num_of_cards:
            return None