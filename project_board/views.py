from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import NewProjectForm, NewTaskForm, EditShortNotes
from .models import Project, Task, Note


# Create your views here.

def task_delete(request, slug, task_id):
    """
    View to delete tasks
    """
    queryset = Project.objects.all()
    project = get_object_or_404(queryset, slug=slug)
    task = get_object_or_404(Task, pk=task_id)

    if task.author == request.user or project.authorised_editor.contains(request.user):
        task.delete()
        messages.add_message(
            request,
            messages.SUCCESS,
            "Task successfully deleted!",
        )
    else:
        messages.add_message(
            request,
            messages.ERROR,
            "Unable to delete task!"
        )

    return HttpResponseRedirect(reverse('project_detail', args=[slug]))


def task_edit(request, slug, task_id):
    """
    View to edit tasks
    """

    if request.method == "POST":

        queryset = Project.objects.all()
        project = get_object_or_404(queryset, slug=slug)
        task = get_object_or_404(Task, pk=task_id)
        task_form = NewTaskForm(data=request.POST, instance=task)

        if task_form.is_valid():
            task = task_form.save(commit=False)
            task.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                "Task Updated!",
            )
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Error updating task!"
            )

    return HttpResponseRedirect(reverse('project_detail', args=[slug]))


class ProjectsList(generic.ListView):
    # default template

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Project.objects.none() # return empty queryset for anonymous user
        else:
            return Project.objects.filter(owner=self.request.user).order_by('date_created')
  
    # Render different templates based on width of display
    def get_template_names(self):
        screen_size = self.get_screen_size()

        if screen_size == "small":
            return ['project_board/index_small.html']
        else:
            return ['project_board/index_default.html']

    def get_screen_size(self):
        screen_size = self.request.COOKIES.get('currentMode', 0)
        return screen_size

    # AI generated code: //with alterations to make fit better
    # end of AI code

    def post(self, request, *args, **kwargs):
        form = NewProjectForm(request.POST)
        if form.is_valid():
            new_project = form.save(commit=False)
            new_project.owner = request.user
            new_project.last_edited_by = request.user
            new_project.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                'New Project successfully created'
            )

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

    queryset = get_queryset

class CollaboratorList(generic.ListView):
    template_name = 'project_board/index.html'
    paginate_by = 4

    def get_queryset(self):
        if self.request.user.is_anonymous:
            return Project.objects.none()
        else:
            return Project.objects.filter(authorised_editor = self.request.user)
    
    queryset = get_queryset


class ProjectDetailView(generic.DetailView):
    """
    Amalgamate all models associated to a single instance of 
    a project board :model:`project_board.Project`.

    **Context**

    ``project``
        An instance of :model:`project_board.Project`.
    ``note``
        An instance of :model:`project_board.Note`.
    ``tasks``
        get all task instances linked to project :model:`project_board.Task`.

    
    **Template**

    :template:`project_board/project_detail.html`
    """

    model = Project
    template_name = 'project_board/project_detail.html'
    context_object_name = 'project'

    def get_template_names(self):
        screen_size = self.get_screen_size()

        if screen_size == "small" or screen_size == "default":
            return ["project_board/project_detail_default.html"]
        else:
            return ['project_board/project_detail_large.html']

    def get_screen_size(self):
        screen_size = self.request.COOKIES.get('currentMode', 0)
        return screen_size

    def get_object(self, queryset=None):
        """
        Get the project from the Project model based on the slug passed.
        """
        slug = self.kwargs.get('slug')
        return get_object_or_404(Project, slug=slug)
    
    def post(self, request, *args, **kwargs):
        slug = self.kwargs.get('slug')
        project = get_object_or_404(Project, slug=slug)

        projectForm = NewProjectForm(request.POST)
        taskForm = NewTaskForm(request.POST)
        noteForm = EditShortNotes(data=request.POST, instance=project)


        if projectForm.is_valid():
            new_project = projectForm.save(commit=False)
            new_project.owner = request.user
            new_project.last_edited_by = request.user
            new_project.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                'New Project successfully created'
            )


            # Automatically create a Note for the new project
            # Note model has a OneToOneField, so it requires an associated project
            Note.objects.create(
                Notes_from=new_project,    # Associating with new project
                short = "Default short description",
                essay="This is a default essay for the new project."
            )

            return redirect('project_detail', slug=project.slug)
        
        elif taskForm.is_valid():
            add_task = taskForm.save(commit=False)
            add_task.author = request.user
            add_task.associated_project = project
            add_task.save()

            messages.add_message(
                request,
                messages.SUCCESS,
                'Successfully created new task'
            )

            return redirect('project_detail', slug = project.slug)
        
        elif noteForm.is_valid():
            note, created = Note.objects.get_or_create(Notes_from=project)
            note.short = noteForm.cleaned_data['short']
            note.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Note successfully updated.'
            )

            return redirect('project_detail', slug = project.slug)

        else:
            context = self.get_context_data(project=project)
            context['project_form'] = projectForm
            context['task_form'] = taskForm
            context['edit_short_notes'] = noteForm
            return self.render_to_response(context)

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

        context['project_form'] = NewProjectForm()
        context['task_form'] = NewTaskForm()
        context['edit_short_notes'] = EditShortNotes(instance=note)

        return context