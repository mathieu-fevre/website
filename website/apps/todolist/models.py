from django.db import models

# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)

    class Meta:
        db_table = 'todolist_task'

    def __str__(self):
        return self.name
    
