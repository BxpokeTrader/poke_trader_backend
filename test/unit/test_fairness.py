from django.test import TestCase

from test.util.test_utils import create_default_trade
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

    def test_fairness_same_pokemon(self):
        global trade
        global fairness
        self.assertEqual(174, fairness.get_experience_amount(trade.left_side))
