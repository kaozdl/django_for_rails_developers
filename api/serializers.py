from rest_framework import serializers

from trello import models


class BoardSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Board
        fields = (
            'id',
            'name',
        )
