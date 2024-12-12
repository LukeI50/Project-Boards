from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About


@admin.register(About)
class AboutAdmin(SummernoteModelAdmin):
    """
    Admin interface for managing the about page content.

    This class provides a custom admin interface for the About model,
    utilizing Summernote functionalities. It allows users to manage the content
    of the about page with rich text editing capabilities.
    
    Attributes:
        summernote_fields (tuple): Fields for which Summernote rich text editor is enabled.
    """
    
    summernote_fields = ('content',)
