
import unittest

from rest_framework import status
from rest_framework.test import APIClient


class VerifyTradeTestCase(unittest.TestCase):
    global client

    def setUp(self):
        global client
        client = APIClient()

    def test_verify_unfair_trade(self):
        response = client.post('http://localhost:8000/trade/verify/',
                               {
                                   "right_side": [
                                       {"name": "teste1", "base_experience": 200
                                        }
                                   ], "left_side": [
                                       {"name": "teste1", "base_experience": 400
                                        }
                                   ], "result": ""
                               },
                               format='json')
        assert response.status_code == status.HTTP_200_OK
        assert response.data['result'] == "This trade is unfair!"

    def test_verify_fair_trade(self):
        response = client.post('http://localhost:8000/trade/verify/',
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
        assert response.data['result'] == "This trade is fair!"
