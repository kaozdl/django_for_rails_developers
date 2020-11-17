from django.db import models

# Create your models here.
class Board(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} - {self.id}"


class Column(models.Model):

    name = models.CharField(max_length=200)
    board = models.ForeignKey(
        Board,
        on_delete=models.CASCADE,
        related_name='columns', # <- direct equivalent to has_many :columns
    )


class Card(models.Model):

    name = models.CharField(max_length=200)
    description = models.TextField()

    column = models.ForeignKey(
        Column,
        on_delete=models.CASCADE,
        related_name='cards',
    )
