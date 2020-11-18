from rest_framework import serializers

from trello import models


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Card
        fields = (
            'name',
            'description',
            'column',
        )


class ColumnSerializer(serializers.ModelSerializer):

    cards = CardSerializer(many=True, read_only=True)

    class Meta:
        model = models.Column
        fields = (
            'id',
            'board',
            'name',
            'cards',
        )


class BoardSerializer(serializers.ModelSerializer):

    columns = ColumnSerializer(many=True, read_only=True)

    class Meta:
        model = models.Board
        fields = (
            'id',
            'name',
            'columns',
        )
