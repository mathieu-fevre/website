from django.urls import path
from . import views

app_name='todolist'
urlpatterns = [
    path('api/get_tasks', views.get_tasks.as_view(), name='get_tasks'),

]