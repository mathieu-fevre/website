from rest_framework import serializers
from website.apps.homm3.models import Player

class PlayerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Player
        fields = ('id', 'discord_name', 'lobby_name', 'twitch_name')
        read_only_fields = ('id', 'created_at')