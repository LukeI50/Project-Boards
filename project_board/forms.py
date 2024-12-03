from .models import Project, Note, Task
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
        )