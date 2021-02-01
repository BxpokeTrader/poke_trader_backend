import json

from django.http import HttpResponse, JsonResponse
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from trade.models import Trade
from trade.serializers import TradeSerializer


class TradeViewSet(ViewSet):
    @action(detail=False, methods=['POST'])
    def verify(self, request):
        """
        Verify if a specific Trade is fair or not.
        It receive a POST request containing a Trade data in JSON format
        and return the same Trade with the result (is fair or not).
        """
        trade_serializer = TradeSerializer(data=request.data)
        if trade_serializer.is_valid():
            trade = Trade(right_side=trade_serializer.validated_data['right_side'],
                          left_side=trade_serializer.validated_data['left_side'])

            trade_serializer.validated_data['result'] = trade.is_fair()

            return Response(trade_serializer.validated_data, status=status.HTTP_200_OK)
        return Response(trade_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['POST'])
    def save(self, request):
        """
        Save a specific trade in database. It is done if the user accept the trade.
        It is used to populate the database with all trades that was made with PokeTrader.
        """
        trade_serializer = TradeSerializer(data=request.data)
        if trade_serializer.is_valid():
            trade = Trade(right_side=trade_serializer.validated_data['right_side'],
                          left_side=trade_serializer.validated_data['left_side'])
            trade.result = trade.is_fair()

            trade.save()
            return Response(trade_serializer.validated_data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        """
        List all trades that was verified by PokeTrader and was accepted by the user.
        """
        historical_data = Trade.objects.all()
        data = []
        for item in historical_data:
            data.append(item.toJson())
        result = {
            'trades': data
        }
        return JsonResponse(result, status=status.HTTP_200_OK, safe=False)
