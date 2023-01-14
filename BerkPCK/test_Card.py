from unittest.mock import mock_open
from Card import Card
import unittest
from unittest import TestCase
import mock
from mock import patch


class TestCard(TestCase):

    @mock.patch('BerkPCK.Card.Card')
    def test_gt(self, mock_card):
        """Test the __gt__ method"""
        card1 = Card(7, 2)
        card2 = Card(2, 1)
        card3 = Card(-2, -4)
        mock_card.value = 1
        mock_card.suit = 1
        self.assertTrue(card1 > card2)
        self.assertFalse(card2 > card1)
        self.assertFalse(card3 > card2)

    @mock.patch('BerkPCK.Card.Card')
    def test_eq(self, mock_card):
        """Test the __eq__ method"""
        card1 = Card(1, 1)
        card2 = Card(1, 1)
        card3 = Card(2, 1)
        mock_card.value = 1
        mock_card.suit = 2
        self.assertTrue(card1 == card2)
        self.assertFalse(card1 == card3)