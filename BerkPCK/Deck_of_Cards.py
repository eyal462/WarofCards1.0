from Card import Card
import random

class Deck_of_Cards:
    def __init__(self):
        """initialize the deck of cards, create a list of 52 diffrent cards (13 cards, 4 suits each card)"""
        self.pack = []
        for i in range(1, 14):
            for j in range(1, 5):
                card = Card(i, j)
                self.pack.append(card)


    def cards_shuffle(self):
        """randomize the order of the deck of cards"""
        return random.shuffle(self.pack)

    def deal_one(self):
        """get random card from the deck of cards"""
        card = random.choice(self.pack)
        self.pack.remove(card)
        return card

