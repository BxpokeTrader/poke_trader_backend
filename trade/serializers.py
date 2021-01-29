from rest_framework import serializers


class TradeSerializer(serializers.Serializer):
    right_side = serializers.ListField()
    left_side = serializers.ListField()
    result = serializers.CharField(allow_blank=True)


class PokemonSerializer(serializers.Serializer):
    name = serializers.CharField()
    base_experience = serializers.IntegerField()
