from django.urls import path
from . import views

app_name='todolist'
urlpatterns = [
    path('api/get_tasks', views.GetTasks.as_view(), name='get_tasks'),
    path('api/create_task', views.CreateTask.as_view(), name='create_task'),
    path('api/delete_task', views.DeleteTask.as_view(), name='delete_task'),
    path('api/edit_task', views.EditTask.as_view(), name='edit_task'),

]