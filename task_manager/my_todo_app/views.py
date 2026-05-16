from typing import Any

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView
from my_todo_app.models import Task
from .form import TaskCreateForm
from django.urls import reverse_lazy
# Create your views here.

class TaskListView(ListView):
    model = Task
    template_name = 'task_list.html'


    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = '/'
    # def get_success_url(self, **kargs) -> str:
    #     return reverse_lazy('list')
    