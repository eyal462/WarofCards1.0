from unittest import TestCase
from CardGame import CardGame
from Card import Card
import mock


class TestCardGame(TestCase):

    def setUp(self):
        self.cardgame = CardGame("eyal", "lior", 26)

    def test_new_game(self):
        """test for new game, test its gives a total of number of cards set by the user"""
        with mock.patch('Deck_of_Cards.Deck_of_Cards.cards_shuffle') as mock_cards_shuffle, \
                mock.patch('Deck_of_Cards.Deck_of_Cards.deal_one') as mock_deal_one:
            cardgame1 = CardGame("eyal", "lior", 26)
            self.assertEqual(mock_cards_shuffle.call_count, 1)                                  # check if its only shuffle once
            self.assertEqual(mock_deal_one.call_count, 52)                                      # check if its give 52 cards
            mock_card = Card(7, 2)
            mock_deal_one.return_value = mock_card                                              # using mock to get card from deal_one
            cardgame2 = CardGame("eyal", "lior", 26)
            card = cardgame2.player1.get_card()                                                 # card = mock_card = (7, 2)
            self.assertEqual(card, mock_card)

    def test_get_winner(self):
        """test for get_winner"""
        cardgame = CardGame("eyal", "lior", 26)
        card1 = Card(1, 2)                                                                      # creating cards to add to each player
        card2 = Card(2, 1)                                                                      # to modify later according to the test
        card3 = Card(5, 1)
        card4 = Card(7, 3)
        card5 = Card(8, 4)
        card6 = Card(1, 2)
        card7 = Card(12, 1)
        card8 = Card(10, 3)
        cardgame.player1.pack_player = [card1, card2, card3, card4]
        cardgame.player2.pack_player = [card5, card6, card7, card8]

        """test for tie"""                                                                      # player 1 has 4 cards
        self.assertEqual(cardgame.get_winner(), None)                                           # player 2 has 4 cards ==> tie

        """test for player 1 wins"""
        cardgame.player2.pack_player.remove(card5)                                              # player 1 has 4
        self.assertEqual(cardgame.get_winner(), cardgame.player1)                               # player 2 has 3 ==> player 1 wins

        """test for player 2 wins"""
        cardgame.player1.pack_player.remove(card4)                                              # player 1 has 3
        cardgame.player1.pack_player.remove(card3)                                              # player 2 has 2 ==> player 2 wins
        self.assertEqual(cardgame.get_winner(), cardgame.player2)

        """test for empty cards"""
        cardgame.player1.pack_player = []
        cardgame.player2.pack_player = []
        self.assertEqual(cardgame.get_winner(), None)
