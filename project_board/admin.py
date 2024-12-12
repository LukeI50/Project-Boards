from django.contrib import admin
from .models import Project, Task, Note
from django_summernote.admin import SummernoteModelAdmin
from guardian.admin import GuardedModelAdmin


@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin, GuardedModelAdmin):
    """
    Admin interface for managing projects.

    This class provides a custom admin interface for the Project model,
    utilizing both Summernote and Guardian functionalities. It allows
    users to manage project titles, slugs, creation dates, authorised editors,
    and descriptions with rich text editing capabilities.

    Attributes:
        list_display (tuple): Fields displayed in the list view of projects.
        search_fields (list): Fields that can be searched through in the admin interface.
        list_filter (tuple): Fields by which the project list can be filtered.
        prepopulated_fields (dict): Fields whose values are automatically generated from other fields.
        summernote_fields (tuple): Fields for which Summernote rich text editor is enabled.
    """

    list_display = ('title', 'slug', 'date_created')
    search_fields = ['title']
    list_filter = ('authorised_editor',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing tasks.

    This class provides a custom admin interface for the Task model,
    utilizing Summernote functionalities. It allows users to manage task titles,
    statuses, last updated times, associated projects, and task contents
    with rich text editing capabilities.

    Attributes:
        list_display (tuple): Fields displayed in the list view of tasks.
        search_fields (list): Fields that can be searched through in the admin interface.
        list_filter (tuple): Fields by which the task list can be filtered.
        prepopulated_fields (dict): Fields whose values are automatically generated from other fields.
        summernote_fields (tuple): Fields for which Summernote rich text editor is enabled.
    """

    list_display = (
        'taskTitle',
        'status',
        'last_updated',
        'associated_project',
    )
    search_fields = ['taskTitle']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('taskTitle',)}
    summernote_fields = ('content',)


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing notes.

    This class provides a custom admin interface for the Note model,
    utilizing Summernote functionalities. It allows users to manage note sources,
    last updated times, and both short and detailed note contents with rich text
    editing capabilities.

    Attributes:
        list_display (tuple): Fields displayed in the list view of notes.
        search_fields (list): Fields that can be searched through in the admin interface.
        summernote_fields (tuple): Fields for which Summernote rich text editor is enabled.
    """

    list_display = ('Notes_from', 'last_updated')
    search_fields = ['Notes_from']
    summernote_fields = ('short', 'essay',)
