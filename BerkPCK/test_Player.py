from unittest import TestCase
from Player import Player
from Card import Card


class TestPlayer(TestCase):

    def setUp(self):
        self.player = Player("eyal", 26)


    def test_set_hand(self):
        """test for correct number of cards"""
        for i in range(0, 10):                  # if it's lower than 10,
            player = Player("Eyal", i)          # its become the default (26)
            self.assertEqual(player.num_of_cards, 26)

    def test_get_card(self):
        self.assertEqual(self.player.get_card(), 1)         # check if its only 1 card
        self.assertIsInstance(self.player.get_card(), Card) # check if its a card
        self.assertEqual(self.player.pack_player, 25)


    def test_add_card(self):
        self.fail()
