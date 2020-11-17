from rest_framework import serializers

from trello import models


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Board
        fields = (
            'id',
            'name',
        )


class ColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Column
        fields = (
            'id',
            'board',
            'name',
        )


class CardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Card
        fields = (
            'name',
            'description',
            'column',
        )
