from rest_framework import viewsets

from trello import models
from api import serializers
# Create your views here.
class BoardViewSet(viewsets.ModelViewSet):

    queryset = models.Board.objects.prefetch_related('columns', 'columns__cards')
    serializer_class = serializers.BoardSerializer


class ColumnViewSet(viewsets.ModelViewSet):

    queryset = models.Column.objects.prefetch_related('cards')
    serializer_class = serializers.ColumnSerializer


class CardViewSet(viewsets.ModelViewSet):

    queryset = models.Card.objects.all()
    serializer_class = serializers.CardSerializer
