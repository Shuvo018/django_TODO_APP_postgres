from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

TASK_STATUS = [
    ('PENDING', 'pending'),
    ('COMPLETED', 'completed'),
    ('INCOMPLETE', 'incomplete'),
]
class Task(TimeStampMixin):
    task_summary = models.CharField(max_length=100)
    task_detail = models.TextField()
    task_deadline = models.DateTimeField(blank=True, null=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='tasks')
    task_status = models.CharField(
        max_length=100,
        choices=TASK_STATUS,
        default= 'PENDING'
    )
    def __str__(self) -> str:
        return self.task_summary