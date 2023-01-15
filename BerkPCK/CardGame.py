from Card import Card
from Deck_of_Cards import Deck_of_Cards
from Player import Player

class CardGame:
    def __init__(self, player1, player2, num_cards):
        """initialize card game, creates objects of a players"""
        self.pack = Deck_of_Cards()
        if player1 == type(int) or player2 == type(int):
            raise TypeError("name can't be number")
        if player1 == "" or player2 == "":
            raise TypeError("name can't be empty")
        if num_cards == type(str):
            raise TypeError("number of cards can't be string")
        self.player1 = Player(player1, num_cards)
        self.player2 = Player(player2, num_cards)
        if num_cards > 26 or num_cards < 10:                                            # Number of cards each player
            num_cards = 26                                                              # can't exceed 26 or below 10 cards
        self.num_cards = num_cards
        self.new_game(self.num_cards)


    def new_game(self, num_cards):
        """create a new game"""
        if len(self.player1.pack_player) == 0 and len(self.player2.pack_player) == 0:   # number of cards cant be 0
            self.pack.cards_shuffle()
            for i in range(num_cards):
                self.player1.pack_player.append(self.pack.deal_one())                   # give players random cards,
            for i in range(num_cards):                                                  # number of cards is set by the user
                self.player2.pack_player.append(self.pack.deal_one())
        else:
            print("error massage")
            raise TypeError("the player's pack is not empty")

    def get_winner(self):
        """The winner of the game is the player with most cards"""
        if len(self.player1.pack_player) > len(self.player2.pack_player):
            return self.player1
        if len(self.player1.pack_player) < len(self.player2.pack_player):
            return self.player2
        if len(self.player1.pack_player) == len(self.player2.pack_player):
            return None