from django.forms import ModelForm
from .models import Task

class TaskCreateForm(ModelForm):
    class Meta:
        model = Task
        fields = ['task_summary', 'task_detail', 'task_deadline', 'task_status']



