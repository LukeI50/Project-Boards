from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import NewProjectForm

from .models import Project

# Create your views here.
class ProjectsList(generic.ListView):
    template_name = 'project_board/index.html'
    paginate_by = 6


    def get_queryset(self):
        if self.request.user.is_anonymous:
            return "None"
        else:
            return Project.objects.filter(owner=self.request.user)

    queryset = get_queryset

    def post(self, request, *args, **kwargs):
        form = NewProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.last_edited_by = request.user
            new_project.save()
            return redirect('home')
        else:
            context = self.get_context_data()
            context['project_form'] = form
            return self.render_to_response(context)

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