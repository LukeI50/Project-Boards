from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic


from .forms import NewProjectForm, NewTaskForm
from .models import Project, Task, Note



# Create your views here.

def determineView(request):
    """
    Redirects user to projects page/home if they are authenticated, 
    otherwise it renders the welcome page.
    """
    if request.user.is_authenticated:
        return redirect('home')
    else:
        return render(
            request,
            template_name="project_board/greeting.html"
        )


class ProjectsList(generic.ListView):
    paginate_by = 4
    # default template

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Project.objects.none() # return empty queryset for anonymous user
        else:
            return Project.objects.filter(owner=self.request.user).order_by('date_created')

    queryset = get_queryset
  
  
    # Render different templates based on resolution of device
    def get_template_names(self):
        screen_size = self.get_screen_size()

        if screen_size == "small":
            return ['project_board/mobile_index.html']
        else:
            return ['project_board/index.html']

    def get_screen_size(self):
        screen_size = self.request.COOKIES.get('currentMode', 0)
        return screen_size


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
    tasks_backlog = tasks.filter(status=0)
    tasks_todo = tasks.filter(status=1)
    tasks_in_progress = tasks.filter(status=2)
    tasks_done = tasks.filter(status=3)


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
            "is_project_detail": True,
        },
    )




class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'project_board/project_detail.html'
    context_object_name = 'project'

    def get_object(self, queryset=None):
        """
        Get the project from the Project model based on the slug passed.
        """
        slug = self.kwargs.get('slug')
        return get_object_or_404(Project, slug=slug)
    

    def get_context_data(self, **kwargs):
        """
        Add the additional context data for the tasks and notes to the template by
        passing them into the context.
        """
        context = super().get_context_data()
        project = context['project']


        note = Note.objects.filter(Notes_from=project).first()

        tasks = Task.objects.filter(associated_project=project).select_related('associated_project')
        tasks_backlog = tasks.filter(status=0)
        tasks_todo = tasks.filter(status=1)
        tasks_in_progress = tasks.filter(status=2)
        tasks_done = tasks.filter(status=3)


        context['note'] = note
        context['tasks_backlog'] = tasks_backlog
        context['tasks_todo'] = tasks_todo
        context['tasks_in_progress'] = tasks_in_progress
        context['tasks_done'] = tasks_done
        context['is_project_detail'] = True

        return context