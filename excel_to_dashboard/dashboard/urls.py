from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('home/', views.home),
    path('dashboard/<int:id>/', views.dashboard),
    path('delete_agents/', views.deleteAgents),
]
