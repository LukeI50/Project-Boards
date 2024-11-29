from django.contrib import admin
from .models import Project, Task, Note
from django_summernote.admin import SummernoteModelAdmin


class ProjectAdmin(SummernoteModelAdmin):
    list_display = ('title', 'slug', 'date_created')
    search_fields = ['title']
    list_filter = ('authorised_editors',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('description',)


# Register your models here.
admin.site.register(Project)
admin.site.register(Task)
admin.site.register(Note)