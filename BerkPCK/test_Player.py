from unittest import TestCase
from Player import Player
from Card import Card
import Deck_of_Cards


class TestPlayer(TestCase):

    def setUp(self):
        self.card = Card(1, 2)
        self.player = Player("eyal", 26)
        self.pack = Deck_of_Cards
        self.player.pack_player = self.pack

    def test_set_hand(self):
        """test for correct number of cards"""
        for i in range(0, 10):                  # if it's lower than 10,
            player = Player("Eyal", i)          # its become the default (26)
            self.assertEqual(player.num_of_cards, 26)

    def test_get_card(self):
        # self.player.set_hand(self.pack)
        # self.assertEqual(self.player.get_card(), 1)         # check if its only 1 card
        # self.assertIsInstance(self.player.get_card(), Card) # check if its a card
        # self.assertEqual(len(self.player.pack_player), 25)
        self.player.set_hand(self.pack)
        self.assertIsInstance(self.player.get_card(), Card)
        self.assertEqual(len(self.player.pack_player), 25)

    def test_add_card(self):
        card = Card(5, 2)
        self.assertEqual(self.player.pack_player, 26)