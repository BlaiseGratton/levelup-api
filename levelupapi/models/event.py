from django.db import models


class Event(models.Model):
    game = models.ForeignKey('levelupapi.Game', 
                             on_delete=models.CASCADE,
                             related_name='events')
    organizer = models.ForeignKey('levelupapi.Gamer',
                             on_delete=models.CASCADE,
                             related_name='hosted_games')
    date = models.DateTimeField()
    title = models.CharField(max_length=100)
    attendees = models.ManyToManyField('levelupapi.Gamer', related_name='attending')
    description = models.CharField(max_length=400)
    time = models.TimeField()
