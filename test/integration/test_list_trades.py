import json
import unittest

from rest_framework import status
from rest_framework.test import APIClient

from test.util.test_utils import create_default_trade, create_unfair_trade
from trade.models import Trade


class ListTradesTest(unittest.TestCase):
    global client

    def setUp(self):
        global client
        client = APIClient()

        fair_trade = create_default_trade()
        unfair_trade = create_unfair_trade()
        fair_trade.save()
        unfair_trade.save()

    def test_list_trades(self):
        response = client.get('http://localhost:8000/trade/', format='json')
        assert response.status_code == status.HTTP_200_OK
        response = json.loads(response.content)
        assert len(response['trades']) == 2

    def test_list_empty_historic(self):
        Trade.objects.all().delete()
        response = client.get('http://localhost:8000/trade/', format='json')
        assert response.status_code == status.HTTP_200_OK
        response = json.loads(response.content)
        assert len(response['trades']) == 0
