from .models import Project, Note, Task
from django import forms

class NewProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = (
            'title',
            'description',
        )

class NewTaskForm(forms.ModelForm):    
    class Meta:
        model = Task
        fields = (
            'taskTitle',
            'content',
            'status',
        )

class EditShortNotes(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'short',
        )