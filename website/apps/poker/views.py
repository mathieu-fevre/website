from datetime import datetime
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from website.apps.poker import serializers
from website.apps.poker.models import Blinds, GameType, Room, Session
from django.utils.timezone import make_aware

class GetSessions(APIView):

    def get(self, request):
        sessions = Session.objects.all()
        content = {
            'data': serializers.SessionSerializer(sessions, many=True, context={'request': request}).data
        }
        return Response(content, status=status.HTTP_200_OK)
        
class AddSession(APIView):

    def post(self, request):
        start = request.POST.get('start', None)
        end = request.POST.get('end', None)
        if start:
            start = make_aware(datetime.strptime(start, '%Y%m%d %H%M'))
        if end:
            end = make_aware(datetime.strptime(end, '%Y%m%d %H%M'))
        money_in = request.POST.get('money_in', None)
        money_out = request.POST.get('money_out', None)
        game_type_id = request.POST.get('game_type_id', None)
        blinds_id = request.POST.get('blinds_id', None)
        room_id = request.POST.get('room_id', None)
        game_types = GameType.objects.filter(id=game_type_id)
        blindss = Blinds.objects.filter(id=blinds_id)
        roomss = Room.objects.filter(id=room_id)
        if game_types:
            game_type = game_types.first()
        else:
            game_type = None
        if blindss:
            blinds = blindss.first()
        else:
            blinds = None
        if roomss:
            room = roomss.first()
        else:
            room = None
        Session.objects.create(start=start, end=end, money_in=money_in, money_out=money_out, game_type=game_type, blinds=blinds, room=room)
        content = {}
        return Response(content, status=status.HTTP_200_OK)
    
class DeleteSession(APIView):

    def post(self, request):
        session_id = request.POST.get('session_id', None)
        Session.objects.filter(id=session_id).delete()
        content = {}
        return Response(content, status=status.HTTP_200_OK)

class EditSession(APIView):

    def post(self, request):
        session_id = request.POST.get('session_id', None)
        Session.objects.filter(id=session_id).first()
        content = {}
        return Response(content, status=status.HTTP_200_OK)
    
class BlindsList(APIView):

    def get(self, request):
        blinds = Blinds.objects.all()
        content = {
            'data': serializers.BlindsSerializer(blinds, many=True, context={'request': request}).data
        }
        return Response(content, status=status.HTTP_200_OK)
    
class GameTypeList(APIView):

    def get(self, request):
        game_type = GameType.objects.all()
        content = {
            'data': serializers.GameTypeSerializer(game_type, many=True, context={'request': request}).data
        }
        return Response(content, status=status.HTTP_200_OK)
    
class RoomList(APIView):

    def get(self, request):
        rooms = Room.objects.all()
        content = {
            'data': serializers.RoomSerializer(rooms, many=True, context={'request': request}).data
        }
        return Response(content, status=status.HTTP_200_OK)