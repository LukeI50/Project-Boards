from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User, Permission
from django.contrib.auth import get_user_model


STATUS = ((0, 'Backlog'), (1, 'Todo'), (2, 'In Progress'), (3, 'Done'))

def dud_user():
    return get_user_model().objects.get_or_create(username = 'deleted')[0]



class Project(models.Model):
    """
    Stores a single Project related to :model:`auth.User`.
    """
    title = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="project_owner")
    description = models.TextField(max_length=180)
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET(dud_user), blank=True, null=True, name='last_updated_by')
    # A Many to Many Field creates a sub table that links the relevant objects in their own table.
    # Technically this table is called project_board_authorised_editors
    authorised_editor = models.ManyToManyField(User, blank=True, related_name='authorised_editor')

    def __str__(self):
        return f"{self.title}"
    
    def save(self, *args, **kwargs):
        """
        Ensures the slugification process has taken place
        in the event a slug did not populate automatically.
        """
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


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

    project = models.ForeignKey(Project, on_delete=models.CASCADE, name='associated_project')
    taskTitle = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.SET(dud_user))
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()


    class Meta:
        """
        passes ordering value to the :model:`Task`.
        """
        ordering = ["date_created"]
    
    def __str__(self):
        return f"{self.taskTitle} | {self.author} Created on {self.date_created}"
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.taskTitle)
        super().save(*args, **kwargs)



class Note(models.Model):
    """
    Stores a single Note related to :model:`Project`.
    """
    project = models.OneToOneField(Project, on_delete=models.CASCADE, primary_key=True, name='Notes_from')
    short = models.TextField()
    essay = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.last_updated}"