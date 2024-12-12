from django.shortcuts import render, get_object_or_404
from .models import About


def about_detail(request):
    """
    View function to display the latest About page content.

    This view retrieves the most recently updated About model instance and renders it
    in the "about/about.html" template. If no About instance is found, a 404 error will be raised.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: A response object that renders the "about/about.html" template with the latest About instance.
    """

    about = About.objects.all().order_by('updated_on').first()

    return render(
        request,
        "about/about.html",
        {"about": about},
    )
