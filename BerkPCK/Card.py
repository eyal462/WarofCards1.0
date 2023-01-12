class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __repr__(self):
        card = ""
        suit = ""
        if self.value == 1 or self.value >= 11:
            if self.value == 1:
                card = "ACE (1)"
            if self.value == 11:
                card = "JACK (11)"
            if self.value == 12:
                card = "QUEEN (12)"
            if self.value == 13:
                card = "KING (13)"

        if self.suit == 1:
            suit = "DIMOND (1)"
        if self.suit == 2:
            suit = "SPADE (2)"
        if self.suit == 3:
            suit = "HEART (3)"
        if self.suit == 4:
            suit = "CLUB (4)"
        if 1 < self.value < 11:
            return f"{self.value}, {suit}"
        else:
            return f"{card}, {suit}"


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