from django.urls import path
from . import views

urlpatterns = [
    path('', views.about_detail, name = 'about_detail')
]