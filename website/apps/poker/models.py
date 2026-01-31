from django.db import models
from django.db.models import Max

# Create your models here.

def get_default_room_sort():
    if not Room.objects.exists():
        return 1
    return Room.objects.aggregate(Max('sort'))['sort__max']+1

def get_default_gametype_sort():
    if not GameType.objects.exists():
        return 1
    return GameType.objects.aggregate(Max('sort'))['sort__max']+1

def get_default_gametype_sort():
    if not Blinds.objects.exists():
        return 1
    return Blinds.objects.aggregate(Max('sort'))['sort__max']+1

class Room(models.Model):
    name = models.CharField(max_length=255)
    sort = models.IntegerField(default=get_default_room_sort)
    
    class Meta:
        db_table = 'poker_room'
        ordering= ['sort']

    def __str__(self):
        return self.name
    
class GameType(models.Model):
    name = models.CharField(max_length=255)
    sort = models.IntegerField(default=get_default_gametype_sort)
    
    class Meta:
        db_table = 'poker_gametype'
        ordering= ['sort']

    def __str__(self):
        return self.name
    
class Blinds(models.Model):
    name = models.CharField(max_length=255)
    sort = models.IntegerField(default=get_default_gametype_sort)
    
    class Meta:
        db_table = 'poker_blinds'
        ordering= ['sort']

    def __str__(self):
        return self.name
    
class Session(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    money_in = models.IntegerField(blank=True, null=True)
    money_out = models.IntegerField(blank=True, null=True)
    game_type = models.ForeignKey(GameType, on_delete=models.SET_NULL, blank=True, null=True)
    blinds = models.ForeignKey(Blinds, on_delete=models.SET_NULL, blank=True, null=True)
    room = models.ForeignKey(Room, on_delete=models.SET_NULL, blank=True, null=True)