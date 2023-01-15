from unittest import TestCase
from Card import Card
from mock import patch
from CardGame import CardGame


class TestPlayer(TestCase):

    def setUp(self):
        self.card = Card(1, 2)
        self.cardgame = CardGame("eyal", "lior", 26)
        self.cardgame2 = CardGame("eyal", "lior", 15)
        self.cardgame3 = CardGame("eyal", "lior", 0)  # lower than 10
        self.cardgame4 = CardGame("eyal", "lior", 40)  # above 26

    def test__init__(self):
        """test the initialize of player"""
        self.assertEqual(self.cardgame.player1.name, "eyal")
        self.assertEqual(len(self.cardgame.player1.pack_player), 26)
        self.assertEqual(self.cardgame.player2.name, "lior")
        self.assertEqual(len(self.cardgame.player2.pack_player), 26)
        self.assertEqual(len(self.cardgame2.player1.pack_player), 15)
        self.assertEqual(len(self.cardgame3.player1.pack_player),
                         26)  # if it's set LOWER than 0, the program set it to 26
        self.assertEqual(len(self.cardgame4.player1.pack_player),
                         26)  # if it's set HIGHER than 26, the program set it to 26

    def test_set_hand(self):
        """test for correct number of cards"""

        for i in range(0, 10):  # if it's lower than 10,
            cardgame = CardGame("eyal", "lior", i)  # its become the default (26)
            self.assertEqual(len(cardgame.player1.pack_player), 26)

        for i in range(10, 27):  # if it's between 10 - 26 cards,
            cardgame = CardGame("eyal", "lior", i)
            self.assertEqual(len(cardgame.player1.pack_player), i)

        for i in range(27, 1000):  # if it's above 26,
            cardgame = CardGame("eyal", "lior", i)  # it's become 26
            self.assertEqual(len(cardgame.player1.pack_player), 26)

    @patch('random.choice')
    def test_get_card(self, mock_random_choice):
        """Test get_card, check if its return a random number from
        players pack and if it's update the number of cards the player had"""
        card = Card(10, 2)  # card to mock
        self.cardgame.player1.pack_player.append(card)  # player now have 27 cards
        self.assertEqual(len(self.cardgame.player1.pack_player), 27)
        mock_random_choice.return_value = Card(10, 2)  # mocking the card
        card1 = self.cardgame.player1.get_card()  # should now remove 1 card from players pack
        self.assertEqual(card1.value, 10)
        self.assertEqual(card1.suit, 2)
        self.assertEqual(len(self.cardgame.player1.pack_player), 26)  # the player should have 26 cards

    def test_add_card(self):
        """test that any card can be in player's pack"""
        for i in range(1, 14):
            for j in range(1, 5):
                card = Card(i, j)
                self.cardgame.player1.pack_player.append(card)
                self.assertEqual(self.cardgame.player1.pack_player[-1], card)  # check if each card we added
                # is the right card
