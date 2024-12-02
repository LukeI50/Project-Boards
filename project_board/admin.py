from django.contrib import admin
from .models import Project, Task, Note
from django_summernote.admin import SummernoteModelAdmin
from guardian.admin import GuardedModelAdmin

@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin, GuardedModelAdmin):
    list_display = ('title', 'slug', 'date_created')
    search_fields = ['title']
    list_filter = ('authorised_editor',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    list_display = ('title', 'status', 'last_updated', 'associated_project',)
    search_fields = ['title']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)


@admin.register(Note)
class NoteAdmin(SummernoteModelAdmin):
    list_display = ('Notes_from', 'last_updated')
    search_fields = ['Notes_from']
    summernote_fields = ('short', 'essay',)


# Register your models here.