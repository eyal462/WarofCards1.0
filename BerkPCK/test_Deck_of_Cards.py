from unittest import TestCase
from Deck_of_Cards import Deck_of_Cards
from Card import Card

class TestDeck_of_Cards(TestCase):

    def setUp(self):
        self.deck_of_cards = Deck_of_Cards()
        self.list1 = Deck_of_Cards()            # original order of cards

    def test_init(self):
        """Test for the initialize of deck of cards
        check if it 52 cards and each card is actually card"""
        self.assertEqual(len(self.deck_of_cards.pack), 52)
        for i in range(len(self.deck_of_cards.pack)):
            self.assertIsInstance(self.deck_of_cards.pack[i], Card)



    def test_deal_one(self):
        """Test for if its a card and if its remove one from the pack"""
        self.assertIsInstance(self.deck_of_cards.deal_one(), Card)
        self.assertEqual(len(self.deck_of_cards.pack), 51)



    def test_shuffle(self):
        """check if the pack is orginzed diffrent from the original deck of cards"""
        self.deck_of_cards.cards_shuffle()
        self.assertFalse(self.deck_of_cards.pack == self.list1)