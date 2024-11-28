from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model


STATUS = ((0, 'Backlog'), (1, 'Todo'), (2, 'In Progress'), (3, 'Done'))

def dud_user():
    return get_user_model().objects.get_or_create(username = 'deleted')[0]


# Create your models here.
class Task(models.Model):
    class TaskStatus(models.IntegerChoices):
        BACKLOG = 0, "Backlog"
        TODO = 1, "Todo"
        IN_PROGRESS = 2, "In Progress"
        DONE = 3, "Done"

    status = models.PositiveSmallIntegerField(choices=TaskStatus.choices, default=TaskStatus.BACKLOG)

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    date_created = models.DateTimeField(auto_now_ad2d=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, name='created_by')
    last_updated = models.DateTimeField(auto_now=True)
    content = models.TextField()


class Note(models.Model):
    short = models.TextField()
    essay = models.TextField()


class Project(models.Model):
    title = models.CharField()
    slug = models.SlugField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='project_boards')
    description = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    last_updated_by = models.ForeignKey(User, on_delete=models.SET(dud_user), name='last_updated_by')
    allowed_editors = models.ForeignKey(User, on_delete=models.SET(dud_user), related_name='editors')
    tasks = models.ForeignKey(Task, on_delete=models.DO_NOTHING, name="todos")
    notes = models.ForeignKey(Note, on_delete=models.CASCADE, name="project notes")


