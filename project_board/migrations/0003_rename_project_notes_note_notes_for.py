# Generated by Django 4.2.16 on 2024-11-29 00:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('project_board', '0002_rename_project_tasks_task_associated_project'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='project_notes',
            new_name='Notes for',
        ),
    ]
