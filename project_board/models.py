from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User, Permission
from django.contrib.auth import get_user_model


STATUS = ((0, 'Backlog'), (1, 'Todo'), (2, 'In Progress'), (3, 'Done'))


def dud_user():
    """
    Returns a dummy user with the username 'deleted'.
    If the user does not exist, it creates one.
    """
    return get_user_model().objects.get_or_create(username='deleted')[0]


class Project(models.Model):
    """
    Represents a project in the application.

    Attributes:
        title (CharField): The title of the project. Must be unique.
        slug (CharField): A URL-friendly version of the title. Must be unique.
        owner (ForeignKey): The user who owns the project. Cascades on deletion.
        description (TextField): A short description of the project.
        date_created (DateField): The date when the project was created.
        last_updated (DateTimeField): The date and time when the project was last updated.
        last_updated_by (ForeignKey): The user who last updated the project. Uses a dummy user if the original user is deleted.
        authorised_editor (ManyToManyField): Users authorized to edit the project.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="project_owner"
    )
    description = models.TextField(max_length=180)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(
        User,
        on_delete=models.SET(dud_user),
        blank=True,
        null=True,
        name='last_updated_by'
    )
    # A Many to Many Field creates a sub table that links
    # the relevant objects in their own table.
    # Technically this table is called project_board_authorised_editors
    authorised_editor = models.ManyToManyField(
        User,
        blank=True,
        related_name='authorised_editor'
    )

    def __str__(self):
        return f"{self.title}"

    def save(self, *args, **kwargs):
        """
        Saves the project instance.
        
        If the slug is not provided, it creates a slug based on the title using `slugify`.
        Calls the superclass's `save` method to complete the save operation.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Task(models.Model):
    """
    Represents a task within a project.

    Attributes:
        status (PositiveBigIntegerField): The current status of the task. Uses choices from `TaskStatus`.
        project (ForeignKey): The project to which this task belongs. Cascades on deletion.
        taskTitle (CharField): The title of the task.
        slug (SlugField): A URL-friendly version of the task title.
        date_created (DateTimeField): The date and time when the task was created.
        author (ForeignKey): The user who authored the task. Uses a dummy user if the original user is deleted.
        last_updated (DateTimeField): The date and time when the task was last updated.
        content (TextField): The detailed content of the task.
    """
    class TaskStatus(models.IntegerChoices):
        """
        Enumeration of possible statuses for a task.

        Options:
            BACKLOG (0): Task is in the backlog stage.
            TODO (1): Task is ready to do.
            IN_PROGRESS (2): Task is currently being worked on.
            DONE (3): Task has been completed.
        """
        BACKLOG = 0, "Backlog"
        TODO = 1, "Todo"
        IN_PROGRESS = 2, "In Progress"
        DONE = 3, "Done"

    status = models.PositiveBigIntegerField(
        choices=TaskStatus.choices,
        default=TaskStatus.BACKLOG
    )

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        name='associated_project'
    )
    taskTitle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET(dud_user))
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    class Meta:
        """
        Meta options for the Task model.

        Attributes:
            ordering (list): Specifies that tasks should be ordered by their creation date.
        """
        ordering = ["date_created"]

    def __str__(self):
        return f"{self.taskTitle} | {self
                                     .author} Created on {self.date_created}"

    def save(self, *args, **kwargs):
        """
        Saves the task instance.

        If the slug is not provided, it creates a slug based on the task title using `slugify`.
        Calls the superclass's `save` method to complete the save operation.
        """
        if not self.slug:
            self.slug = slugify(self.taskTitle)
        super().save(*args, **kwargs)


class Note(models.Model):
    """
    Represents a note associated with a project.

    Attributes:
        project (OneToOneField): The project this note is related to. Uses the primary key of the project.
        short (TextField): A brief note about the project.
        essay (TextField): A detailed note about the project.
        last_updated (DateTimeField): The date and time when the note was last updated.
    """
    project = models.OneToOneField(
        Project,
        on_delete=models.CASCADE,
        primary_key=True,
        name='Notes_from'
    )
    short = models.TextField()
    essay = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.last_updated}"
