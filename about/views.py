from django.shortcuts import render, get_object_or_404
from .models import About

# Create your views here.
def about_detail(request):

    about = get_object_or_404(About)

    return render(
        request,
        "about/about.html",
        {"about": about},
    )