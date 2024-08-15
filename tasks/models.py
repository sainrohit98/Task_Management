from django.contrib.auth.models import User
from django.db import models

class Task(models.Model):
    TODO = 'Todo'
    INPROGRESS = 'Inprogress'
    DONE = 'Done'

    STATUS_CHOICES = [
        (TODO, 'Todo'),
        (INPROGRESS, 'Inprogress'),
        (DONE, 'Done')
    ]

    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=TODO)
    members = models.ManyToManyField(User, related_name='tasks')

    def __str__(self):
        return self.title
