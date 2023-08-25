from django.urls import path
from . import views


urlpatterns = [
    path('', views.categories, name='categories'),
    path('agents', views.agents, name='agents'),
    path('create', views.createPost, name='create'),
    path('agentsingle/<int:agent_id>', views.single, name='single'),
    path('single/<int:listing_id>', views.findSingle, name='listingsingle'),
]
