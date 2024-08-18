from django.urls import path
from . import views

urlpatterns = [
    path('', views.tour_list, name='tour_list'),  # List all tours
    path('<int:tour_id>/', views.tour_detail, name='tour_detail'),  # View specific tour details
]
