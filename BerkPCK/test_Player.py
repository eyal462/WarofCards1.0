from unittest import TestCase
from Player import Player
from Card import Card
import Deck_of_Cards
from Deck_of_Cards import Deck_of_Cards
from mock import patch


class TestPlayer(TestCase):

    def setUp(self):
        self.card = Card(1, 2)
        self.player = Player("eyal", 26)
        self.pack = Deck_of_Cards

    def test__init__(self):
        """test the initialize of player"""
        self.assertEqual(self.player.name, "eyal")
        self.assertEqual(self.player.num_of_cards, 26)

    def test_set_hand(self):
        """test for correct number of cards"""
        for i in range(0, 10):                  # if it's lower than 10,
            player = Player("Eyal", i)          # its become the default (26)
            self.assertEqual(player.num_of_cards, 26)

        for i in range (10, 27):                # if it's between 10 - 26 cards,
            player = Player("Eyal", i)
            self.assertEqual(player.num_of_cards, i)

        for i in range(27, 100):                # if it's above 26,
            player = Player("Eyal", i)
            self.assertEqual(player.num_of_cards, 26)

    @patch('random.choice')
    def test_get_card(self, mock_random_choice):
        """Test get_card, check if its return a random number from
        players pack and if it's update the number of cards the player had"""
        player = Player("eyal", 26)
        card = Card(12, 4)
        player.pack_player.append(card)
        mock_random_choice.return_value = Card(12, 4)
        card = player.get_card()
        self.assertEqual(card.value, 12)
        self.assertEqual(card.suit, 4)
        self.assertEqual(player.num_of_cards, 25)
    def test_add_card(self):
        """test that any card can be in player's pack"""
        for i in range(1, 14):
            for j in range(1, 5):
                card = Card(i, j)
                self.player.pack_player.append(card)
                self.assertEqual(self.player.pack_player[-1], card)