from rest_framework import viewsets

from trello import models
from api import serializers
# Create your views here.
class BoardViewSet(viewsets.ModelViewSet):

    queryset = models.Board.objects.all()
    serializer_class = serializers.BoardSerializer
