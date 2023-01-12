import random
from Card import Card

class Player:
    def __init__(self, name, num_of_cards):
        self.name = name
        self.pack_player = []
        if num_of_cards > 26 or num_of_cards < 10:
            num_of_cards = 26
        self.num_of_cards = num_of_cards

    def set_hand(self, pack):
        """give player random cards, number of cards is set by the user"""
        for i in range(self.num_of_cards):
            self.pack_player[i] = pack.deal_one()

    def get_card(self):
        """returns random card form player's pack of cards"""
        card = random.choice(self.pack_player)
        self.pack_player.remove(card)
        return card

    def add_card(self, card):
        self.pack_player.append(card)