from django.db import models


class Game(models.Model):
    skill_level = models.IntegerField()
    gamer = models.ForeignKey('levelupapi.Gamer',
                              on_delete=models.CASCADE,
                              related_name='created_games')
    title = models.CharField(max_length=100)
    number_of_players = models.IntegerField()
    game_type = models.ForeignKey('levelupapi.GameType',
                                  on_delete=models.CASCADE,
                                  related_name='games')
    maker = models.CharField(max_length=100)