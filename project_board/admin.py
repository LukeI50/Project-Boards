from django.contrib import admin
from .models import Project, Task, Note
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Project)
class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'date_created')
    search_fields = ['title']
    list_filter = ('authorised_editors',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)

@admin.register(Task)
class TaskAdmin(SummernoteModelAdmin):
    list_display = ('associated_project', 'title', 'status', 'last_updated')
    search_fields = ['project']
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)

# Register your models here.
admin.site.register(Note)