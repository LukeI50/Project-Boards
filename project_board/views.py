from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect

from .forms import NewProjectForm, NewTaskForm, EditShortNotes
from .models import Project, Task, Note


def task_delete(request, slug, task_id):
    """
    View to delete a specific task from a project.

    Args:
        request: The HTTP request object.
        slug (str): The slug of the project.
        task_id (int): The ID of the task to be deleted.

    Returns:
        HttpResponseRedirect: Redirects to the project detail page after deletion or an error message.
    """
    queryset = Project.objects.all()
    project = get_object_or_404(queryset, slug=slug)
    task = get_object_or_404(Task, pk=task_id)

    if task.author == (request.user or
                       project.authorised_editor.contains(request.user)):
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
    View to edit a specific task within a project.

    Args:
        request: The HTTP request object.
        slug (str): The slug of the project.
        task_id (int): The ID of the task to be edited.

    Returns:
        HttpResponseRedirect: Redirects to the project detail page after editing or an error message.
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
    """
    View to list all projects owned by the logged-in user.

    Attributes:
        model (Model): The Project model.
        template_name (str): The default template name for rendering the view.
    """

    def get_queryset(self):
        """
        Returns a queryset of projects owned by the logged-in user.

        Returns:
            QuerySet: A filtered queryset of projects.
        """
        if self.request.user.is_anonymous:
            # return empty queryset for anonymous user
            return Project.objects.none()
        else:
            return Project.objects.filter(owner=self.request
                                          .user).order_by('date_created')

    # Render different templates based on width of display
    # Override class get_template_names
    def get_template_names(self):
        """
        Determines the template to use based on the screen size.

        Returns:
            list: A list containing the name of the template to be used.
        """
        screen_size = self.get_screen_size()

        if screen_size == "small":
            return ['project_board/index_small.html']
        else:
            return ['project_board/index_default.html']

    # get size of display and return string
    def get_screen_size(self):
        """
        Retrieves the screen size from cookies.

        Returns:
            str: The current mode of the screen (e.g., 'small', 'default').
        """
        screen_size = self.request.COOKIES.get('currentMode', 0)
        return screen_size

    # AI generated code: //with alterations to make fit better
    # end of AI code

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new project.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponseRedirect: Redirects to the home page after creating a new project.
        """
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
            # Note model has a OneToOneField, so it requires an
            # associated project
            Note.objects.create(
                Notes_from=new_project,    # Associating with new project
                short="Default short description",
                essay="This is a default essay for the new project."
            )

            return redirect('home')
        else:
            context = self.get_context_data()
            context['project_form'] = form
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context dictionary for rendering the template.
        """
        context = super().get_context_data()
        context['project_form'] = NewProjectForm()
        return context


class CollaboratorList(generic.ListView):
    """
    View to list all projects where the logged-in user is an authorized collaborator.

    Attributes:
        model (Model): The Project model.
        template_name (str): The default template name for rendering the view.
    """

    def get_template_names(self):
        """
        Determines the template to use based on the screen size.

        Returns:
            list: A list containing the name of the template to be used.
        """
        screen_size = self.get_screen_size()

        if screen_size == "small":
            return ['project_board/index_small.html']
        else:
            return ['project_board/index_default.html']

    def get_screen_size(self):
        """
        Retrieves the screen size from cookies.

        Returns:
            str: The current mode of the screen (e.g., 'small', 'default').
        """
        screen_size = self.request.COOKIES.get('currentMode', 0)
        return screen_size

    def get_queryset(self):
        """
        Returns a queryset of projects where the logged-in user is an authorized collaborator.

        Returns:
            QuerySet: A filtered queryset of projects.
        """
        if self.request.user.is_anonymous:
            return Project.objects.none()
        else:
            return Project.objects.filter(authorised_editor=self.request.user)


class ProjectDetailView(generic.DetailView):
    """
    View to display details of a specific project, including its tasks and notes.

    Attributes:
        model (Model): The Project model.
        template_name (str): The default template name for rendering the view.
        context_object_name (str): The name of the context object containing the project instance.
    """

    model = Project
    template_name = 'project_board/project_detail.html'
    context_object_name = 'project'

    def get_template_names(self):
        """
        Determines the template to use based on the screen size.

        Returns:
            list: A list containing the name of the template to be used.
        """
        screen_size = self.get_screen_size()

        if screen_size == "small" or screen_size == "default":
            return ["project_board/project_detail_default.html"]
        else:
            return ['project_board/project_detail_large.html']

    def get_screen_size(self):
        """
        Retrieves the screen size from cookies.

        Returns:
            str: The current mode of the screen (e.g., 'small', 'default').
        """
        screen_size = self.request.COOKIES.get('currentMode', 0)
        return screen_size

    def get_object(self, queryset=None):
        """
        Retrieves the project instance based on the slug.

        Returns:
            Project: The project instance.
        """
        slug = self.kwargs.get('slug')
        return get_object_or_404(Project, slug=slug)

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests to create a new project or task, or update notes.

        Args:
            request: The HTTP request object.
            *args: Additional positional arguments.
            **kwargs: Additional keyword arguments.

        Returns:
            HttpResponseRedirect: Redirects back to the project detail page after processing.
        """
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
            # Note model has a OneToOneField, so it requires an
            # associated project
            Note.objects.create(
                Notes_from=new_project,    # Associating with new project
                short="Default short description",
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

            return redirect('project_detail', slug=project.slug)

        elif noteForm.is_valid():
            note, created = Note.objects.get_or_create(Notes_from=project)
            note.short = noteForm.cleaned_data['short']
            note.save()
            messages.add_message(
                request,
                messages.SUCCESS,
                'Note successfully updated.'
            )

            return redirect('project_detail', slug=project.slug)

        else:
            context = self.get_context_data(project=project)
            context['project_form'] = projectForm
            context['task_form'] = taskForm
            context['edit_short_notes'] = noteForm
            return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        """
        Adds additional context data to the template.

        Args:
            **kwargs: Additional keyword arguments.

        Returns:
            dict: The context dictionary for rendering the template.
        """
        context = super().get_context_data()
        project = context['project']

        note = Note.objects.filter(Notes_from=project).first()

        tasks = Task.objects.filter(
            associated_project=project).select_related('associated_project')
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
