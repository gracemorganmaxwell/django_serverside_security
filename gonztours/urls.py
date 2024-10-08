from django.urls import path, include
from . import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('accounts/', include('accounts.urls')),
    path('tours/', include('tours.urls')),
    path('agents/', include('agents.urls')),

]
