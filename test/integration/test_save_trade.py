import unittest

from rest_framework import status
from rest_framework.test import APIClient

from trade.models import Trade


class SaveTradeTest(unittest.TestCase):
    global client

    def setUp(self):
        global client
        client = APIClient()
        Trade.objects.all().delete()

    def test_save_trade(self):
        response = client.post('http://localhost:8000/trade/save/',
                               {
                                   "right_side": [
                                       {"name": "teste1", "base_experience": 200
                                        }
                                   ], "left_side": [
                                   {"name": "teste1", "base_experience": 200
                                    }
                               ], "result": ""
                               },
                               format='json')
        assert response.status_code == status.HTTP_200_OK
        trades = Trade.objects.all()
        assert len(trades) == 1

    def test_save_trade_wrong_format(self):
        response = client.post('http://localhost:8000/trade/save/',
                               {
                                   "right_side": [
                                       {"name": "teste1", "base_experience": 200
                                        }
                                   ], "result": ""
                               },
                               format='json')

        assert response.status_code == status.HTTP_400_BAD_REQUEST
        trades = Trade.objects.all()
        assert len(trades) == 0
