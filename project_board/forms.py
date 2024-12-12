from .models import Project, Note, Task
from django import forms


class NewProjectForm(forms.ModelForm):
    """
    Form for creating a new project.

    This form is used to collect data from users for creating a new project.
    It includes fields for the project title and description.

    Attributes:
        model (Model): The Django model associated with this form, which is the `Project` model.
        fields (tuple): A tuple of field names that should be included in the form. In this case,
                         it includes 'title' and 'description'.
    """

    class Meta:
        model = Project
        fields = (
            'title',
            'description',
        )


class NewTaskForm(forms.ModelForm):
    """
    Form for creating a new task.

    This form is used to collect data from users for creating a new task.
    It includes fields for the task title, content, and status.

    Attributes:
        model (Model): The Django model associated with this form, which is the `Task` model.
        fields (tuple): A tuple of field names that should be included in the form. In this case,
                         it includes 'taskTitle', 'content', and 'status'.
    """

    class Meta:
        model = Task
        fields = (
            'taskTitle',
            'content',
            'status',
        )


class EditShortNotes(forms.ModelForm):
    """
    Form for editing short notes.

    This form is used to collect data from users for editing the short content of a note.
    It includes a single field for the short note content.

    Attributes:
        model (Model): The Django model associated with this form, which is the `Note` model.
        fields (tuple): A tuple of field names that should be included in the form. In this case,
                         it includes 'short'.
    """

    class Meta:
        model = Note
        fields = (
            'short',
        )
