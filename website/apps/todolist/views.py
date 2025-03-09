import json
from rest_framework.response import Response
from rest_framework.views import APIView
from website.apps.todolist import serializers
from website.apps.todolist.models import Task

class GetTasks(APIView):
    
    def get(self, request):
        
        objs = Task.objects.all().order_by('id')
        return Response({
            'status': True,
            'status_code': 200,
            'message': 'Tasks list retrived',
            'data': serializers.TaskSerializer(objs, many=True, context={'request': request}).data,
        })
        
class CreateTask(APIView):
    
    def post(self, request):
        name = request.POST.get('name', None)
        completed = request.POST.get('completed', False)
        print(completed)
        if not name:
            return Response({
                'status_code': 400,
                'message': 'Name is missing',
            })
        task = Task.objects.create(name=name, completed=completed)
        return Response({
            'status_code': 200,
            'message': 'Task created',
            'data': str(task.id)
        })
        
class DeleteTask(APIView):
    
    def post(self, request):
        task_id = request.POST.get('task_id', None)
        if not task_id:
            return Response({
                'status_code': 400,
                'message': 'task id is missing',
            })
        Task.objects.filter(id=task_id).delete()
        return Response({
            'status_code': 200,
            'message': 'Task deleted',
        })
        
class EditTask(APIView):
    
    def post(self, request):
        task_id = request.POST.get('task_id', None)
        task = Task.objects.filter(id=task_id).first()
        name = request.POST.get('name', None)
        completed = request.POST.get('completed', None)
        if not task:
            return Response({
                'status_code': 400,
                'message': 'data is missing',
            })
        if name:
            task.name = name
        if completed == 'switch':
            task.completed = not task.completed
        task.save()
        return Response({
            'status_code': 200,
            'message': 'Task edited',
        })