from typing import Any

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from my_todo_app.models import Task
from .form import TaskCreateForm
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout

# Create your views here.

class TaskListView(LoginRequiredMixin, ListView):
    model = Task
    template_name = 'task_list.html'


    
class TaskCreateView(CreateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = '/'
    # def get_success_url(self, **kargs) -> str:
    #     return reverse_lazy('list')

class TaskUpdateView(UpdateView):
    model = Task
    form_class = TaskCreateForm
    template_name = 'task_create.html'
    success_url = '/'

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'task_create.html'
    success_url = '/'