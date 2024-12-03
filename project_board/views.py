from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from .forms import NewProjectForm

from .models import Project, Task, Note


# Create your views here.
class ProjectsList(generic.ListView):
    template_name = 'project_board/index.html'
    paginate_by = 4


    def get_queryset(self):
        if self.request.user.is_anonymous:
            return "None"
        else:
            return Project.objects.filter(owner=self.request.user).order_by('date_created')

    queryset = get_queryset

    def post(self, request, *args, **kwargs):
        form = NewProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.last_edited_by = request.user
            new_project.save()

            # Automatically create a Note for the new project
            # Note model has a OneToOneField, so it requires an associated project
            Note.objects.create(
                Notes_from=new_project,    # Associating with new project
                short = "Default short description",
                essay="This is a default essay for the new project."
            )

            return redirect('home')
        else:
            context = self.get_context_data()
            context['project_form'] = form
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['project_form'] = NewProjectForm()
        return context


class CollaboratorList(generic.ListView):
    template_name = 'project_board/index.html'
    paginate_by = 4

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Project.objects.none()
        else:
            return Project.objects.filter(authorised_editor = self.request.user)
    
    queryset = get_queryset
        




def project_detail(request, slug):
    """
    Display an individual :model:`project_board.Project`

    **Context**

    ``project``
        An instance of :model:`project_board.Project`.
    
    **Template**

    :template:`project_board/project_detail.html`
    """

    project = get_object_or_404(Project, slug = slug)

    note = Note.objects.filter(Notes_from=project).first()

    tasks = Task.objects.filter(associated_project = project).select_related('associated_project')
    tasks_backlog = tasks.filter(status=0).select_related('status')
    tasks_todo = tasks.filter(status=1).select_related('status')
    tasks_in_progress = tasks.filter(status=2).select_related('status')
    tasks_done = tasks.filter(status=3).select_related('status')


    return render(
        request,
        "project_board/project_detail.html",
        {
            "project": project,
            "note": note,
            "tasks_backlog": tasks_backlog,
            "tasks_todo": tasks_todo,
            "tasks_in_progress": tasks_in_progress,
            "tasks_done": tasks_done,
        },
    )