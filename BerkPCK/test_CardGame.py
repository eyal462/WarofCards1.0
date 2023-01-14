from unittest import TestCase
from Player import Player
from CardGame import CardGame
import mock
from Card import Card


class TestCardGame(TestCase):

    def setUp(self):
        self.player1 = Player("Eyal", 20)
        self.player2 = Player("lior", 26)
        self.card_game = CardGame(self.player1, self.player2, 26)
    def test_new_game(self):
        self.fail()
    @mock.patch('BerkPCK.CardGame.CardGame')
    def test_get_winner(self):
        card1 = Card(1, 2)
        card2 = Card(2, 2)
        card3 = Card(3, 2)
        card4 = Card(4, 2)
        card5 = Card(5, 2)
        player1 = self.player1
        player2 = self.player2
        mock_player.pack_player = [card1, card2, card3]
        cg = CardGame(player1, player2, 26)
        self.assertTrue(self.card_game.get_winner(), self.player2)

