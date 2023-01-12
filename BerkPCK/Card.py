class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        return f"CARD {self.value}, {self.suit}\n"

    def __gt__(self, other):
        """compare the cards, if current card is higher from ther other, it returns True"""
        if self.value > other.value:
            return True
        if self.value == other.value and self.suit > other.suit:
            return True
        else:
            return False


    def __eq__(self, other):
        """compare the card agaist another, if its the same one it returns True"""
        if self.value == other.value and self.suit == other.suit:
            return True
        else:
            return False