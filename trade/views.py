from typing import io

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from trade.models import Trade
from trade.serializers import TradeSerializer


class TradeViewSet(ViewSet):
    @action(detail=False, methods=['POST'])
    def verify(self, request):
        trade_serializer = TradeSerializer(data=request.data)
        if trade_serializer.is_valid():
            print('entrou aqui em!')
            print(trade_serializer.validated_data)
            trade = Trade(right_side=str(trade_serializer.validated_data['right_side']),
                          left_side=str(trade_serializer.validated_data['left_side']))

            trade_serializer.validated_data['result'] = trade.is_fair()

            return Response(trade_serializer.validated_data, status=status.HTTP_200_OK)
        return Response(trade_serializer.errors, status=status.HTTP_200_OK)



