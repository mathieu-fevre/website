from django.urls import path
from . import views

app_name='poker'

urlpatterns = [
    path('api/get_sessions', views.GetSessions.as_view(), name='get_sessions'),
    path('api/add_session', views.AddSession.as_view(), name='add_sessions'),
    path('api/delete_session', views.DeleteSession.as_view(), name='delete_sessions'),
    path('api/blinds_list', views.BlindsList.as_view(), name='blinds_list'),
    path('api/room_list', views.RoomList.as_view(), name='rooms_list'),
    path('api/game_type_list', views.GameTypeList.as_view(), name='game_type_list'),
]