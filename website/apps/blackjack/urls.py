from django.urls import path
from . import views

app_name='blackjack'
urlpatterns = [
    path('display_basic_strategy', views.display_basic_strategy, name='display_basic_strategy'),
    path('compare/results', views.compare_results, name='compare_results'),
    path('compare/add', views.compare_add, name='compare_add'),
]