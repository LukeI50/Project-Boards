from django.urls import path
from . import views


urlpatterns = [
    path('collaborator/', views.CollaboratorList.as_view(), name='collaborator'),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name = 'project_detail'),
    path('<slug:slug>/delete_task/<int:task_id>', views.task_delete, name='task_delete'),
    path('<slug:slug>/edit_task/<int:task_id>', views.task_edit, name='task_edit'),
    path('', views.ProjectsList.as_view(), name='home'),
]