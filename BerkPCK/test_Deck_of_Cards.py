from unittest import TestCase
from Deck_of_Cards import Deck_of_Cards
from Card import Card

class TestDeck_of_Cards(TestCase):

    def setUp(self):
        self.pack = Deck_of_Cards()

    def test_init(self):
        """Test for the initialize of deck of cards
        check if it 52 cards and each card is actually card"""
        self.assertEqual(len(self.pack.pack), 52)
        for i in range(len(self.pack.pack)):
            self.assertIsInstance(self.pack.pack[i], Card)



    def test_deal_one(self):
        """Test for if its a card and if its remove one from the pack"""
        self.assertIsInstance(self.pack.deal_one(), Card)
        self.assertEqual(len(self.pack.pack), 51)

    def test_shuffle(self):
        """check if the pack is orginzed diffrent from the original deck of cards"""
        list1 = self.pack.pack
        self.pack.cards_shuffle()
        self.assertNotEqual(self.pack.pack, list1)