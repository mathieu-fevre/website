from rest_framework import serializers
from website.apps.poker.models import Blinds, GameType, Room, Session
from website.apps.poker.utils import datetime_to_str

class SessionSerializer(serializers.ModelSerializer):
    winnings = serializers.SerializerMethodField('get_winnings')
    blinds = serializers.SerializerMethodField('get_blinds')
    game_type = serializers.SerializerMethodField('get_game_type')
    room = serializers.SerializerMethodField('get_room')
    start = serializers.SerializerMethodField('get_start')
    end = serializers.SerializerMethodField('get_end')
    
    def get_winnings(self, obj):
        if obj.money_in and obj.money_out:
            return obj.money_out - obj.money_in
        return None
    
    def get_blinds(self, obj):
        if obj.blinds:
            return obj.blinds.name
        return None
    
    def get_game_type(self, obj):
        if obj.game_type:
            return obj.game_type.name
        return None
    
    def get_room(self, obj):
        if obj.room:
            return obj.room.name
        return None

    def get_start(self, obj):
        return datetime_to_str(obj.start)

    def get_end(self, obj):
        return datetime_to_str(obj.end)
    
    class Meta:
        model = Session
        fields = ['id', 'start', 'end', 'money_in', 'money_out', 'winnings', 'game_type', 'blinds', 'room']
        
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'name', 'sort']
        
class BlindsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blinds
        fields = ['id', 'name', 'sort']
        
class GameTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameType
        fields = ['id', 'name', 'sort']