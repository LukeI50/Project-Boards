from django.db import models
from django.contrib.auth.models import User


STATUS = ((0, 'Backlog'), (1, 'Todo'), (2, 'In Progress'), (3, 'Done'))

# Create your models here.
class Todos(models.Model):
    class TaskStatus(models.IntegerChoices):
        BACKLOG = 0, "Backlog"
        TODO = 1, "Todo"
        IN_PROGRESS = 2, "In Progress"
        DONE = 3, "Done"

    task_status = models.PositiveSmallIntegerField(choices=TaskStatus)

    title = models.CharField()
    slug = models.SlugField()
    status = models.TextChoices()
    date_created = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, name='created_by')
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()


class Project(models.Model):
    title = models.CharField()
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_boards')
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(User, name='last_update_by')
    authorised_editors = models.ForeignKey(User, related_name='editors')
    todos = models.ForeignKey(Todos)


