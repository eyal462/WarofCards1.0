from unittest.mock import mock_open
from Card import Card
import unittest
from unittest import TestCase
import mock
from mock import patch


class TestCard(TestCase):


    def test_gt(self):
        """Test the __gt__ method"""
        card1 = Card(7, 2)
        card2 = Card(2, 1)
        card3 = Card(2, 4)
        self.assertTrue(card1 > card2)
        self.assertFalse(card2 > card1)  # card 2 is weaker than card 1
        self.assertTrue(card3 > card2)

    def test_eq(self):
        """Test the __eq__ method"""
        card1 = Card(1, 1)
        card2 = Card(1, 1)
        card3 = Card(2, 1)
        self.assertTrue(card1 == card2)
        self.assertFalse(card1 == card3)