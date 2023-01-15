from unittest import TestCase
from Player import Player
from CardGame import CardGame
import mock
from Card import Card
from Deck_of_Cards import Deck_of_Cards
from mock import patch


class TestCardGame(TestCase):

    def setUp(self):
        self.cardgame = CardGame("eyal", "lior", 26)

    def test_new_game(self):
        self.cardgame.new_game(26)

    @patch('BerkPCK.Deck_of_Cards.Deck_of_Cards.cards_shuffle')
    @patch('BerkPCK.Deck_of_Cards.Deck_of_Cards.deal_one')
    def test_new_game(self, mock_deal_one, mock_cards_shuffle):
        player1 = "eyal"
        player2 = "lior"
        game = CardGame(player1, player2, 4)
        game.new_game(4)
        mock_cards_shuffle.assert_called_once()
        self.assertEqual(mock_deal_one.call_count, 8)
        self.assertEqual(len(game.player1.pack_player), 4)
        self.assertEqual(len(game.player2.pack_player), 4)

    def test_get_winner(self):
        """test for get_winner"""
        cardgame = CardGame("eyal", "lior", 26)

        """test for player 1 wins"""
        cardgame.player1.num_of_cards = 10
        cardgame.player2.num_of_cards = 5
        self.assertEqual(cardgame.get_winner(), cardgame.player1)

        """test for player 2 wins"""
        cardgame.player1.num_of_cards = 2
        cardgame.player2.num_of_cards = 15
        self.assertEqual(cardgame.get_winner(), cardgame.player2)

        """test for tie"""
        cardgame.player1.num_of_cards = 15
        cardgame.player2.num_of_cards = 15
        self.assertEqual(cardgame.get_winner(), None)

        """test for tie"""
        cardgame.player1.num_of_cards = 0
        cardgame.player2.num_of_cards = 0
        self.assertEqual(cardgame.get_winner(), None)
