from django.shortcuts import render
from django.views import generic

from .models import Project

# Create your views here.
class ProjectsList(generic.ListView):
    model = Project