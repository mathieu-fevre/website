import json
from rest_framework.response import Response
from rest_framework.views import APIView
from website.apps.todolist import serializers
from website.apps.todolist.models import Task

class get_tasks(APIView):
    
    def get(self, request):
        
        objs = Task.objects.all()
        return Response({
            'status': True,
            'status_code': 200,
            'message': 'Tasks list retrived',
            'data': serializers.TaskSerializer(objs, many=True, context={'request': request}).data,
        })
        
    def post(self, request):
        payload = json.loads(request.body)
        name = payload.get('name', None)
        completed = payload.get('completed', False)
        if not name:
            return Response({
                'status_code': 400,
                'message': 'Name is missing',
            })
        Task.objects.create(name=name, completed=completed)
        return Response({
            'status_code': 200,
            'message': 'Task created',
        })
        