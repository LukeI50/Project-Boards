from django.db import models
from django.contrib.auth.models import User, Permission
from django.contrib.auth import get_user_model


STATUS = ((0, 'Backlog'), (1, 'Todo'), (2, 'In Progress'), (3, 'Done'))

def dud_user():
    return get_user_model().objects.get_or_create(username = 'deleted')[0]


# Create your models here.
class Project(models.Model):
    """
    Stores a single Project related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_owner")
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.OneToOneField(User, on_delete=models.SET(dud_user), blank=True, null=True, name='last_updated_by')
    # A Many to Many Field creates a sub table that links the relevant objects in their own table.
    # Technically this table is called project_board_authorised_editors
    authorised_editors = models.ManyToManyField(User, blank=True, related_name='authorised_editor')


class Task(models.Model):
    """
    Stores a single task related to :model:`Project`.
    """
    class TaskStatus(models.IntegerChoices):
        """
        Stores four integer choices for the status variable. 0 = Backlog, 1 = Todo, 2 = In Progress, 3 = Done.
        """
        BACKLOG = 0, "Backlog"
        TODO = 1, "Todo"
        IN_PROGRESS = 2, "In Progress"
        DONE = 3, "Done"
    
    status = models.PositiveBigIntegerField(choices=TaskStatus.choices, default=TaskStatus.BACKLOG)

    project = models.ForeignKey(Project, on_delete=models.CASCADE, name='project_tasks')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.OneToOneField(User, on_delete=models.SET(dud_user), name='task_creator')
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} | Created by: {self.created_by}, on {self.date_created}"


class Note(models.Model):
    """
    Stores a single Note related to :model:`Project`.
    """
    project = models.OneToOneField(Project, on_delete=models.CASCADE, name='project_notes')
    short = models.TextField()
    essay = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.project} Notes."