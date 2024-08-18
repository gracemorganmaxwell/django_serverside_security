from django.urls import path
from . import views

urlpatterns = [
    path('', views.agent_list, name='agent_list'),  # List all agents
    path('<int:agent_id>/', views.agent_detail, name='agent_detail'),  # View specific agent details
]
