import random
from Card import Card

class Player:
    def __init__(self, name, num_of_cards):
        self.name = name
        self.pack_player = []                               # list of cards for player
        if num_of_cards > 26 or num_of_cards < 10:          # number of cards for player
            num_of_cards = 26
        self.num_of_cards = num_of_cards


    def __str__(self):
        return f"{self.name.upper()}"

    def set_hand(self, pack):
        """give player random cards by pack of 52 cards, number of cards is set by the user"""
        for i in range(self.num_of_cards):
            self.pack_player.append(pack.deal_one())
            self.num_of_cards += 1

    def get_card(self):
        """returns random card form player's pack of cards"""
        card = random.choice(self.pack_player)
        self.pack_player.remove(card)
        self.num_of_cards -= 1
        return card

    def add_card(self, card):
        self.pack_player.append(card)
        self.num_of_cards += 1