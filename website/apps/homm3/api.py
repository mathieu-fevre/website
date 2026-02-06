from rest_framework.response import Response
from rest_framework.views import APIView
from website.apps.homm3.models import Player
from website.apps.homm3.serializers import PlayerSerializer
from django.http import JsonResponse
from rest_framework import status

class GetAllPlayers(APIView):
    
    def get(self, request):
        
        objs = Player.objects.all().order_by('id')
        return JsonResponse(PlayerSerializer(objs, many=True, context={'request': request}).data, safe=False)
    
class CreatePlayer(APIView):
    
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)

        if serializer.is_valid():
            player = serializer.save()
            return Response(
                PlayerSerializer(player).data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )