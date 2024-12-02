from django.shortcuts import render, get_object_or_404
from django.views import generic
from .forms import NewProjectForm

from .models import Project

# Create your views here.
class ProjectsList(generic.ListView):

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return "None"
        else:
            return Project.objects.filter(owner=self.request.user)

    queryset = get_queryset

    template_name = 'project_board/index.html'
    paginate_by = 6


    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['project_form'] = NewProjectForm()
        return context

    


# def get_queryset(self):
#         return Food.objects.filter(user=self.request.user)

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