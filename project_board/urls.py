from django.urls import path
from . import views


urlpatterns = [
    path('', views.determineView, name="greeting"),
    path('collaborator/', views.CollaboratorList.as_view(), name='collaborator'),
    path('projects/', views.ProjectsList.as_view(), name='home'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name = 'project_detail'),
    path('<slug:slug>/edit_task/<int:task_id>', views.task_edit, name='task_edit'),
]