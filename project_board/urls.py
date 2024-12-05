from django.urls import path
from . import views


urlpatterns = [
    path('projects/', views.ProjectsList.as_view(), name='home'),
    path('collaborator/', views.CollaboratorList.as_view(), name='collaborator'),
    path('', views.determineView, name="greeting"),
    path('<slug:slug>/', views.ProjectDetailView.as_view(), name = 'project_detail'),
]