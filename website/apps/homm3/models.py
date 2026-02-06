from django.db import models

# Create your models here.

class Player(models.Model):
    discord_name = models.CharField(max_length=255)
    lobby_name = models.CharField(max_length=255)
    twitch_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'homm3_player'
        
    def __str__(self):
        return self.discord_name
        
class Match(models.Model):
    player1 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player1')
    player2 = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='matches_as_player2')
    result = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.player1.__str__() + ' VS ' + self.player2.__str__()