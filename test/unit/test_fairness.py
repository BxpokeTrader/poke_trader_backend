from unittest import mock

from django.test import TestCase

from test.util.test_utils import create_default_trade, mocked_requests_get
from trade.fairness import Fairness
from trade.models import Trade


class FairnessTestCase(TestCase):
    global trade
    global fairness

    def setUp(self):
        global trade
        global fairness
        trade = create_default_trade()
        fairness = Fairness(experience_weight=1)

    def test_get_experience_amount(self):
        global trade
        global fairness
        self.assertEqual(174, fairness.get_experience_amount(trade.left_side))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_count_locals(self, mock_get):
        self.assertEqual(3, fairness.count_locals(trade.left_side[0]))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_get_rarity(self, mock_get):
        self.assertEqual(6, fairness.get_rarity_amount(trade.left_side))

    def test_is_fair_only_experience(self):
        self.assertTrue(fairness.is_fair(trade))
        pokemon1 = {'name': 'pikachu', 'base_experience': 112, 'image': 'url'}
        pokemon2 = {'name': 'charmander', 'base_experience': 62, 'image': 'url'}
        trade2 = Trade()
        trade2.left_side = [pokemon1]
        trade2.right_side = [pokemon2]

        self.assertFalse(fairness.is_fair(trade2))
