from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Project

# Create your views here.
class ProjectsList(generic.ListView):

    queryset = Project.objects.filter()
    template_name = 'project_board/index.html'
    paginate_by = 6


def project_detail(request, slug):
    """
    Display an individual :model:`project_board.Project`

    **Context**

    ``project``
        An instance of :model:`project_board.Project`.
    
    **Template**

    :template:`project_board/project_detail.html`
    """

    queryset = Project.objects.all()
    project = get_object_or_404(queryset, slug = slug)

    return render(
        request,
        "project_board/project_detail.html",
        {"project": project},
    )