from django.urls import path
from . import views


urlpatterns = [
    path('', views.ProjectsList.as_view(), name='home'),
    path('collaborator/', views.CollaboratorList.as_view(), name='collaborator'),
    path('<slug:slug>/', views.project_detail, name = 'project_detail'),
]