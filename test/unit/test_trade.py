import unittest
from unittest import mock

from test.util.test_utils import create_default_trade
from trade.models import Trade, Pokemon


class TradeTestCase(unittest.TestCase):
    global trade

    def setUp(self):
        global trade
        trade = create_default_trade()

    @mock.patch('trade.fairness.Fairness.is_fair')
    def test_is_fair(self, mock_fairness):
        mock_fairness.return_value = True
        self.assertEqual('This trade is fair!', trade.is_fair())

    def test_get_right_side(self):
        self.assertIn('charmander', str(trade.get_right_side()))

    def test_get_left(self):
        self.assertIn('pikachu', str(trade.get_left_side()))
