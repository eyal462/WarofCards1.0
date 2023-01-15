class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        value = {1: "ACE (1)", 11: "JACK (11)", 12: "QUEEN (12)", 13: "KING (13)"}
        suit = {1: "DIMOND (1)", 2: "SPADE (2)", 3: "HEART (3)", 4: "CLUB (4)"}
        card = value.get(self.value, self.value)                            # the get method search in the dicticnery keys
        suit = suit.get(self.suit)                                          # if self.value found in key it returns value
        return f"{card}, {suit}"                                            # if not, return self.value

    def __gt__(self, other):
        """compare the cards, if current card is higher from ther other, it returns True"""
        if self.value == 1 and other.value != 1:   # ACE is the highest card
            return True
        if self.value != 1 and other.value == 1:
            return False
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