from rest_framework import status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from trade.models import Trade
from trade.serializers import TradeSerializer


class TradeViewSet(ViewSet):
    @action(detail=False, methods=['POST'])
    def verify(self, request):
        trade_serializer = TradeSerializer(data=request.data)
        if trade_serializer.is_valid():
            trade = Trade(right_side=str(trade_serializer.validated_data['right_side']),
                          left_side=str(trade_serializer.validated_data['left_side']))

            trade_serializer.validated_data['result'] = trade.is_fair()

            return Response(trade_serializer.validated_data, status=status.HTTP_200_OK)
        return Response(trade_serializer.errors, status=status.HTTP_200_OK)

    @action(detail=False, methods=['POST'])
    def save(self, request):
        trade_serializer = TradeSerializer(data=request.data)
        if trade_serializer.is_valid():
            trade = Trade(right_side=str(trade_serializer.validated_data['right_side']),
                          left_side=str(trade_serializer.validated_data['left_side']))

            trade.save()
            return Response(trade_serializer.validated_data, status=status.HTTP_200_OK)
        return Response(None, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        historical_data = Trade.objects.all()
        data = {
            "trades": []
        }
        for item in historical_data:
            data['trades'].append(item.toJson())
        return Response(data, status=status.HTTP_200_OK)
