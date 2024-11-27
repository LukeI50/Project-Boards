from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def projectsList(request):
    return HttpResponse("Hello, World!")